"""
    使用 logging 模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：
    logger提供了应用程序可以直接使用的接口；
    handler将(logger创建的)日志记录发送到合适的目的输出；
    filter提供了细度设备来决定输出哪条日志记录；
    formatter决定日志记录的最终输出格式。
"""
import logging
import time
import os

LOG_PATH = os.path.abspath(os.path.join(__file__, '..\\..\\logs'))


def get_log(logger_name):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 设置日志存放路径，日志文件名
    # 获取本地时间，转换为设置的格式
    # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    rq = time.strftime('%Y_%m_%d_', time.localtime(time.time()))
    # 设置所有日志和错误日志的存放路径
    path = LOG_PATH
    # 拼接日志存放路径
    all_log_path = os.path.join(path, 'all_Logs\\')
    error_log_path = os.path.join(path, 'error_Logs\\')
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)
    if not os.path.exists(error_log_path):
        os.makedirs(error_log_path)
    # 设置日志文件名
    all_log_name = all_log_path + rq + '.log'
    error_log_name = error_log_path + rq + '.log'

    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    # 创建一个handler写入错误日志
    eh = logging.FileHandler(error_log_name)
    eh.setLevel(logging.ERROR)
    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 创建一个handler输出到控制台
    de = logging.StreamHandler()
    de.setLevel(logging.DEBUG)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
    # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
    error_log_formatter = logging.Formatter(
        '[%(asctime)s - %(name)s - %(levelname)s] %(module)s  - %(lineno)s - %(message)s')
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)
    de.setFormatter(all_log_formatter)
    eh.setFormatter(error_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(eh)
    logger.addHandler(ch)
    logger.addHandler(de)
    return logger


logger = get_log("pythonDemo")

# if __name__ == '__main__':
#     print(os.path.abspath(os.path.join(__file__, '..\\..\\logs')))
#     print(os.path.abspath('E:/lewic/pycharm/workspace/myCode/pythonDemo/source/utils/logs.py'))
#     a = 'D:\\abc\\asdf'
#     if not os.path.exists(a):
#         os.makedirs(a)
#     pass
