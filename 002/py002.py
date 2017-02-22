# -*- coding: utf-8 -*-
# __author__:Ww2zero


import MySQLdb
import string
import random


class ACMySqlDB(object):
    """
    # 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
    """

    def __init__(self):
        self.conn = None
        self.cur = None
        self.config = {
            'user': 'root',
            'passwd': '2014',
            'host': '127.0.0.1',
            'db': 'userkeys',
            'charset': 'utf8',
        }

    def connect(self):
        self.conn = MySQLdb.connect(**self.config)

    def cursor(self):
        try:
            self.cur = self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            self.cur = self.conn.cursor()

    def createTable(self):
        '''
        CREATE TABLE `ukeys` (
        `uid`  int UNSIGNED NOT NULL AUTO_INCREMENT ,
        `ukey`  varchar(60) NOT NULL ,
        PRIMARY KEY (`uid`)
        );
        '''
        sql_create = ''' CREATE TABLE `ukeys` ( `uid`  int UNSIGNED NOT NULL AUTO_INCREMENT , `ukey`  varchar(60) NOT NULL ,PRIMARY KEY (`uid`) )'''
        self.cur.execute(sql_create)

    def InsertDatas(self, key_list):
        '''
        INSERT INTO `uKeys` (`uid`, `ukey`) VALUES ('1', '2')
        '''
        sql_insert = "INSERT INTO `uKeys` (`ukey`) VALUES (%(value)s)"
        self.cur.executemany(sql_insert, [dict(value=v) for v in key_list])

    def query(self, sql):
        '''
        查询sql
        '''
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def QueryData(self):
        sql_select = "select ukey from ukeys"
        rows = self.query(sql_select)
        self.printResult(rows)

    def printResult(self, rows):
        if rows is None:
            print "rows None"
        for row in rows:
            print row

    def DeleteData(self, uid):
        sql_delete = "delete from `uKeys` where id=" + uid
        self.cur.execute(sql_delete)

    def DropTable(self):
        sql_drop = '''DROP TABLE IF EXISTS `ukeys`'''
        self.cur.execute(sql_drop)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


class ActivateCodes(object):
    """
    生成激活码
    """

    def __init__(self):
        #  字典域 由数字和字母（包括大小写）组成
        self.FIELD = string.digits + string.letters
        self.GENERATE = None

    def createCodes(self, codenumber=10, codesize=10):
        """
            生成codenumber组随机码,每组生成的码的长度为codesize
        """
        def getCode(codesize):
            """
                得到codesize位激活码
            """
            return "".join(random.sample(self.FIELD, codesize))
        self.GENERATE = [getCode(codesize) for i in range(codenumber)]
        return True

    def writeInFile(self, file):
        """
            写入文件 并按顺序排列
        """
        for i in self.GENERATE:
            with open(file, "a") as boom:
                boom.write(i + " \n")

    def saveinMySQL(self):
        db = ACMySqlDB()
        db.connect()
        db.cursor()
        db.DropTable()
        db.createTable()
        db.InsertDatas(self.GENERATE)
        db.commit()
        db.QueryData()
        db.close()

if __name__ == "__main__":
    ac = ActivateCodes()
    ac.createCodes(200, 30)
    ac.saveinMySQL()
