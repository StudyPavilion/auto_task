import os
from datetime import timedelta

from apscheduler.triggers.cron import CronTrigger
from flask import Flask, request, session
from flask_session import Session
from flask_cors import CORS
import json
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from redis import Redis

from mysql_config import mysql_init, mysql_config, connect_mysql, disconnect_mysql, find_user_info, \
    add_users
from utils.common import read_json, get_python_command, generate_random_number, auto_mail_sending
from task.quark_task import quark_auto_task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'StudyPavilion'
# SESSION_TYPE = 'redis'
# SESSION_REDIS = Redis(host='localhost', port=6379)
# app.config.from_object(__name__)
# Session(app)
# 解决跨域问题

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 配置7天有效
CORS(app, supports_credentials=True)

quark_config = "task_config/quark_config.json"
test_config = "task_config/test_config.json"

test_task = "task/test_task.py"
quark_task = "task/quark_task.py"

mysql_config_data = read_json(mysql_config)
connect_config = mysql_config_data.get("connect_config")

scheduler = BackgroundScheduler()

DEBUG = True

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="[%(asctime)s][%(levelname)s] %(message)s",
    datefmt="%m-%d %H:%M:%S",
)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return "不支持GET请求，请使用POST进行请求"
    elif request.method == 'POST':
        login_result = {"login_result": "", "log": ""}
        json_data = request.get_json()
        user_name = json_data.get('account')
        password = json_data.get('password')
        logging.info("user_name:{}, password:{}".format(user_name, password))

        cnx = connect_mysql(connect_config)
        user_info = find_user_info(cnx, user_name, field='password')
        logging.info("user_info:{}".format(user_info))
        if user_info:
            db_password = user_info[0]
            if password == db_password:
                login_result["login_result"] = "success"
                login_result["log"] = "登录成功"
            else:
                login_result["login_result"] = "error"
                login_result["log"] = "密码错误"
        else:
            login_result["login_result"] = "error"
            login_result["log"] = "用户不存在"
        disconnect_mysql(cnx)
        return login_result
    else:
        return "未知请求，请使用POST进行请求"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return "不支持GET请求，请使用POST进行请求"
    elif request.method == 'POST':
        session_id = request.cookies.get(app.config['SESSION_COOKIE_NAME'])
        print('register Session ID:', session_id)
        user_list = []
        login_result = {"register_result": "", "log": ""}
        json_data = request.get_json()
        json_data["vip"] = 0
        user_list.append(json_data)
        logging.info("user_list:{}".format(user_list))
        user_name = json_data.get('user_name')
        password = json_data.get('password')
        email = json_data.get('email')
        code = json_data.get('code')
        logging.info('code:{}, session[email]: {}'.format(code, session.get('email')))
        logging.info("session['email']: {}".format(session.get('email')))
        logging.info("type(code):{}, type(session.get('email')):{}".format(type(code), type(session.get('email'))))
        if code != session.get('email'):
            login_result["register_result"] = "error"
            login_result["log"] = "验证码错误"
            return login_result
        logging.info("user_name:{}, password:{}, email:{}".format(user_name, password, email))

        cnx = connect_mysql(connect_config)
        user_info = find_user_info(cnx, user_name, field='user_name')
        logging.info("user_info:{}".format(user_info))
        if user_info:
            login_result["register_result"] = "error"
            login_result["log"] = "该用户已被注册，请登录"
        else:
            logging.info("正在创建用户：{}".format(user_name))
            if add_users(cnx, user_list):
                login_result["register_result"] = "success"
                login_result["log"] = "注册成功"
            else:
                login_result["register_result"] = "error"
                login_result["log"] = "注册失败"
        disconnect_mysql(cnx)
        return login_result
    else:
        return "未知请求，请使用POST进行请求"


@app.route('/get_code', methods=['GET', 'POST'])
def get_code():
    if request.method == 'GET':
        email = request.args.get("email")
        logging.info("email:{}".format(email))
        get_code_result = {"get_code_result": "", "log": ""}
        code = generate_random_number(6)
        session['email'] = str(code)
        session_id = request.cookies.get(app.config['SESSION_COOKIE_NAME'])
        print('get_code Session ID:', session_id)
        logging.info("session['email']: {}".format(session.get('email')))
        mail_content = "您的验证码是：{}, \n 五分钟内有效".format(code)
        if auto_mail_sending(mail_content, to_addr=email):
            get_code_result["get_code_result"] = "success"
            get_code_result["log"] = "验证码发送成功"
        else:
            get_code_result["get_code_result"] = "error"
            get_code_result["log"] = "验证码发送失败"
        return get_code_result
    elif request.method == 'POST':
        return "不支持POST请求，请使用GET进行请求"
    else:
        return "请使用GET进行请求"


