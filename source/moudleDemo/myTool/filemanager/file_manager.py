#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 12:48
# @Author  : Administrator
# @File    : rename_file.py
# @Software: PyCharm
# @context :

import datetime
import os
import os.path as op
import re
import time
import sys
import winshell
import win32com.client

from source.utils.logs import logger
from source.application.pingyin.pinyin import PinYin

from source.utils.decorators import print_cls

"""[正则表达式,表达式说明]"""
RE_ALL = [r'.*', '所有文件']
RE_SUFFIX = [r'.*\.mp3', '匹配文件后缀']
RE_PREFIX = [r'ABC123.*', '匹配文件前缀']
RE_HAS_CHINESE = [u".*[\u4e00-\u9fa5]+.*", '包含中文']
RE_HAS_KOREAN = [u".*[\uAC00-\uD7A3]+.*", '包含韩文']
RE_HAS_JAPAN = [u".*[\u0800-\u4e00]+.*", '包含日文']


def get_now_time(formats='%Y-%m-%d %H:%M:%S'):
    now_time = datetime.datetime.now().strftime(formats)
    return now_time


def TimeStampToTime(timestamp, format='%Y-%m-%d %H:%M:%S'):
    """把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12"""
    timeStruct = time.localtime(timestamp)
    return time.strftime(format, timeStruct)


def create_lnk(target, lnkdir=None, filename=None, description="", is_desk=False, is_cover=True):
    """
    创建快捷方式

    :param target: 指向路径
    :param lnkdir: lnk保存路径 默认与target同目录
    :param filename: 快捷方式名称 默认target
    :param description: 备注
    :param is_desk: 是否为创建桌面快捷方式
    :param is_cover: 是否覆盖同名快捷方式
    :return:
    """
    try:
        if is_desk:
            # 桌面快捷
            lnkdir = winshell.desktop()
        elif not lnkdir:
            # 当前路径
            lnkdir = os.path.dirname(target)

        # 默认原文件名
        filename = filename if filename else os.path.basename(target)
        # 文件全路径
        file_name = os.path.join(lnkdir, os.path.basename(filename) + ".lnk")
        if not is_cover:
            # 快捷方式已存在时,文件名添加下标
            serial = 1
            while os.path.exists(file_name):
                file_name = os.path.join(lnkdir, os.path.basename(filename) + '__' + str(serial) + ".lnk")
                serial += 1

        winshell.CreateShortcut(
            Path=file_name,
            Target=target,
            Icon=(target, 0),
            # 文件备注
            Description=description)

        print('create lnk success, path: %s' % file_name)
    except Exception:
        raise


def get_lnk_info(lnk_name):
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        if os.path.isfile(lnk_name) and lnk_name[-4:] == '.lnk':
            shortcut = shell.CreateShortCut(lnk_name)
            target_path = shortcut.Targetpath
            print(target_path)
            return target_path
        else:
            print('lnk name error: %s' % lnk_name)
    except Exception:
        raise


