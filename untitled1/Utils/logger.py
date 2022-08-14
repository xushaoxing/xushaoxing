import logging
from Common.config_manage import ConfigManager
class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            # 写入文件
            fh = logging.FileHandler(ConfigManager().log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            sh.setFormatter(formatter)

            # 添加到handler
            self.logger.addHandler(fh)
            self.logger.addHandler(sh)
    @property
    def fmt(self):
        return '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        # return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

log = Log().logger
if __name__ == '__main__':

    log.info('hello world')
