import os
import re

from source.moudleDemo.myTool.filemanager.file_manager import FileManage


def print_repair(filename, bak=True):
    """
    修复py文件中的print语句


    :param filename: 文件全路径
    :param bak: 是否备份
    :return:
    """

    with open(filename, 'r') as ff:
        context = ff.readlines()
    context_bak = context[:]

    # 替换
    change_count = 0

    pattern = re.compile(r'^(\s*)print +(.*)$')
    for i in range(len(context)):
        line = context[i]
        res = re.match(pattern, line)
        if res:
            group1 = res.group(2)
            line = re.sub(r'print +', 'print(', line, 1)
            context[i] = line.replace(group1, group1 + ')')
            change_count += 1

    # 文件如果需要被修改
    if change_count > 0:
        # 创建备份文件
        if bak:
            creater = (i for i in range(100))
            suffix = '.bak'
            while True:
                if not os.path.exists(filename + suffix):
                    new_name = filename + suffix
                    with open(new_name, 'w') as ff2:
                        ff2.writelines(context_bak)
                    break
                else:
                    suffix = '.bak' + str(next(creater))

        with open(filename, 'w') as ff3:
            ff3.writelines(context)
        print('change success, file(%s) change %s line' % (filename, change_count))
        return True

    return False


if __name__ == '__main__':
    filename = __file__ + '/../test.py'
    # print_replace(filename)

    rootDir = os.path.abspath(os.path.join(__file__, '../../../../../'))
    fm = FileManage(rootDir)
    for i in fm.get_all_filelist():
        print_repair(filename)
