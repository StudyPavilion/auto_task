from flask import Flask, request
from flask_cors import CORS
import time
import requests
import json

app = Flask(__name__)
# 解决跨域问题
CORS(app)

quark_config_file_path = "task_config/quark_config.json"


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/read_config/', methods=['GET', 'POST'])
def read_config():
    if request.method == 'GET':
        software = request.args.get("software")
        print(software)
        if software == "quark":
            data = read_json(quark_config_file_path)
            user_list = data["userList"]
            return json.dumps(user_list)
        else:
            print("没有{}的配置文件".format(software))
    elif request.method == 'POST':
        return "不支持POST请求，请使用GET进行请求"
    else:
        return "请使用GET进行请求"



@app.route('/run_task', methods=['GET', 'POST'])
def run_task():  # put application's code here
    print(request.method)
    # if request.method == 'POST' or request.method == 'GET':
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)

        kps = json_data['kps']
        sign = json_data['sign']
        vcode = json_data['vcode']

        print("kps:", kps, type(kps))
        account = kps + "&" + sign + "&" + vcode
        summary_message = quark_auto_task(account)
        return summary_message
    elif request.method == 'GET':
        return "GET"


def read_json(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_query(url):
    u = url.split("&")
    return f"__t={int(time.time() * 1000)}&sign_cyclic=true&fr=android&kps={u[0]}&sign={u[1]}&vcode={u[2]}&pr=ucpro&uc_param_str="


def check_request_response(response):
    """检查请求是否成功，并返回响应数据或打印错误信息"""
    if not response.ok:
        print(f"请求失败，状态码: {response.status_code}")
        return None
    return response.json()


def quark_sign_in(url):
    state_url = f"https://drive-m.quark.cn/1/clouddrive/capacity/growth/info?{get_query(url)}"

    # 获取签到状态
    state_response = requests.get(state_url)
    response_data = check_request_response(state_response)
    if not response_data:
        return False

    sign = response_data["data"]["cap_sign"]

    if sign["sign_daily"]:
        number = sign["sign_daily_reward"] / (1024 * 1024)
        progress = round(sign["sign_progress"] / sign["sign_target"] * 100, 2)
        message = f"今日已签到获取{number}MB，进度{progress}%"
        print(message)
        return message

    # 执行签到
    sign_url = f"https://drive-m.quark.cn/1/clouddrive/capacity/growth/sign?{get_query(url)}"
    params = {"sign_cyclic": True}
    headers = {'Content-Type': 'application/json'}
    sign_response = requests.post(sign_url, headers=headers, json=params)

    data_response = check_request_response(sign_response)
    if not data_response:
        return None

    mb = data_response["data"]["sign_daily_reward"] / (1024 * 1024)
    print(json.dumps(data_response))
    return f"签到成功，获取到{mb}MB!"


def quark_auto_task(account):
    """
    夸克盘自动签到
    :param account: 账号信息，包含kps, sign, vcode
    :return: 签到结果
    """
    task_result = "success"
    # 定义多个 账号，每个 账号 带有名称作为键
    账号列表 = {
        # "账号1": "AASdlyqho8zVXQ4US7krPBSa7XacPrhyjZhFMWZMEE6DzaOXgNCO8MMENeLxEH52suoSqmMgOJ02p1HoGDt4%2BTVXsPCBfKmElYWgqItMvc8lBA%3D%3D&AARmhtoyIQTPvQB6JAKWDnomL%2Bs%2B2t4s9AARiQi341AXcJm%2B%2Bk0j1J2Qr7hPeD5HI68%3D&1722327010080",
        "账号2": account,
        "账号3": account
        # 继续添加更多 账号
    }

    # 定义用于存储签到结果的字典
    sign_results = {}

    # 循环遍历每个 url 并调用签到函数
    for name, 账号 in 账号列表.items():
        print(f"正在签到 {name} ...")
        sign_message = quark_sign_in(账号)
        if sign_message:
            sign_results[name] = sign_message
            sign_results["task_result"] = "success"
        else:
            sign_results[name] = "签到失败"
            # notify.send("夸克盘签到异常", f"{name} 的签到失败!")
            sign_results["task_result"] = "error"
            print(sign_results)
            print("夸克盘签到异常", f"{name} 的签到失败!")

    # 输出所有账户的签到结果
    print("\n签到结果：")
    for name, message in sign_results.items():
        print(f"{name}: {message}")

    # 汇总所有签到信息
    summary_message = "\n".join(
        [f"{name}: {message}" for name, message in sign_results.items()])

    # 使用 notify.send 发送汇总信息通知
    # notify.send("夸克盘签到汇总", summary_message)
    print("夸克盘签到汇总", summary_message)
    return sign_results


if __name__ == "__main__":
    app.run(debug=True)
    # quark_auto_task()
