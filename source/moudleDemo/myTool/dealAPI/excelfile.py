import time
from source.moudleDemo.myTool.filemanager.excel_manage import *

file1 = r'D:\task\20190312 整理项目中openstack的api文档\项目中openstack的api补充文档.xlsx'
# sheet1 = 'all'
sheet1 = 'bak3'
data = get_excel_data(file1, sheet1)

try:
    for row in data[sheet1]:
        if row[2] and ('{' + row[2] + '}') not in row[1]:
            if '%s' in row[1]:
                row[1] = row[1].replace('%s', '{'+row[2]+'}')
            elif row[1][-1] == '/':
                row[1] = row[1] + '{' + row[2] + '}'
            else:
                row[1] = row[1] + '/{' + row[2] + '}'
        if row[1][-1] == '/':
            row[1] = row[1][:-1]
except:
    raise

now = time.time()
save_info(file1, str(now), data[sheet1])

if __name__ == '__main__':
    file1 = r'D:\task\20190312 整理项目中openstack的api文档\项目中openstack的api补充文档.xlsx'
