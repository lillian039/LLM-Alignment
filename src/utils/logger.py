import logging
import os
def get_logger(name):
    logger = logging.getLogger('my_logger')

    # 设置日志级别（例如：DEBUG、INFO、WARNING、ERROR、CRITICAL）
    logger.setLevel(logging.DEBUG)

    # 创建一个文件处理器，并设置日志级别和日志文件名
    os.makedirs('logs', exist_ok=True)
    file_handler = logging.FileHandler(f'logs/{name}.log')
    file_handler.setLevel(logging.DEBUG)

    # 创建一个格式化器，并定义日志输出的格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # 将处理器添加到 logger
    logger.addHandler(file_handler)
    return logger