import pickle
import datetime
import os
import json

ID_CREATER = ('{:0>5}'.format(i) for i in range(99999))


class MessageManage:
    def __init__(self, file='.\\datas'):
        self.file = file
        self.datas = self.get_data()

    def get_data(self):
        try:
            if not os.path.exists(self.file):
                return []
            with open(self.file, 'rb') as files:
                return pickle.load(files)
        except:
            return []

    def add_message(self, username, context):
        """
        新增一条留言
        :param username:
        :param context:
        :return:
        """
        # 生成一个id
        ids = [int(data['mid']) for data in self.datas]
        if not ids:
            mid = '00000'
        else:
            mid = '{:0>5}'.format(max(ids) + 1)

        if context is None or context.strip() is '':
            return False, "留言不能为空!"
        message = {
            'mid': mid,
            'now_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'username': username,
            'context': context
        }
        self.datas.append(message)

    def save_data(self):
        with open(self.file, 'wb') as files:
            pickle.dump(self.datas, files)

    def get_console_data(self):
        return json.dumps(self.datas)

    def __str__(self):
        ret = ''
        for i in self.datas:
            ret += '{} {} {:<10} {}\n'.format(i.get('mid'), i.get('now_time'), i.get('username'), i.get('context'))
        return ret


if __name__ == '__main__':
    mm = MessageManage()
    # mm.add_message('zhang3', 'hello')
    # mm.add_message('zhang34', 'hello')
    # mm.add_message('zhang3', 'h2ello')
    # mm.add_message('li4', 'h2el3lo')
    # mm.add_message('liss4', 'h2el3lo')
    # mm.save_data()
    # print(mm)
    print(mm.get_console_data())
