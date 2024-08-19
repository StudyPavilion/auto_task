import logging

import mysql.connector
from mysql.connector import errorcode

from utils.common import read_json

mysql_config = "database_config/mysql_config.json"


def connect_mysql(config):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logging.error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logging.error("Database does not exist")
        else:
            logging.error(err)
    else:
        return cnx


def disconnect_mysql(cnx):
    cursor = cnx.cursor()
    cursor.close()
    cnx.close()


def create_database(cnx, db_name):
    cursor = cnx.cursor()
    try:
        cursor.execute("create database if not exists {} DEFAULT CHARACTER SET 'utf8';".format(db_name))
    except mysql.connector.Error as err:
        logging.error("数据库：{db_name}创建失败: {err}".format(db_name=db_name, err=err))
        return False
    else:
        logging.info("数据库：{}创建成功".format(db_name))
        return True


def create_table(cnx, tables, db_name="auto_task"):
    error = 0
    cursor = cnx.cursor()
    cursor.execute("use {};".format(db_name))
    logging.info("tables: {}".format(tables))
    logging.info("tables 长度：{}".format(len(tables)))
    for table in tables:
        table_name = table.get("table_name")
        logging.info("table_name:{}".format(table_name))
        table_description = table.get("table_description")
        logging.info("正在创建表： {} ".format(table_name))
        try:
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            error += 1
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                logging.error("表{}已经存在".format(table_name))
            else:
                logging.error(err.msg)
            # return False
        else:
            logging.info("表{}创建成功！".format(table_name))
    return error


def add_users(cnx, users, db_name="auto_task"):
    cursor = cnx.cursor()
    cursor.execute("use {};".format(db_name))
    add_user = ("insert into user "
                "(user_name, password, email, vip) "
                "values (%(user_name)s, %(password)s, %(email)s, %(vip)s)")
    try:
        for user in users:
            cursor.execute(add_user, user)
            cnx.commit()
            logging.info("User {} added successfully".format(user.get("user_name")))
            return True
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            logging.error("用户名重复！")
            logging.error(err)
        else:
            logging.error("发生错误！")
            logging.error(err)
        return False


def check_user_exists(cnx, user_name, db_name="auto_task"):
    cursor = cnx.cursor()
    cursor.execute("use {};".format(db_name))
    select_query = "select 1 from user where user_name = %s;"
    cursor.execute(select_query, (user_name,))
    result = cursor.fetchone()
    logging.info(result)
    # 如果结果为True，则表示找到了匹配的用户名
    if result:
        logging.info("用户{user_name}已存在".format(user_name=user_name))
        return True
    else:
        logging.info("用户{user_name}不存在".format(user_name=user_name))
        return False


def find_user_info(cnx, user_name, db_name="auto_task", field="*"):
    cursor = cnx.cursor()
    cursor.execute("use {};".format(db_name))
    select_query = "select {} from user where user_name = %s;".format(field)
    logging.info("select_query: {}".format(select_query))
    cursor.execute(select_query, (user_name,))
    result = cursor.fetchone()
    logging.info(result)
    return result


def mysql_init():
    logging.info("初始化mysql数据库")
    data = read_json(mysql_config)
    connect_config = data.get("connect_config")
    logging.info("连接mysql配置：{}".format(connect_config))
    tables = data.get("tables")
    logging.info("建表数据：{}".format(tables))
    users_data = data.get("users_data")
    logging.info("用户数据：{}".format(users_data))

    cnx = connect_mysql(connect_config)
    cursor = cnx.cursor()
    create_database(cnx, "auto_task")
    cursor.execute("use auto_task;")
    create_table(cnx, tables)

    if not check_user_exists(cnx, "admin"):
        add_users(cnx, users_data)

    cnx.commit()

    disconnect_mysql(cnx)
    return True


def main():
    logging.basicConfig(level=logging.DEBUG)  # DEBUG及以上的日志信息都会显示
    logging.info("MySQL 服务正在运行")
    mysql_init()
    data = read_json(mysql_config)
    connect_config = data.get("connect_config")
    cnx = connect_mysql(connect_config)
    cursor = cnx.cursor()

    disconnect_mysql(cnx)


if __name__ == '__main__':
    main()
