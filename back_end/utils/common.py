import json
import logging
import os
import sys
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL


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


def auto_mail_sending(mail_content, from_addr='2298276317@qq.com',
                      to_addr='1475109413@qq.com'):
    host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
    sender_qq = from_addr  # 发件人邮箱
    # pwd = password
    # 获取环境变量EMAIL_PWD作为密码
    pwd = os.environ.get("EMAIL_PWD")
    receiver = [to_addr]  # 收件人邮箱

    mail_title = '自动任务'  # 邮件标题
    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    msg['To'] = ";".join(receiver)
    # 邮件正文内容
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    smtp = SMTP_SSL(host_server)  # ssl登录

    # login(user,password):
    # user:登录邮箱的用户名。
    # password：登录邮箱的密码，像笔者用的是网易邮箱，网易邮箱一般是网页版，需要用到客户端密码，需要在网页版的网易邮箱中设置授权码，该授权码即为客户端密码。
    smtp.login(sender_qq, pwd)

    smtp.sendmail(sender_qq, receiver, msg.as_string())

    # quit():用于结束SMTP会话。
    smtp.quit()


if __name__ == "__main__":
    print("这是common.py")
    # email_password = os.environ.get("email_password")
    # print(email_password)
    # auto_mail_sending("测试")
