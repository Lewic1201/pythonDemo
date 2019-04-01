import pickle
import datetime
import os
import json

ID_CREATER = ('{:0>5}'.format(i) for i in range(99999))
DEFAULT_FILE = '.\\datas.pkl'


class WordManage:
    def __init__(self, file=DEFAULT_FILE):
        self.file = file
        """
        datas: [{
            wid:int,
            index:str,
            queue_num:index+str(wid),
            en:str,
            ch:str,
            time:str,
            translate_if:bool,
            spell_if:bool
        },...]
        """
        self.datas = self.get_data()

    def get_data(self):
        try:
            if not os.path.exists(self.file):
                return []
            with open(self.file, 'rb') as files:
                return pickle.load(files)
        except:
            return []

    def add_word(self, en_str, ch_str=''):
        """
        :param en_str:
        :param ch_str:
        :return:
        """
        # 生成一个id
        ids = [int(data['wid']) for data in self.datas]
        if not ids:
            wid = '00000'
        else:
            wid = '{:0>5}'.format(max(ids) + 1)

        if en_str is None or en_str.strip() is '':
            return False, "word must exist!"
        word = {
            'wid': wid,
            'index': en_str[0].lower(),
            'queue_num': en_str[0].lower() + str(wid),
            'en': en_str,
            'ch': ch_str,
            'translate_if': False,
            'spell_if': False,
            'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        self.datas.append(word)

    def delete_word(self, wid):
        """
        :param wid:
        :return:
        """
        for i in range(len(self.datas)):
            if self.datas[i]['wid'] == wid:
                self.datas.pop(i)
                break

    def save_data(self):
        with open(self.file, 'wb') as files:
            pickle.dump(self.datas, files)

    # 控制台调试用
    def get_console_data(self):
        return json.dumps(self.datas)

    def __str__(self):
        ret = ''
        for i in self.datas:
            ret += '{} {} {:<10} {}\n'.format(i.get('mid'), i.get('now_time'), i.get('username'), i.get('context'))
        return ret


if __name__ == '__main__':
    wm = WordManage()
