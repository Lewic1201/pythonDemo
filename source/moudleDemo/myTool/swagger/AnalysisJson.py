import requests
import os
import json
from source.moudleDemo.myTool.swagger.writeExcel import Write_excel  # 写入excel模块
from source.moudleDemo.myTool.swagger.logger import Log  # 打印日志模块
from source.moudleDemo.myTool.swagger.processingJson import write_data  # 写入json文件模块


class AnalysisJson:
    """swagger自动生成测试用例"""

    def __init__(self):
        # url_json = 'http://xxx.com/v2/api-docs?group=sign-api'  # json swagger url地址
        # url_json = 'http://192.168.199.143:18080/api/swagger-ui.html#/'
        # r = requests.get(url_json).json()

        with open("./sw.json", 'r',encoding='utf-8') as load_f:
            r = json.load(load_f)
        self.json_path = os.path.abspath(
            os.path.dirname(__file__)) + '\\case_generate' + '\\data' + '\\data.json'  # json file path
        self.excel_path = os.path.abspath(
            os.path.dirname(__file__)) + '\\case_generate' + '\\data' + '\\demo_api.xlsx'  # case path
        self.interface_params = {}
        self.log = Log()
        self.row = 2  # 写入excel起始行数
        self.num = 1  # case id
        self.case = {'1': 3, '2': 5, '3': 7, '4': 9}  # 参数为空，错误的情况  目前可以获取到的参数，最多4个，有9种简单的异常情况
        if self.check_data(r):
            self.data = r['paths']  # paths中的数据是有用的

    def check_data(self, r):
        if not isinstance(r, dict):
            self.log.info('swagger return json error.')
            return False
        else:
            return True

    def retrieve_data(self):
        """主函数"""
        global body_name, method
        for k, v in self.data.items():
            method_list = []
            for _k, _v in v.items():
                interface = {}
                if not _v.get('deprecated'):  # 接口是否被弃用
                    method_list.append(_k)
                    api = k  # api地址
                    if len(method_list) > 1:  # api地址下的请求方式不止一个的情况
                        for i in range(len(method_list)):
                            body_name = api.replace('/', '_') + '_' * i  # json文件对应参数名称，excel中body名称
                            method = method_list[-1]  # 请求方式 同一个api地址，不同请求方式
                    else:
                        body_name = api.replace('/', '_')
                        method = _k
                    self.interface_params = self.retrieve_excel(_v, interface, api)
                else:
                    self.log.info('interface path: {}, case name: {}, is deprecated.'.format(k, _v['description']))
                    break
        if self.interface_params:
            write_data(self.interface_params, self.json_path)  # 参数写入json文件

    def retrieve_excel(self, _v, interface, api):
        """解析参数，拼接为dict--准备完成写入excel的数据"""
        parameters = _v.get('parameters')  # 未解析的参数字典
        case_name = _v.get('description')  # 接口名称
        tags = _v['tags'][0]  # 标签名称
        if tags != '运维工具':  # 去除运维相关接口
            params_dict = self.retrieve_params(parameters)  # 处理接口参数，拼成dict形式
            params_list = list(params_dict.keys())  # 接口参数存到list中
            if params_dict:  # 单个或多个参数
                for i in range(self.case.get(str(len(params_dict)),0)):  # 根据接口参数数量，生成异常用例
                    body_name_all = body_name + str(i)  # 重新拼接body_name
                    interface['row_num'] = self.row  # 写入excel时的所在行
                    interface['id'] = 'test_' + str(self.num)  # case id
                    interface['tags'] = tags  # 标签名称
                    case_name_except = self.rewrite_case_name(i, case_name, params_list)  # 异常接口名称
                    interface['name'] = case_name_except  # case中文描述
                    _type = 'json'  # 参数获取方式
                    interface['method'] = method  # 请求方式
                    interface['url'] = 'http://xxx.com' + api  # 拼接完成接口url
                    interface['headers'] = 'yes'  # 是否传header
                    interface['body'] = body_name_all
                    interface['type'] = _type
                    self.num += 1
                    self.row += 1
                    self.manual_processing(params_list, case_name, body_name_all)  # 记录需要手动处理的case
                    self.interface_params[body_name_all] = params_dict  # 参数拼成dict
                    # self.write_excel(interface, self.excel_path)  # 参数写入excel
            else:  # 不传参数
                _type = 'data'
                interface['name'] = case_name
                interface['row_num'] = self.row
                interface['id'] = 'test_' + str(self.num)
                interface['tags'] = tags
                interface['method'] = method
                interface['url'] = 'http://xxx.com' + api
                interface['headers'] = 'yes'
                interface['body'] = body_name
                interface['type'] = _type
                self.num += 1
                self.row += 1
                self.interface_params[body_name] = params_dict
                # self.write_excel(interface, self.excel_path)
        return self.interface_params

    def retrieve_params(self, parameters):
        """处理参数，转为dict"""
        params = ''
        _in = ''
        if not parameters:
            return {}
        for each in parameters:
            _in += each.get('in') + '\n'  # 参数传递位置
            params += each.get('name') + '\n'  # 参数
        _in = _in.strip('\n')
        _in_list = _in.split('\n')
        params = params.strip('\n')
        params_list = params.split('\n')
        del_list = params_list.copy()
        for i in range(len(_in_list)):
            if _in_list[i] == 'header':
                params_list.remove(del_list[i])  # 只保存在body传的参数
        test_list = params_list.copy()
        params_dict = dict(zip(params_list, test_list))  # 把list转为dict
        return params_dict

    def write_excel(self, interface, filename):
        """把dict中的值写入对应的excel行中"""
        wt = Write_excel(filename)
        try:
            wt.write(interface['row_num'], 1, interface['id'])
            wt.write(interface['row_num'], 2, interface['tags'])
            wt.write(interface['row_num'], 3, interface['name'])
            wt.write(interface['row_num'], 4, interface['method'])
            wt.write(interface['row_num'], 5, interface['url'])
            wt.write(interface['row_num'], 7, interface['headers'])
            wt.write(interface['row_num'], 8, interface['body'])
            wt.write(interface['row_num'], 9, interface['type'])
            self.log.info('Interface case id {},write to excel file successfully!'.format(interface['id']))
        except Exception as e:
            self.log.info('Failure of interface use case to write to excel file! error:{}\n'.format(e))
            return

    def rewrite_case_name(self, i, case_name, params_list):
        """使case更加易读，给异常用例补全名称"""
        global case_name_except
        if not case_name:
            case_name = ''
        if i == 0:
            case_name_except = case_name + '-正常传参'
        if i == 1:
            case_name_except = case_name
            case_name_except = case_name_except + '-' + params_list[0] + '为空'
        if i == 2:
            case_name_except = case_name
            case_name_except = case_name_except + '-' + params_list[0] + '错误'
        if i > 2:
            if i == 3:
                case_name_except = case_name
                case_name_except = case_name_except + '-' + params_list[1] + '为空'
            if i == 4:
                case_name_except = case_name
                case_name_except = case_name_except + '-' + params_list[1] + '错误'
        if i > 4:
            if i == 5:
                case_name_except = case_name
                case_name_except = case_name_except + '-' + params_list[2] + '为空'
            if i == 6:
                case_name_except = case_name
                case_name_except = case_name_except + '-' + params_list[2] + '错误'
        return case_name_except

    def manual_processing(self, params_list, case_name, body_name):
        """"记录需要手动处理的case"""
        if 'param' in params_list:
            self.log.info(
                'case: {} json file params:  {} , need to enter parameters manually.\n'.format(case_name, body_name))


if __name__ == '__main__':
    AnalysisJson().retrieve_data()
