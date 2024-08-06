import json
import logging
import sys


def read_json(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_os_type():
    os_type = None
    if sys.platform.startswith('linux'):
        os_type = "Linux"
        logging.info("当前系统为 Linux")
    elif sys.platform.startswith('win'):
        os_type = "Windows"
        logging.info("当前系统为 Windows")
    else:
        logging.info("当前系统为{}".format(sys.platform))
    return os_type


def get_python_command():
    python_command = None
    os_type = get_os_type()
    if os_type == "Linux":
        python_command = "python3"
    elif os_type == "Windows":
        python_command = "python"
    else:
        logging.info("不支持{}系统".format(sys.platform))
    return python_command


if __name__ == "__main__":
    print("这是common.py")
