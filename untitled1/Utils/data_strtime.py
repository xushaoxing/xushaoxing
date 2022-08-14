import datetime

def dt_strftime(fmt="%Y%m%d"):
    """
    格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


if __name__ == '__main__':
    print(dt_strftime("%Y%m%d%H%M%S"))