class FileManage:
    """文件管理系统"""

    def __init__(self, path):
        self.root_dir = path

    def get_dir_structure(self):
        """
        获取当前目录文件结构
        :return: 每个文件夹下的文件
        :rtype: [(文件夹路径,路径下的文件夹,路径下的文件),...]
        """
        rootdir = self.root_dir
        ret = []
        if not rootdir or not os.path.exists(rootdir):
            return []
        for i in os.walk(rootdir):
            ret.append(i)
        return ret

    # @print_cls
    def get_all_filelist(self):
        """
        获取当前目录下所有文件路径
        :return: 路径列表
        :rtype: list
        """
        rootdir = self.root_dir
        if not rootdir or not os.path.exists(rootdir):
            return []

        def list_all_files(dir_path):
            _files = []
            # 列出文件夹下所有的目录与文件
            file_list = os.listdir(dir_path)
            for i in range(0, len(file_list)):
                file_name = os.path.join(dir_path, file_list[i])
                if os.path.isdir(file_name):
                    _files.extend(list_all_files(file_name))
                if os.path.isfile(file_name):
                    _files.append(file_name)
            return _files

        result = list_all_files(rootdir)
        # 过滤文件夹
        for i in range(len(result)):
            if os.path.isdir(result[i]):
                result.pop(i)
        return result

    def sort_file_list(self, file_list):
        pass

    # @print_cls
    def filter_files_by_name(self, re_expressions, file_list=None, nameorpath=True):
        """
        按正则过滤掉file_list下符合条件的文件

        :param file_list 文件列表(绝对路径)
        :param re_expressions 正则表达式 或 正则表达式列表
        :param nameorpath 通过文件名过滤,或者通过文件路径过滤
        :return [绝对路径]
        :rtype list
        """

        # 按正则表达式过滤file_list
        def filter_inner(re_expression, files):
            pattern = re.compile(re_expression)
            result = []
            for f in files:
                fn = os.path.basename(f)
                if op.isdir(f):
                    continue
                if nameorpath:
                    if not re.match(pattern, fn):
                        result.append(f)
                else:
                    if not re.match(pattern, f):
                        result.append(f)
                pass
            return result

        if not file_list:
            file_list = self.get_all_filelist()
        if isinstance(re_expressions, str):
            # 传入一条正则表达式
            ret = filter_inner(re_expressions, file_list)
        elif isinstance(re_expressions, list):
            # 传入为正则表达式列表,那么递归过滤
            ret = file_list
            for re_ex in re_expressions:
                ret = filter_inner(re_ex, ret)
        else:
            # 其它类型不过滤
            ret = file_list

        return ret

    # @print_cls
    def get_files_by_name(self, re_expressions, file_list=None, nameorpath=True):
        """按正则获取file_list下符合条件的文件
        :param file_list 文件列表(绝对路径)
        :param re_expressions 正则表达式 或 正则表达式列表
        :param nameorpath 通过文件名过滤,或者通过文件路径过滤
        :rtype list
        """

        # 按正则表达式获取file_list
        def get_inner(re_expression, files):
            pattern = re.compile(re_expression)
            result = []
            for f in files:
                fn = os.path.basename(f)
                if op.isdir(f):
                    continue
                if nameorpath:
                    if re.match(pattern, fn):
                        result.append(f)
                else:
                    if re.match(pattern, f):
                        result.append(f)
                pass
            return result

        ret = []
        if not file_list:
            file_list = self.get_all_filelist()
        if isinstance(re_expressions, str):
            # 传入一条正则表达式
            ret = get_inner(re_expressions, file_list)
        elif isinstance(re_expressions, list):
            # 传入为正则表达式列表,获取每一种规则的文件
            for re_ex in re_expressions:
                a_ret = get_inner(re_ex, file_list)
                ret.extend(a_ret)

        return ret

    def get_files_by_size(self, min_size=None, max_size=None, file_list=None):
        """
        通过文件大小过滤出列表中符合条件的文件

        :param min_size:
        :param max_size:
        :param file_list:
        :return:
        """
        file_list = file_list if file_list else self.get_all_filelist()

        ret = []
        for ff in file_list:
            size = self.get_size(ff)
            if min_size and size < min_size:
                continue
            if max_size and size > max_size:
                continue
            ret.append(ff)
        return ret

    def change_names(self, file_list, flag):
        """
        批量按指定规则修改文件名

            修改规则:1  将(A001)(    )(ABC-123asdf)(.mp3)文件中空格等距
                    2  简单的首尾替换
                    3  将所有汉字转为拼音
                    4  将所有文字翻译
        """
        try:
            for ff in file_list:
                self.change_name(ff, flag)
        except Exception:
            raise

    @print_cls
    def change_name(self, file_name, flag, file_new_name=''):
        """
        修改文件名
        :param file_name: 文件名(绝对路径)
        :param file_new_name: 新的文件名
        :param flag: 修改规则
        :return:

        修改规则:1  将(A001)(    )(ABC-123asdf)(.mp3)文件中空格等距
                2  简单的首尾替换
                3  将所有汉字转为拼音
                4  将所有文字翻译
        """

        file_path = op.split(file_name)[0]
        basename = op.basename(file_name)
        name, tp = op.splitext(basename)

        # 修改规则字典,可添加新方法
        rule = {
            1: self.get_format1_name,
            2: self.get_format2_name,
            3: self.get_format3_name,
            4: self.get_format4_name,
            5: self.get_format5_name,
        }
        # 是否改为默认的新名字
        if not file_new_name:
            new_name = rule[flag](name)

            file_new_name = op.join(file_path, new_name + tp)
        else:
            new_name = op.split(file_new_name)[1]
        if name != new_name:
            try:
                message = 'info: ' + '\033[5;33;0m' + name + '\033[5;34;0m' + ' ---->>>> ' + '\033[5;33;0m' \
                          + new_name + '\033[0m'
                # 文件已存在跳过
                if os.path.exists(file_new_name):
                    logger.error('error:' + message[5:])
                    logger.error('文件已存在,不能修改文件名')
                else:
                    os.rename(file_name, file_new_name)
                print(message)
                return True
            except FileNotFoundError:
                err_message = 'warning: ' + '\033[5;31;0m' + 'file "' + file_name + '" not found' + '\033[0m'
                print(err_message)
                raise
        return False

    def get_format1_name(self, name):
        """
        改名1规则: 将(A001)(    )(ABC-123asdf)(.mp3)文件中空格等距,不符合规则不修改
        :param name: 仅文件名
        :return: 新文件名
        :rtype: str
        """
        # 将文件名分成四部分(A001)(    )(ABC-123asdf)(.mp3)
        pattern_01 = re.compile(r'^(\w\d{3})(\s{3,})(.*)(\.\w{2,4})$')
        # pattern_02 = re.compile(r'^.*(阳光电影www\.ygdy8\.com\.).*$')
        check_result = re.match(pattern_01, name)

        new_name = name
        if check_result:  # 查找头部，没有匹配
            prefix = check_result.group(1)
            speace = check_result.group(2)
            name_content = check_result.group(3)
            suffix = check_result.group(4)

            new_name = prefix + '                       ' + name_content + suffix
            return new_name

        return new_name

    def get_format2_name(self, name):
        """
        改名2规则: 文件名部分替换,不符合规则不修改
        :param name: 仅文件名
        :return: 新文件名
        :rtype: str
        """
        # 将文件名分成四部分(A001)(    )(ABC-123asdf)(.mp3)
        # 如微信打不开请输入www.kmyy.tv继续观看(9)
        # 西柚酱制作-猜猜猜8@小密圈特别
        new_name = name
        if '西柚酱制作-猜猜猜' in name:
            new_name = name.replace('西柚酱制作-猜猜猜', 'guessWho-').replace('@小密圈特别资源', '')
        return new_name

    def get_format3_name(self, name):
        """
        改名3规则: 将所有汉字转为拼音
        :param name: 仅文件名
        :return: 新文件名
        :rtype: str
        """
        # 过滤出带汉字的name
        pattern = RE_HAS_CHINESE[0]
        check_result = re.match(pattern, name)
        new_name = name
        if check_result:
            py = PinYin()
            # 汉字转拼音
            new_name = py.hanzi2pinyin_split(name)
        return new_name

    def get_format4_name(self, name):
        """
        改名4规则: 将所有文字翻译,自动翻译,其它语言翻译成汉语,汉语翻译成英语
        :param name: 仅文件名
        :return: 新文件名
        :rtype: str
        """
        new_name = Trans().translate(name)
        return new_name

    def get_format5_name(self, name):
        """
        改名4规则: 将所有文字翻译成字母
        :param name: 仅文件名
        :return: 新文件名
        :rtype: str
        """
        new_name = name
        if re.match(RE_HAS_KOREAN[0], name) or re.match(RE_HAS_JAPAN[0], name):
            new_name = Trans().translate(name)
        if re.match(RE_HAS_CHINESE[0], new_name):
            new_name = self.get_format3_name(new_name)

        return new_name

    def change_queue_name(self, file_list='', prefix='', suffix=''):
        """
        批量修改为序列文件名(并按不同类型文件分组)

        :param file_list:
        :param prefix: 文件名前缀 eg:'ShareCircle-'
        :param suffix: 文件名后缀 eg:'.mp4'
        :return:
        """

        # 传入过滤条件,可修改
        if not file_list:
            file_list = os.listdir(self.root_dir)

        queue_name = self.get_queue_name(len(file_list), prefix, suffix)
        maker = (name for name in queue_name)

        # 分组
        type_map = self.group_by_type(file_list)

        for tp in type_map:
            for ff in type_map[tp]:
                new_name = op.join(op.split(ff)[0], next(maker) + os.path.splitext(ff)[1])
                os.rename(ff, new_name)

    @staticmethod
    def get_queue_name(nums, prefix, suffix):
        """
        生成序列化的文件名
        :param nums: 生成数量
        :param prefix:
        :param suffix:
        :return: list
        eg: pre0001suf
        """
        name_list = []
        for i in range(nums):
            name = "%s{0:04d}%s".format(i) % (prefix, suffix)
            name_list.append(name)
        return name_list

    def group_by_type(self, file_list):
        """
        按文件类型分组

        :param file_list:
        :return: {str:[filename,...]}
        """

        type_map = dict()
        for ff in file_list:
            file_type = os.path.splitext(ff)[1]
            if file_type in type_map:
                type_map[file_type].append(ff)
            else:
                type_map[file_type] = [ff]
        return type_map

    @staticmethod
    def get_size(file_name):
        """获取文件的大小"""
        fsize = os.path.getsize(file_name)
        return fsize
        # 结果保留两位小数，单位为MB
        # fsize = os.path.getsize(file_name)
        # fsize = fsize / float(1024 * 1024)
        # return round(fsize, 2)

    @staticmethod
    def get_accessTime(file_name):
        """获取文件的访问时间"""
        t = os.path.getatime(file_name)
        return TimeStampToTime(t)

    @staticmethod
    def get_createTime(file_name):
        """获取文件的创建时间"""
        t = os.path.getctime(file_name)
        return TimeStampToTime(t)

    @staticmethod
    def get_modifyTime(file_name):
        """获取文件的修改时间"""
        t = os.path.getmtime(file_name)
        return TimeStampToTime(t)

    def get_file_params(self, file_name, lnk_target=False):
        """
        获取文件所有参数
        :param file_name:
        :param lnk_target: 替换lnk为lnk目标文件信息,默认不替换
        :return: {path:,name:,type,size:,createTime:,modifyTime:}
        """
        try:
            if lnk_target and os.path.isfile(file_name) and file_name[-4:] == '.lnk':
                print(file_name)
                target_name = get_lnk_info(file_name)
                if target_name:
                    file_name = target_name
            context = {'path': os.path.split(file_name)[0],
                       'name': os.path.split(file_name)[1],
                       'type': os.path.splitext(file_name)[1][1:],
                       'size': self.get_size(file_name),
                       'createTime': self.get_createTime(file_name),
                       'modifyTime': self.get_modifyTime(file_name)
                       }
            return context
        except Exception as e:
            print(file_name, e)
            raise

    # @print_cls
    def get_all_file_params(self, file_list=''):
        """
        获取当前文件夹下所有的文件参数
        :param file_list: 文件绝对路径列表
        :return: [{},...]
        """
        if not file_list:
            file_list = self.get_all_filelist()
        result = []
        for f in file_list:
            file_params = self.get_file_params(f)
            result.append(file_params)
        return result

    def save_all(self, save_file, file_list=None, lnk_target=False):
        """
        保存所有子文件信息到指定Excel文件
        :param save_file: 生成文件的绝对路径
        :param file_list: 要保存的文件名绝对路径(默认根目录下全部)
        :param lnk_target: 替换lnk为lnk目标文件信息,默认不替换
        :return:
        """
        if not file_list:
            file_list = self.get_all_filelist()
        # # 过滤文件夹
        # for i in range(len(file_list)):
        #     if os.path.isdir(file_list[i]):
        #         file_list.pop(i)

        # 获取所有文件信息
        file_info = []
        first = True
        for f in file_list:
            file_params = self.get_file_params(f, lnk_target)
            if first:
                # 添加表头
                file_info.append(list(file_params.keys()))
                first = False
            file_info.append(list(file_params.values()))

        # 保存信息
        now = get_now_time('%Y%m%d%H%M%S')
        file = save_info(save_file, now, file_info)

    @print_cls
    def save_name_map(self, save_file):
        """
        保存文件名及文件名翻译 到指定Excel文件
        :param save_file: 绝对路径
        :return:
        """
        file_list = self.get_all_filelist()
        datas = []
        header = ['path', 'name', 'type', 'pinyin', 'trans']
        datas.append(header)
        for file_name in file_list:
            print(file_name)
            path = os.path.split(file_name)[0]
            name = os.path.split(file_name)[1]
            types = os.path.splitext(file_name)[1][1:]
            pinyin = self.get_format3_name(name)

            no_expend_name = op.split(op.splitext(file_name)[0])[1]
            # 去掉文件扩展名
            trans = Trans().translate(no_expend_name)
            data = [path, name, types, pinyin, trans]
            datas.append(data)
        # 保存文件
        now = get_now_time('%Y%m%d%H%M%S')
        save_info(save_file, now, datas)

    # @print_cls
    def get_same_file(self, file_list=''):
        """
        获取大小相同的文件,方便去重
        :param file_list: 文件绝对路径列表
        :return: {size:[more file_path],...}
        :rtype: {int:list}
        """
        try:
            file_params = self.get_all_file_params(file_list)
            flen = len(file_params)
            repeats = {}
            group = {}
            for i in range(flen):
                # 添加文件绝对路径
                file_name = os.path.join(file_params[i].get('path'), file_params[i].get('name'))
                file_size = file_params[i].get('size')
                if file_size not in group:
                    group[file_size] = [file_name]
                else:
                    group[file_size].append(file_name)
            for j in group:
                if len(group[j]) > 1:
                    repeats[j] = group[j]
            return repeats
        except:
            raise

    def create_desktop_lnk(self):
        """为根目录创建桌面快捷方式"""

        destDir = winshell.desktop()
        target = self.root_dir
        file_name = os.path.join(destDir, os.path.basename(target) + ".lnk")

        winshell.CreateShortcut(
            Path=file_name,
            Target=target,
            Icon=(target, 0),
            Description="root_dir")

    def create_lnks(self, lnkdir, file_list=None):
        """批量创建文件快捷方式到指定目录"""
        file_list = file_list if file_list else self.get_all_filelist()

        if not os.path.exists(lnkdir):
            os.mkdir(lnkdir)
        for ff in file_list:
            create_lnk(ff, lnkdir=lnkdir)


