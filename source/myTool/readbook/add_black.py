import re
import random


def add_black(filename, savefile):
    """随机给文本添加回车"""
    with open(filename, 'rb') as ff:
        contexts = []
        context = ff.readline().decode('utf-8')
        while context:
            tmp_len = random.randint(20, 60)

            while len(context) > tmp_len:
                contexts.append(context[:tmp_len])
                contexts.append('\r' * random.randint(1, 3))
                context = context[tmp_len:]
                tmp_len = random.randint(20, 60)
            else:
                contexts.append(context)
            context = ff.readline().decode('utf-8')
    with open(savefile, 'w', encoding='utf-8') as ff2:
        ff2.writelines(contexts)


def add_black_in_pause(filename, savefile):
    """按逗号句号文本添加回车"""
    with open(filename, 'rb') as ff:
        contexts = ff.read().decode('utf-8')
        res_str = ''
        black_num = 0
        for i in range(len(contexts)):
            if contexts[i] in ['\r', '\n']:
                black_num += 1
                continue
            res_str += black_num * '\n'
            res_str += contexts[i]
            if contexts[i] in [',', '，']:
                res_str += '\r'
            if contexts[i] in ['.', '。']:
                res_str += '\r\n'
            black_num = 0

    with open(savefile, 'w', encoding='utf-8') as ff2:
        ff2.writelines(res_str)


if __name__ == '__main__':
    file0 = r'C:\Users\li_panfeng\Desktop\171490.txt'
    save0 = r'C:\Users\li_panfeng\Desktop\lczd.txt'
    # add_black(file0, save0)
    add_black_in_pause(file0, save0)
