# coding: utf-8
# from ftplib import FTP
import ftplib
import socket
import os


def ftpconnect(ftp_info):
    try:
        ftp = ftplib.FTP(ftp_info[0])
    except (socket.error, socket.gaierror):
        print("ERROR: cannot reach %s" % ftp_info[0])
        return None

    username = ftp_info[1]
    passwd = ftp_info[2]
    try:
        ftp.login(username, passwd)
    except ftplib.error_perm:
        print("ERROR: cannot login anonymously")
        ftp.quit()
        return None
    return ftp


if __name__ == "__main__":
    info_list = ["10.19.3.199", "fastupdate_amap", "@utonavi&A.map"]
    ftp = ftpconnect(info_list)
    if not ftp:
        exit(1)
    bufsize = 1024
    fname = "20150416113942674.tar.gz"
    fp = open(os.path.join(".", fname), 'wb')
    remotefile = os.path.join("/ADF++", fname)
    ftp.retrbinary("RETR " + remotefile, fp.write, bufsize)

    # 是否有目录，没有就创建；有的话看是否有权限创建
    a = ftp.dir()
    try:
        ftp.cwd("jimi")
    except ftplib.error_perm:
        try:
            ftp.mkd("jimi")
        except ftplib.error_perm:
            print("WARNING: U have no authority to make dir")
    finally:
        ftp.quit()
