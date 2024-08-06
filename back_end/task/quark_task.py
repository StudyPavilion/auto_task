import requests
import json
import time


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
    print("state_response", state_response)
    # 检查请求状态
    response_data = check_request_response(state_response)
    print("response_data", response_data)
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
    account_list = {
        # "账号1": "AASdlyqho8zVXQ4US7krPBSa7XacPrhyjZhFMWZMEE6DzaOXgNCO8MMENeLxEH52suoSqmMgOJ02p1HoGDt4%2BTVXsPCBfKmElYWgqItMvc8lBA%3D%3D&AARmhtoyIQTPvQB6JAKWDnomL%2Bs%2B2t4s9AARiQi341AXcJm%2B%2Bk0j1J2Qr7hPeD5HI68%3D&1722327010080",
        "账号2": account,
        # 继续添加更多 账号
    }

    # 定义用于存储签到结果的字典
    sign_results = {"task_result": "", "log": {}}

    # 循环遍历每个 url 并调用签到函数
    for name, account in account_list.items():
        print(f"正在签到 {name} ...")
        sign_message = quark_sign_in(account)

        if sign_message:
            sign_results["log"][name] = sign_message
            sign_results["task_result"] = "success"
        else:
            # sign_results[name] = "签到失败"
            # notify.send("夸克盘签到异常", f"{name} 的签到失败!")
            sign_results["log"][name] = "签到失败"
            sign_results["task_result"] = "error"
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
    print("sign_results", sign_results)
    return sign_results


def main():
    print('quark_task.py is running')
    account = "AASdlyqho8zVXQ4US7krPBSa7XacPrhyjZhFMWZMEE6DzaOXgNCO8MMENeLxEH52suoSqmMgOJ02p1HoGDt4%2BTVXsPCBfKmElYWgqItMvc8lBA%3D%3D&AARmhtoyIQTPvQB6JAKWDnomL%2Bs%2B2t4s9AARiQi341AXcJm%2B%2Bk0j1J2Qr7hPeD5HI68%3D&1722327010080"
    quark_auto_task(account)


if __name__ == '__main__':
    main()
