import pymysql

#连接数据库
db=pymysql.connect(host='localhost',user='root',password='123456',charset='utf8')

#创建一个游标对象（相当于指针）
cursor=db.cursor()

#执行创建数据库语句
# cursor.execute('create schema wzg default charset=utf8;')
cursor.execute('use test;')
cursor.execute('select * from user;')
all_01=cursor.fetchone()
all_02=cursor.fetchall()
#fetchone获取一条数据（元组类型）
print(all_02)
#现在指针到了[1]的位置

#fetchall获取全部数据（字符串类型）
all=cursor.fetchall()
for i in all:
    print(i[0])

#关闭游标和数据库连接
cursor.close()
db.close()