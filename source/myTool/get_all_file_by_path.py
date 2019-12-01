import os
from source.utils.decorators import *


# @print_def
def get_dir_structure(rootdir):
    """
    获取当前目录文件结构
    :param rootdir: 根目录
    :return: 每个文件夹下的文件
    :rtype: [(文件夹路径,路径下的文件夹,路径下的文件),...]
    """
    ret = []
    if not rootdir or not os.path.exists(rootdir):
        return []
    for i in os.walk(rootdir):
        ret.append(i)
    return ret


# @print_def
def get_all_filelist(rootdir):
    """
    获取当前目录下所有文件路径
    :param rootdir: 根目录
    :return: 路径列表
    :rtype: list
    """
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

    return list_all_files(rootdir)


if __name__ == '__main__':
    import pprint

    test = os.getcwd() + '\\swagger'
    # pprint.pprint(get_dir_structure(test))
    # pprint.pprint(get_all_by_listdir(test))
    # pprint.pprint(list_all_files(test))
