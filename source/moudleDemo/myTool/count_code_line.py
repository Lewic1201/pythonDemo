"""
统计代码行数
"""
import os
from source.moudleDemo.myTool.get_all_file_by_path import *


def get_py_files(rootDir):
    """获取python文件列表"""
    all_file = get_all_filelist(rootDir)
    files_path = []
    for i in all_file:
        if os.path.splitext(i)[1] == '.py':
            files_path.append(i)
    return files_path


def count(files):
    """
    统计文件代码行数
    :param files: 文件绝对路径列表
    :return: (代码行数,空行数,注释行数)
    """
    try:
        line_of_code, blank, comments = 0, 0, 0
        for filename in files:
            with open(filename, 'rb') as f:
                for a_line in f:
                    line = a_line.decode('utf-8').strip()
                    line_of_code += 1
                    if line == '':
                        blank += 1
                    elif line[0] in ['#', '/', "'", '"']:
                        comments += 1
        return (line_of_code, blank, comments)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    rootDir = 'E:\\lewic\\pycharm\\workspace\\myCode\\pythonDemo\\'
    files = get_py_files(rootDir)
    import pprint

    pprint.pprint(files)

    lines = count(files)
    print('Line(s):%d,black line(s):%d,comments line(s):%d' % (lines[0], lines[1], lines[2]))
