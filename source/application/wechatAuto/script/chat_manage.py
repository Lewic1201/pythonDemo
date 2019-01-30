import re
import time
import wxpy
from wxpy import Bot
from wxpy import embed
from wxpy import Group, TEXT
from source.utils.decorators import print_def


class ChatManage:
    def __init__(self):
        # 登录缓存
        self.bot = Bot(cache_path=True)

    def send_msg_self(self):
        # 给机器人自己发送消息
        self.bot.self.send('Hello World!')
        # 给文件传输助手发送消息
        self.bot.file_helper.send('Hello World!')

    def get_friends(self, name=None):
        """获取通讯录对象"""
        if not name:
            return self.bot.friends()
        return self.bot.friends().search(name)

    @print_def
    def get_friend_info(self, friends=None):
        """
        获取朋友详细信息
        :param friends:
        :return:
        """
        if not friends:
            friends = self.get_friends()
        friends_info = []
        for friend in friends:
            data = [
                friend.name,
                # friend.nick_name,
                # friend.sex,
                friend.signature,
                # friend.city,
            ]
            friends_info.append(data)
        return friends_info

    def get_groups(self, name=None):
        """获取所有群"""
        if not name:
            return self.bot.groups()
        return self.bot.groups.search(name)

    @print_def
    def get_group_info(self, groups=None):
        """
        获取群详细信息
        :param groups:
        :return:
        """
        if not groups:
            groups = self.get_groups()
        groups_info = []
        for group in groups:
            data = [
                group.name,
                group.owner.nick_name,
                [people.name for people in group.members],
            ]
            groups_info.append(data)
        return groups_info

    def get_mps(self, name=None):
        """获取公众号对象"""
        if not name:
            return self.bot.mps()
        return self.bot.mps().search(name)

    def get_mps_info(self, mps=None):
        pass


if __name__ == '__main__':
    cm = ChatManage()
    # friend_list = cm.get_friends()
    infos = cm.get_friend_info()
    # gro = cm.get_group_info()
    # mps = cm.get_mps()
    # 堵塞线程 进入Python 命令行 让程序保持运行
    embed()
