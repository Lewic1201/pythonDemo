"""
将api接口转换成给定的代码格式

"""

import re

from source.moudleDemo.myTool.editcode.getList import ret


# def read_file(filename, model='rb'):
#     with open(filename, model) as file:
#         context = file.read()
#     return context.decode('utf-8')


def write_file(filename, context, model='w'):
    with open(filename, 'w', encoding='utf-8')as file:
        file.write(context)


def deal_case_body(datas):
    """
    将api数据转换成代码
    :param datas: [[sendType,interface,doc],...]
    :return: str
    """
    case_method_context = ''
    content = set()
    for data in datas:
        # 取接口url的前缀
        headline = data[1].split('/')[1]
        if headline not in content:
            # case_method_context += '    # %s\n' % data[1]
            content.add(headline)
            data.append(headline)
        mname = data[0].lower() + re.sub('[{}]', '', re.sub('[-/]', '_', data[1]))
        line1 = "        suf_api = '%s'\n" % data[1]
        line2 = ''
        if data[0] == 'POST':
            line2 = '        data={}\n'
        line3_parm2 = ', data' if data[0] == 'POST' else ''
        line3 = '        status_code, response_json = self.client.{}(suf_api{})\n'.format(data[0].lower(), line3_parm2)
        line4 = '        self.assertEqual(status_code, 200)\n'

        method_def = '    def test_{}(self):\n        """{}"""\n'.format(mname, data[2])
        method_body = '{}{}{}{}\n'.format(line1, line2, line3, line4)
        data.append(method_def)
        data.append(method_body)
        case_method_context += (method_def + method_body)
    return datas, case_method_context


_, method_context = deal_case_body(ret)
write_file('case_method.txt', method_context)

print('generate code success')