if __name__ == '__main__':
    rootDir = os.path.abspath(os.path.join(__file__, '../../../../../'))
    path1 = 'G:\\Lenovo Limited Warranty_V1.2_UHD\\config\\new190113\\ShareCircle'
    path2 = 'G:\\Lenovo Limited Warranty_V1.2_UHD\\config'
    path3 = 'E:\\import_file\\disk_file'
    path5 = 'E:\\import_file\\name_map_file'
    path6 = r'E:\lewic\gitRepository\tmp'
    path7 = r'E:\bak\testlnk'
    path9 = r'E:\bak\testlnk2'
    path8 = r'E:\lewic\pycharm\workspace\myCode\pythonDemo'
    path10 = r'F:\tmp\lnk_pre3'
    path11 = r'F:\tmp\tmp2'
    path12 = r'E:\javalib\shortMessage'
    # fm = FileManage(path2)
    # fm.change_queue_name()
    # pprint.pprint(fm.get_all_file_params())
    # for ff in fm.get_all_filelist():
    #     # 批量修改文件名
    #     fm.change_name(ff)
    # fm.save_all(path3)
    # fm.save_name_map(path5)
    # fm.get_same_file()

    # special_file = ['.*\.git.*', '.*__init__.py', '.*\.pyc']
    # file_lists = fm.filter_files_by_name(special_file, nameorpath=False)
    # fm.get_files_by_name(special_file, nameorpath=False)

    # fm.get_same_file(file_lists)

    # ff = fm.filter_files_by_name(special_file, nameorpath=False)
    # fm.save_all(r'E:\tmp', ff)

    # ffs0 = fm.get_files_by_size(min_size=5000, max_size=10000)
    # ffs1 = fm.filter_files_by_name(['.*ShareCircle.*', '.*\.pyc'], ffs0)
    # fm.create_lnks(path9, ffs1)
    # fm.change_queue_name()

    # 获取pre文件快捷方式
    # fms = FileManage(path2)
    # fm_ls = fms.get_files_by_name([r'.*\\pre\\.*', r'.*\\pre_(mp4|avi)\\.*', r'.*\\java\\.*'], nameorpath=False)
    # fm_ls = fms.get_files_by_size(min_size=500 * 1024, file_list=fm_ls)
    # fm.create_lnks(path10, fm_ls)
    # fm2 = FileManage(path10)
    # fm2_list = fm2.get_all_filelist()
    # fm2.change_names(fm2_list, 5)

    # fm_list = fm.get_all_filelist()
    # fm.change_names(fm_list, 5)

    # flist = fm.get_all_filelist()
    # fm.change_names(flist, 2)
    #
    # fm.save_all(path2 + '\\..\\files')

    # # 文件去重
    # fms = FileManage(path2)
    # # fm_ls = fms.get_files_by_name([r'.*\\pre\\.*', r'.*\\pre_(mp4|avi)\\.*', r'.*\\java\\.*'], nameorpath=False)
    # fms2 = FileManage(path11)
    # fms_all = fms.get_all_filelist() + fms2.get_all_filelist()
    # fms_all = fms.filter_files_by_name([r'.*\.download', r'.*fox-.*', r'.*ShareCircle-.*'], fms_all)
    # same_file = fms.get_same_file(fms_all)
    # print('--')

    fm = FileManage(path12)
    fl = fm.get_all_filelist()
    import pprint
    pprint.pprint(fl)
