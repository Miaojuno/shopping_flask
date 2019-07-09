import sql_fun

def checklogin(account,pwd):
    sql = "select * from user where account = '"+account+"'"
    ls=sql_fun.con_sql(sql)
    if ls==[]:
        return "账户不存在"
    if pwd !=ls[0][1]:
        return "密码错误"
    return 'success'