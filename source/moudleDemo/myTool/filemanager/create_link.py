# # coding:gbk
# # GetLink.py
# # hbxcyz.cn
# import os
# import pythoncom
# from win32com.shell import shell
# from win32com.shell import shellcon
#
#
# # 从.lnk文件中获取文件路径
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
# # 创建快捷方式
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
# # 创建url快捷方式
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
# # 从.url快捷方式获取url连接地址
# def GetURLFromShortcut(url):
#     shortcut = pythoncom.CoCreateInstance(
#         shell.CLSID_InternetShortcut, None,
#         pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IUniformResourceLocator)
#     shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(url)
#     url = shortcut.GetURL()
#     return url
#
#
# # 获取桌面路径
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
    创建快捷方式

    :param target: 指向路径
    :param lnkdir: lnk保存路径 默认与target同目录
    :param filename: 快捷方式名称 默认target
    :param description: 备注
    :param is_desk: 是否为创建桌面快捷方式
    :return:
    """
    try:
        if is_desk:
            # 桌面快捷
            lnkdir = winshell.desktop()
        elif not lnkdir:
            # 当前路径
            lnkdir = os.path.dirname(target)

        # 默认原文件名
        filename = filename if filename else os.path.basename(target)
        # 文件全路径
        file_name = os.path.join(lnkdir, os.path.basename(filename) + ".lnk")

        winshell.CreateShortcut(
            Path=file_name,
            Target=target,
            Icon=(target, 0),
            # 文件备注
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
    file1 = r'E:\bak\新建文本文档.txt'
    # create_lnk(r'C:\python37', is_desk=True)
    # create_lnk(file1, is_desk=True)
    # create_lnk(file1)
    # create_lnk(file1, 'E:\\', 'test', '213', True)
    # create_lnk(file1, 'E:\\', 'test', '213')

    get_lnk_info('E:\\test.lnk')
