import pymysql

def con_sql(sql):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='book', charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cols = cursor.description
    conn.commit()
    conn.close()
    data = list(map(list, data))
    return data