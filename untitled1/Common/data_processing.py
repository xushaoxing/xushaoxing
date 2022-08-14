class data_processing():
    def open_read(self,file_path=r"C:\users.txt"):
        # 读取数据
        file=open(file_path,'r')
        # file=file.readlines()
        data = []
        for line in file:
            cols=line.split()
            data.append(cols)
            # yhm=cols[0]
            # mm=cols[1]
        file.close()
        return data
        # with open(file_path, 'r') as file:
        #     data= file.read()
        # return data
    def pandas_read(self,file_path=r"C:\test.xls"):
        # pandas读取数据
        import pandas
        file=pandas.read_excel(file_path,header=None,names=["yhm","mm"],dtype={"yhm":str,"mm":str})
        data=file.values.tolist()
        # for line in data:
        #     yhm=line[0]
        #     mm=line[1]
        data.pop(0)
        return data
    def mysql_read(self):
        #连接数据库
        import pymysql
        conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="test",charset="utf8")
        cur=conn.cursor()
        #读取数据
        sql="select * from user where yhm >= 'zhsan1'"
        cur.execute(sql)
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data
        # for row in data2:
        #     yhm=row[0]
        #     mm=row[1]
        #     cur.close()
        #     conn.close()
        # 批量插入数据，减少数据库负担
        # data=[]
        # for i in  range(2,22):
        #     data.append(("lisi"+str(i),str(i)))
        # sql="insert into user values(%s,%s)"
        # cur.executemany(sql,data)
        # conn.commit()
if __name__ =="__main__":
    a=data_processing()
    # file_path = r"C:\users.txt"
    print(a.open_read())
    # file_path = r"C:\test1.xls"
    # print(a.pandas_read())
    # print(a.mysql_read())