"""
@summary 获取电脑的mac地址
@summary: return the MAC address of the computer
"""
import socket
import uuid
from source.utils.decorators import prints


@prints
def get_hostname():
    return socket.gethostname()


@prints
def get_ip():
    return socket.gethostbyname(socket.gethostname())


@prints
def get_mac_address_by_uuid():
    """该方法获取的可能是其它网卡的mac地址"""
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


@prints
def get_mac_address():
    """按照操作系统平台来"""
    import sys
    import os
    mac = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            # print(line)
            if line.lstrip().startswith("Physical Address"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
            elif line.lstrip().startswith("物理地址"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if 'Ether' in line:
                mac = line.split()[4]
                break
    return mac


if __name__ == '__main__':
    get_hostname()
    get_ip()
    get_mac_address()
    # 优先
    get_mac_address_by_uuid()
