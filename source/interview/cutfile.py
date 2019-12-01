import threading
import time
import os
import shutil

FILE_NAME = r'E:\tmp1.xls'
FILE_NAME2 = r'E:\tmp2.xls'

with open(FILE_NAME, 'rb') as ff:
    datas = ff.readlines()
    # print(data)

# for i in datas:
#     print(i)


# 删除文件,直到其它程序不再占用此文件
while True:
    try:
        if not os.path.exists(FILE_NAME):
            break
        os.remove(FILE_NAME)
    except PermissionError:
        print('另一个程序正在使用此文件，进程无法访问，请关闭。')
        time.sleep(2)

with open(FILE_NAME2, 'wb') as ff:
    ff.writelines(datas)

print("OVER")
