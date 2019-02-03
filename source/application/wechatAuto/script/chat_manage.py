import re
import time
import wxpy
from wxpy import Bot
from wxpy import embed
from wxpy import Group, TEXT, FRIENDS
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
        """
        获取通讯录对象
        :param name: 昵称
        :return: 好友对象列表
        :rtype: list
        """
        if not name:
            return self.bot.friends()
        return self.bot.friends().search(name)

    @print_def
    def get_friend_info(self, friends=None):
        """
        获取朋友详细信息
        :param friends:
        :return: [[姓名,昵称,性别,个性签名,城市]]
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

    @print_def
    def get_friend_nums(self):
        """返回好友总数"""
        return len(self.get_friends())

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

    # @print_def
    def get_mps_info(self, mps_list=None):
        """
        获取公众号基本信息
        :param mps_list:
        :return: [[名称,昵称,地点,签名]]
        """
        if not mps_list:
            mps_list = self.get_mps()
        mps_info = []
        for mps in mps_list:
            data = [
                mps.name,
                mps.nick_name,
                mps.raw['Province'] + '-' + mps.raw['City'],
                mps.signature,
            ]
            mps_info.append(data)
        return mps_info

    def get_mps_nums(self):
        """获取公众号数量"""
        return len(self.get_mps())

    def send_div(self, friend, msg, sign='text'):
        """
        发送消息体
        :param friend:
        :param msg:
        :param sign:
        :return:
        """
        if sign == 'text':
            friend.send(msg)
        elif sign == 'img':
            # 发送图片 path 'my_picture.png'
            friend.send_image(msg)
        elif sign == 'video':
            # 发送视频 path 'my_video.mov'
            friend.send_video()
        elif sign == 'file':
            # 发送文件 path 'my_file.zip'
            friend.send_file()
        else:
            # 以动态的方式发送图片 '@img@my_picture.png'
            friend.send(msg)

    def get_now_msg(self):
        """
        获取实时消息
        :return:
        """

        @self.bot.register()
        def print_others(msg):
            print(msg)

    def reply_msg(self, friend):
        """
        自动回复
        :param friend: 好友对象
        :return:
        """

        # 回复 friend 的消息 (优先匹配后注册的函数!)
        @self.bot.register(friend)
        def reply_my_friend(msg):
            return 'received: {} ({})'.format(msg.text, msg.type)

    # 自动接受新的好友请求
    def auto_accept(self):
        @self.bot.register(msg_types=FRIENDS)
        def auto_accept_friends(msg):
            # 接受好友请求
            new_friend = msg.card.accept()
            # 向新的好友发送消息
            new_friend.send('哈哈，我接受了你的好友请求')


if __name__ == '__main__':
    cm = ChatManage()
    # friend_list = cm.get_friends()
    # infos = cm.get_friend_info()
    # gro = cm.get_group_info()
    # mps = cm.get_mps()
    # cm.get_friend_nums()

    # mps_info = cm.get_mps_info()
    # for i in mps_info:
    #     if '陕西' in i[2]:
    #         print(i)

    print(cm.get_now_msg())

    # 堵塞线程 进入Python 命令行 让程序保持运行
    embed()
