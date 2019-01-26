"""
统计代码行数
"""
import datetime
import os
import pprint
from source.moudleDemo.myTool.get_all_file_by_path import *

ROOT_DIR = os.path.abspath(os.path.join(__file__, '..\\..\\..\\..\\..\\'))
# 获取的文件列表, 可追加
FILE_TYPE = ['.py']


def get_py_files(rootDir):
    """获取python文件列表"""
    all_file = get_all_filelist(rootDir)
    files_path = []
    for i in all_file:
        # 过滤出所有py文件
        if os.path.splitext(i)[1] in FILE_TYPE:
            files_path.append(i)
    return files_path


def countpy(files):
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
        raise


# def countall(files):
#     return countpy(files)[0], 0, 0


def record(lines, file='linenum.log'):
    """追加记录日志"""
    now = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    data = '\n{}type:{:<20} line(s):{:<8} black line(s):{:<8} comments line(s):{:<8}' \
        .format(now, str(FILE_TYPE), lines[0], lines[1], lines[2])
    with open(file, 'a') as ff:
        ff.write(data)
    print(data)


if __name__ == '__main__':
    files = get_py_files(ROOT_DIR)
    # pprint.pprint(files)
    lines = countpy(files)
    record(lines)
