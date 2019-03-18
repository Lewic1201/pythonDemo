#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 13:33
# @Author  : li_panfeng
# @File    : generateRequirements.py
# @Software: PyCharm
# @context : 自动更新requirements.txt文件
import os
import sys

from source.moudleDemo.myTool.filemanager.file_manager import FileManage

ROOTDIR = os.path.abspath(os.path.join(__file__, '../../../../'))


def _get_win_pip():
    """获取当前windows中安装的三方模块"""

    tmp_file = 'tmp.txt'
    cmd = 'pip freeze > %s' % tmp_file
    os.system(cmd)

    with open(tmp_file) as ff:
        context = ff.readlines()

    os.remove(tmp_file)

    return context


def _find_all_import():
    """找出项目中所有的import语句"""

    fm = FileManage(ROOTDIR)
    flist = fm.get_files_by_name('.*\.py$')
    import_list = []
    try:
        for fname in flist:
            with open(fname, 'rb') as ff:
                line = ff.readline().strip().decode('utf-8')
                if 'import ' in line or 'from ' in line:
                    if line not in import_list:
                        import_list.append(line)
    except UnicodeDecodeError:
        raise
    # print(import_list)
    return import_list


def _deal_import_sentence(import_list):
    """检测import语句中的模块名 不支持,分隔"""

    module_list = []
    for im in import_list:
        parts = im.split(' ')
        if '.' in parts[1]:
            module_list.append(parts[1].split('.')[0].lower())
        else:
            module_list.append(parts[1].lower())

    print(module_list)
    return module_list


def _generate_txt(dev_env, project_mod, rms_path):
    """
    生成要更新的模块txt,并更新

    :param dev_env: 开发环境中已安装的全部包
    :param project: 项目中检测到的全部包
    :rtype: list
    """
    res, rms = [], []
    with open(rms_path, 'rb') as ff:
        for line in ff:
            rms.append(line.decode('utf-8').split('=')[0].lower())

    for mod in dev_env:
        mod_name = mod.split('=')[0].lower()
        if mod_name in project_mod:
            if mod_name not in rms:
                res.append(mod)

    with open(rms_path, 'a') as ff_a:
        ff_a.writelines(res)

    print('requirements.txt update success...')
    return res


def update_requirements():
    """根据本机模块更新项目中的requirements.txt文件"""

    rms_path = os.path.join(ROOTDIR, 'requirements.txt')

    import_list = _find_all_import()
    pro_mod = _deal_import_sentence(import_list)
    standard_module = _get_win_pip()
    _generate_txt(standard_module, pro_mod, rms_path)


if __name__ == '__main__':
    # _get_win_pip()
    print(ROOTDIR)
    update_requirements()
