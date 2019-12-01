import os
import re


def print_repair(filename, bak=True):
    """
    修复py文件中的print语句


    :param filename: 文件全路径
    :param bak: 是否备份
    :return:
    """
    if filename[-3:] != '.py':
        return False

    try:
        # 忽略其它编码字符
        # with open(filename, 'r', errors='ignore') as ff:
        with open(filename, 'r') as ff:
            context = ff.readlines()
        context_bak = context[:]

    except UnicodeDecodeError as err:
        print(filename, err)
        return False
    except Exception:
        raise

    # 替换
    change_count = 0

    pattern = re.compile(rb'^(\s*)print +(.*)$')
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
    print_repair(filename)

    # rootDir = os.path.abspath(os.path.join(__file__, '../../../../../'))
    # fm = FileManage(rootDir)
    # flist = fm.get_files_by_name(r'.*\.py')
    # for i in flist:
    #     print_repair(i)