@app.route('/read_config/', methods=['GET', 'POST'])
def read_config():
    # read_config_result = {}
    if request.method == 'GET':
        software = request.args.get("software")
        print(software)
        if software == "quark":
            data = read_json(quark_config)
            user_list = data["userList"]
            print(data)
            return json.dumps(data)
        elif software == "test":
            data = read_json(test_config)
            user_list = data["userList"]
            return json.dumps(data)

        else:
            print("没有{}的配置文件".format(software))
            return "没有{}的配置文件".format(software)
    elif request.method == 'POST':
        return "不支持POST请求，请使用GET进行请求"
    else:
        return "请使用GET进行请求"


@app.route('/save_config', methods=['GET', 'POST'])
def save_config():
    print(request.method)
    json_data = request.get_json()
    print(json_data)
    software = json_data['software']
    print(software)
    if request.method == 'POST':
        save_config_result = {"task_result": "", "log": ""}
        if software == "quark":
            crontab = json_data["crontab"]
            trigger = CronTrigger.from_crontab(crontab)
            # 先暂停任务，再恢复任务
            scheduler.pause_job('quark')
            scheduler.modify_job('quark', trigger=trigger)
            scheduler.resume_job('quark')
            # 写入配置
            with open(quark_config, "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False, sort_keys=False)
            save_config_result["task_result"] = "success"
            save_config_result["log"] = "保存成功"

        elif software == "test":
            with open(test_config, "w", encoding="utf-8") as f:
                # json.dump(json_data, f)
                json.dump(json_data, f, indent=4, ensure_ascii=False, sort_keys=False)
            save_config_result["task_result"] = "success"
            save_config_result["log"] = "保存成功"
        else:
            print("没有{}的配置文件".format(software))
            save_config_result["task_result"] = "error"
            save_config_result["log"] = "保存失败"
        print("save_config_result: {}".format(save_config_result))
        return save_config_result
    elif request.method == 'GET':
        return "不支持GET请求，请使用POST进行请求"
    else:
        return "未知请求，请使用POST进行请求"


@app.route('/run_task', methods=['GET', 'POST'])
def run_task():  # put application's code here
    print(request.method)
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        summary_message = quark_auto_task(json_data)
        return summary_message
    elif request.method == 'GET':
        return "不支持GET请求，请使用POST进行请求"


def run_python(args):
    logging.info(f">>> 定时运行任务")
    os.system(f"{get_python_command()} {args}")


def reload_tasks(software):
    """
    重载任务调度器
    :return:
    """
    if software == "quark":
        data = read_json(quark_config)
        # 尝试从数据中获取名为"crontab"的键对应的值
        crontab = data.get("crontab")
    else:
        logging.info("不支持{}配置定时任务".format(software))
        return False
    # 如果成功获取到crontab，则继续执行
    if crontab:
        # data = read_json(quark_config)
        account_list = data["userList"]
        # 如果调度器当前处于运行状态，则先暂停调度器
        if scheduler.state == 1:
            scheduler.pause()  # 暂停调度器
        # 根据crontab创建一个触发器
        trigger = CronTrigger.from_crontab(crontab)
        # 移除调度器中的所有现有任务
        scheduler.remove_all_jobs()
        # 添加新的任务到调度器
        scheduler.add_job(
            # 指定要执行的函数
            quark_auto_task,
            # 使用上面创建的触发器
            trigger=trigger,
            # 指定传递给函数的参数
            args=[account_list],
            id="quark",  # 为任务指定一个唯一标识符
        )
        # 根据调度器的当前状态决定是否重新启动或恢复调度器
        if scheduler.state == 0:
            scheduler.start()
        elif scheduler.state == 2:
            scheduler.resume()
        # 定义一个映射，将调度器的状态代码转换为可读的状态描述
        scheduler_state_map = {0: "停止", 1: "运行", 2: "暂停"}
        # 记录日志信息，包括调度器的状态、定时规则和现有任务
        logging.info(">>> 重载调度器")
        logging.info(f"调度状态: {scheduler_state_map[scheduler.state]}")
        logging.info(f"定时规则: {crontab}")
        logging.info(f"现有任务: {scheduler.get_jobs()}")
        return True
    else:
        # 如果没有获取到crontab，记录日志信息并返回False
        logging.info(">>> 没有配置定时任务")
        return False


def main():
    mysql_init()
    reload_tasks("quark")
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)


if __name__ == "__main__":
    main()
