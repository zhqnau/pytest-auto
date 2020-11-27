import logging
import time
import threading
from utils.dir_config import *

'''
日志模块
'''


class MyLogger:

    def __init__(self):
        """将日志保存到指定的路径文件中；指定日志的级别，调用文件"""
        self.logger = logging.getLogger()  # 创建logger文件
        self.logger.setLevel(logging.DEBUG)

        now = time.strftime("%Y-%m-%d-%H_%M_%S")  # 创建日志文件名称
        # root_path = os.path.dirname(os.path.dirname(__file__))
        # log_path = os.path.join(root_path, "report/logs/")
        log_path1 = os.path.normpath(logs_dir)
        print(log_path1)
        log_name = now+".log"
        print(log_name)
        filehandle = logging.FileHandler(os.path.join(log_path1, log_name), encoding="utf-8")
        print(filehandle)
        filehandle.setLevel(logging.INFO)

        # 创建一个handle，用来输入日志到控制台
        controlhandle = logging.StreamHandler()
        controlhandle.setLevel(logging.INFO)

        # 将输出的handle格式转换
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        filehandle.setFormatter(formatter)
        controlhandle.setFormatter(formatter)

        self.logger.addHandler(filehandle)  # 给logger添加handle
        self.logger.addHandler(controlhandle)

    def get_log(self):
        return self.logger


class Logger:
    log = None
    lock = threading.Lock()  # 创建锁

    @staticmethod
    def get_logger():

        if Logger.log is None:
            Logger.lock.acquire()  # 锁定
            try:
                Logger.log = MyLogger().logger
            finally:
                Logger.lock.release()  # 释放
        return Logger.log


log = Logger.get_logger()


if __name__ == "__main__":
    logger = Logger.get_logger()
    logger.info("...")
    logger.info("这是一个日志记录")


