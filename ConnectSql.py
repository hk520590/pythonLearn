import pymssql
import time
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
ServerName ="sa"
password_ = "123456"
ServerDomain="127.0.0.1"
port_ = 1433
def ConnectSql():
    conn = pymssql.connect(ServerDomain, ServerName, password, "QPAccountsDB")
    cursor = conn.cursor()
    # 新建、插入操作
    cursor.execute("""
    IF OBJECT_ID('persons', 'U') IS NOT NULL
        DROP TABLE persons
    CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
    )
    """)
    cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
    # 如果没有指定autocommit属性为True的话就需要调用commit()方法
    conn.commit()

    # 查询操作
    cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'Joe Dog')
    row = cursor.fetchone()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()

    # 也可以使用for循环来迭代查询结果
    # for row in cursor:
    #     print("ID=%d, Name=%s" % (row[0], row[1]))

    # 关闭连接
    conn.close()

#需要备份的列表
databaseName =["QPAccountsDB","QPNativeWebDB","QPPlatformDB","QPPlatformManagerDB","QPRecordDB","QPTreasureDB"]

def backupSql():
    nowtime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ""

    con = pymssql.connect(host=ServerDomain, port=port_, user=ServerName, password=password_, database='QPAccountsDB')
    con.autocommit(True)
    cur = con.cursor()
    sql = "backup database QPAccountsDB to disk='F:/QPAccountsDB" + nowtime + ".bak'"
    for i in range(len(databaseName)):
        sql = "backup database "+databaseName[i]+ " to disk='F:/"+ databaseName[i]+ nowtime + ".bak'"
        #print(sql)
        cur.execute(sql)
    con.autocommit(False)
    cur.close()