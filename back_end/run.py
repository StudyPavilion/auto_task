from task.quark_task import quark_auto_task
from utils.common import read_json

if __name__ == '__main__':
    quark_config = "task_config/quark_config.json"
    data = read_json(quark_config)
    account_list = data["userList"]
    quark_auto_task(account_list)