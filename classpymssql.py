import pymssql

#tablename  表名
#coloum   列名
#rowname  字段名   ########这些字段日后备用
class py_mssql(object):
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur
    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        调用示例
        ms = py_mssql(host="localhost",user="sa",pwd="password",db="database")
        resList = ms.ExecQuery("SELECT rowname1,rowname2 FROM tablename where rowname2='有糖'")
        for (rowname1,rowname2) in resList:
            print(rowname1,rowname2) 

        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList
    def ExecNonQuery(self,sql):
        """
        执行非查询语句
        调用示例
        ms.ExecNonQuery("insert into tablenames values('a')")
        ms.ExecNonQuery("update tablename set rownames1='a'where rownames2='b'")

        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
def main():
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="dmsweb")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into rownames values('a')")  插入语句

    ms = py_mssql(host="172.16.0.36",user="sa",pwd="123.abc",db="dmsweb")
    resList = ms.ExecQuery("SELECT Vlogin,VIdentityNo FROM SYSC01 where vpersonname='林杰'")
    for (Vlogin,VIdentityNo) in resList:
        print(Vlogin,VIdentityNo) 
if __name__ == '__main__':
    main()
                 