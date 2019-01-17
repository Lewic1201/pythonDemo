"""
统计代码行数
"""
import os




def get_files():
    files_path = []
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            files_path.append(i)
    return files_path


def count(files):
    line_of_code, blank, comments = 0, 0, 0
    for filename in files:
        f = open(filename, 'rb')
        for line in f:
            line = line.strip()
            line_of_code += 1
            if line == '':
                blank += 1
            elif line[0] == '#' or line[0] == '/':
                comments += 1
        f.close()
    return (line_of_code, blank, comments)


if __name__ == '__main__':
    files = get_files()
    print(files)

    lines = count(files)
    print('Line(s):%d,black line(s):%d,comments line(s):%d' % (lines[0], lines[1], lines[2]))
