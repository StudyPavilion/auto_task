import logging

import mysql.connector
from mysql.connector import errorcode

from utils.common import read_json

mysql_config = "../database_config/mysql_config.json"


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


def create_database(cnx, db_name):
    cursor = cnx.cursor()
    try:
        cursor.execute("create database if not exists {} DEFAULT CHARACTER SET 'utf8';".format(db_name))
    except mysql.connector.Error as err:
        logging.error("Failed creating database: {}".format(err))
        return False
    else:
        logging.info("Database created successfully")
        return True


def create_table(cnx, db_name, tables):
    cursor = cnx.cursor()
    cursor.execute("use {};".format(db_name))
    for table_name in tables:
        table_description = tables[table_name]
        try:
            logging.info("Creating table {}: ".format(table_name))
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                logging.error("already exists.")
            else:
                logging.error(err.msg)
            return False
        else:
            logging.info("OK")
            return True


def add_users(cnx, db_name, users):
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


def check_user_exists(cnx, db_name, user_name):
    cursor = cnx.cursor()
    cursor.execute("use {};".format(db_name))
    select_query = "select 1 from user where user_name = %s;"
    cursor.execute(select_query, (user_name,))
    result = cursor.fetchone()
    # 如果结果为True，则表示找到了匹配的用户名
    if result:
        logging.info("{user_name}已存在".format(user_name=user_name))
        return True
    else:
        logging.info("{user_name}不存在".format(user_name=user_name))
        return False


def mysql_init(config, tables, data_users):
    read_json(mysql_config)
    cnx = connect_mysql(config)
    cursor = cnx.cursor()
    create_database(cnx, "auto_task")
    cursor.execute("use auto_task;")
    create_table(cnx, "auto_task", tables)
    if not check_user_exists(cnx, "auto_task", "admin"):
        add_users(cnx, "auto_task", data_users)

    cnx.commit()

    cursor.close()
    cnx.close()

    return True


def main():
    logging.basicConfig(level=logging.DEBUG)  # DEBUG及以上的日志信息都会显示
    logging.info("MySQL 服务正在运行")
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "123456",
        "charset": 'utf8',
    }
    tables = {
        'user': (
            "create table if not exists `user` ("
            "  `user_name` varchar(32),"
            "  `password` varchar(32) not null,"
            "  `email` varchar(32),"
            "  `vip` boolean  not null default false,"
            "  primary key (`user_name`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    }
    data_users = [
        {
            'user_name': "admin",
            'password': "admin",
            'email': "1",
            'vip': 1,
        },
    ]

    mysql_init(config, tables, data_users)
    cnx = connect_mysql(config)
    cursor = cnx.cursor()

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()
