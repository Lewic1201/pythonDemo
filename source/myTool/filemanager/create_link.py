# # coding:gbk
# # GetLink.py
# # hbxcyz.cn
# import os
# import pythoncom
# from win32com.shell import shell
# from win32com.shell import shellcon
#
#
# # ��.lnk�ļ��л�ȡ�ļ�·��
#
# def GetpathFromLink(lnkpath):
#     shortcut = pythoncom.CoCreateInstance(
#         shell.CLSID_ShellLink, None,
#         pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
#     shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(lnkpath)
#     path = shortcut.GetPath(shell.SLGP_SHORTPATH)[0]
#     return path
#
#
# # ������ݷ�ʽ
#
# def CreateLnkpath(filename, lnkname):
#     shortcut = pythoncom.CoCreateInstance(
#         shell.CLSID_ShellLink, None,
#         pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
#     shortcut.SetPath(filename)
#     if os.path.splitext(lnkname)[-1] != '.lnk':
#         lnkname += ".lnk"
#     shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname, 0)
#
#
# # ����url��ݷ�ʽ
#
# def CreateURLShortcut(url, name):
#     shortcut = pythoncom.CoCreateInstance(
#         shell.CLSID_InternetShortcut, None,
#         pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IUniformResourceLocator)
#     shortcut.SetURL(url)
#     if os.path.splitext(name)[-1] != '.url':
#         name += '.url'
#     shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(name, 0)
#
#
# # ��.url��ݷ�ʽ��ȡurl���ӵ�ַ
# def GetURLFromShortcut(url):
#     shortcut = pythoncom.CoCreateInstance(
#         shell.CLSID_InternetShortcut, None,
#         pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IUniformResourceLocator)
#     shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(url)
#     url = shortcut.GetURL()
#     return url
#
#
# # ��ȡ����·��
#
# def GetDesktoppath():
#     ilist = shell.SHGetSpecialFolderLocation(0, shellcon.CSIDL_DESKTOP)
#     dtpath = shell.SHGetPathFromIDList(ilist)
#     # dtpath = dtpath.decode('gbk')
#     return dtpath


# -*-code: utf-8 -*-
import os
import winshell
import sys
import win32com.client


def main():
    destDir = winshell.desktop()
    filename = "myShortcut"
    target = r"C:\Python37"

    winshell.CreateShortcut(
        Path=os.path.join(destDir, os.path.basename(filename) + ".lnk"),
        Target=target,
        Icon=(target, 0),
        Description="shortcut test")


def create_lnk(target, lnkdir=None, filename=None, description="", is_desk=False):
    """
    ������ݷ�ʽ

    :param target: ָ��·��
    :param lnkdir: lnk����·�� Ĭ����targetͬĿ¼
    :param filename: ��ݷ�ʽ���� Ĭ��target
    :param description: ��ע
    :param is_desk: �Ƿ�Ϊ���������ݷ�ʽ
    :return:
    """
    try:
        if is_desk:
            # ������
            lnkdir = winshell.desktop()
        elif not lnkdir:
            # ��ǰ·��
            lnkdir = os.path.dirname(target)

        # Ĭ��ԭ�ļ���
        filename = filename if filename else os.path.basename(target)
        # �ļ�ȫ·��
        file_name = os.path.join(lnkdir, os.path.basename(filename) + ".lnk")

        winshell.CreateShortcut(
            Path=file_name,
            Target=target,
            Icon=(target, 0),
            # �ļ���ע
            Description=description)

        print('create lnk success, path: %s' % file_name)
    except Exception:
        raise


def get_lnk_info(lnk_name):
    shell = win32com.client.Dispatch("WScript.Shell")
    if os.path.isfile(lnk_name) and lnk_name[-4:] == '.lnk':
        shortcut = shell.CreateShortCut(lnk_name)
        target_path = shortcut.Targetpath
        print(target_path)
        return target_path
    else:
        print('lnk name error')
        return ''


if __name__ == "__main__":
    # main()
    file0 = r'C:\python37'
    file1 = r'E:\bak\�½��ı��ĵ�.txt'
    # create_lnk(r'C:\python37', is_desk=True)
    # create_lnk(file1, is_desk=True)
    # create_lnk(file1)
    # create_lnk(file1, 'E:\\', 'test', '213', True)
    # create_lnk(file1, 'E:\\', 'test', '213')

    get_lnk_info('E:\\test.lnk')
