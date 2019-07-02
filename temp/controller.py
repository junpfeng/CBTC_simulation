import pymysql


class MySQLController(object):
    """用于python和mysql之间进行交互"""

    def __init__(self):
        self.__host = "127.0.0.1"
        self.__port = 3306  # 3306是mysql服务器的默认端口
        self.__usr = "root"
        self.__passwd = "123"
        self.__database = "netdesign"
        self.__charset = "utf8"
        self.__mysql_conc = None

    def connect_mysql(self):
        """返回是指定的数据库对象"""
        self.__mysql_conc = pymysql.connect(host=self.__host,
                                            port=self.__port,
                                            user=self.__usr,
                                            password=self.__passwd,
                                            db=self.__database,
                                            charset=self.__charset)

    def query_mysql(self, table_str, sql_str):
        """一个通用SQL的查询语句"""
        if self.__mysql_conc:
            self.connect_mysql()
        # 获取数据库连接对象的光标
        _cur = self.__mysql_conc.cursor()
        _cur.execute(sql_str % ("*", table_str))
        return _cur.fetchall()

    def query_mysql(self, sql_str):
        """一个通用SQL的直接查询语句"""
        if self.__mysql_conc is None:
            self.connect_mysql()
        # 获取数据库连接对象的光标
        _cur = self.__mysql_conc.cursor()
        _cur.execute(sql_str)
        return _cur.fetchall()




if __name__ == "__main__":
    print(__name__)
    msc = MySQLController()
    str = msc.query_mysql("select * from mycost")
    print(str)





