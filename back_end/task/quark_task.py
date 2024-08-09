import logging

import requests
import json
import time
import os
import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.append('..')
from utils.common import read_json, auto_mail_sending

quark_config = "../task_config/quark_config.json"


def get_query(account):
    return f"__t={int(time.time() * 1000)}&sign_cyclic=true&fr=android&kps={account["kps"]}&sign={account["sign"]}&vcode={account["vcode"]}&pr=ucpro&uc_param_str="


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
    # print("state_response", state_response)
    # 检查请求状态
    response_data = check_request_response(state_response)
    # print("response_data", response_data)
    if not response_data:
        return False

    sign = response_data["data"]["cap_sign"]

    if sign["sign_daily"]:
        number = sign["sign_daily_reward"] / (1024 * 1024)
        progress = round(sign["sign_progress"] / sign["sign_target"] * 100, 2)
        message = f"今日已签到获取{number}MB，进度{progress}%"
        # print(message)
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
    # print(json.dumps(data_response))
    return f"签到成功，获取到{mb}MB!"


def quark_auto_task(account):
    """
    夸克盘自动签到
    :param account: 账号信息，包含kps, sign, vcode
    :return: 签到结果
    """
    account_list = []
    # print("accounts:", account, type(account_list))
    # 判断是否为 account 是否为 字典类型，如果是，加入account_list
    if isinstance(account, dict):
        account_list.append(account)
    else:
        account_list = account

    # 定义用于存储签到结果的字典
    sign_results = {"task_result": "", "log": {}}

    # 循环遍历每个 account 并调用签到函数
    for account in account_list:
        logging.info(f"正在签到 {account.get('name')} ...")
        sign_message = quark_sign_in(account)
        if sign_message:
            sign_results["log"][account["name"]] = sign_message
            sign_results["task_result"] = "success"
        else:
            # sign_results[name] = "签到失败"
            # notify.send("夸克盘签到异常", f"{name} 的签到失败!")
            sign_results["log"][account["name"]] = "签到失败"
            sign_results["task_result"] = "error"
            print("夸克盘签到异常", f"{account["name"]} 的签到失败!")
    print("签到汇总", sign_results)
    # 发送短信
    email_msg = "自动任务"
    if sign_results["task_result"] == "success":
        task_result = "成功\n"
    elif sign_results["task_result"] == "error":
        task_result = "失败\n"
    else:
        task_result = "未知错误\n"
    email_msg += task_result
    for account_name in sign_results["log"]:
        email_msg += account_name + ":\n" + sign_results.get("log")[account_name] + "\n"
    auto_mail_sending(email_msg)
    return sign_results


def main():
    print('quark_task.py is running')
    data = read_json(quark_config)
    account_list = data["userList"]
    quark_auto_task(account_list)


if __name__ == '__main__':
    main()
