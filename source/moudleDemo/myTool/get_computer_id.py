"""
@summary 获取电脑的mac地址
@summary: return the MAC address of the computer
"""
import uuid
from source.utils.decorators import prints


@prints
def get_mac_address():
    """通用方法,借助uuid模块"""
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac


def get_mac_address_by_cmd():
    """按照操作系统平台来"""
    import sys
    import os
    mac = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            print(line)
            if line.lstrip().startswith("Physical Address"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if 'Ether' in line:
                mac = line.split()[4]
                break
    return mac


if __name__ == '__main__':
    # 优先使用
    get_mac_address()
    get_mac_address_by_cmd()
