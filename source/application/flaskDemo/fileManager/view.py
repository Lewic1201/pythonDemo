import pickle
import datetime
import os
import json
from utils import FileManage
from source.utils.logs import logger


class FileService:
    """将后台数据处理成前台所需要的数据样式"""

    def get_filelist(self, request):
        """获取当前文件夹文件"""
        dir0 = r'E:\lewic\pycharm\workspace\webDemo\DjangoDemo'
        if 'currentDir' in request:
            dir0 = request['currentDir']
            if 'dirName' in request:
                name = request['dirName']
                dir0 = os.path.join(dir0, name)

        fm = FileManage(dir0)
        fmls = fm.get_current_dir_filename()
        data = {
            'device': '8C:DC:D4:25:8F:4C',
            'rootDir': os.path.abspath(dir0),
            'tableHead': ['name', 'type', 'size', 'time', 'deal'],
            'tableFile': fmls,
        }
        logger.info("data: " + str(data))
        return data

    def managedir(self):
        return


if __name__ == '__main__':
    mm = FileService()
    test = mm.get_filelist('')
    import pprint
    pprint.pprint(test)
