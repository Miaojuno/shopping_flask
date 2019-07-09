from flask import Flask, render_template, request, session, json

import search_fun
import user_fun
import recommend_fun
import book_eva_fun
import simliar_book_fun
import getbooklist

app = Flask(__name__)
app.secret_key = '123456'
app.config['DEBUG']=True
app.jinja_env.auto_reload = True


# 登陆页面
@app.route('/')
def login():
    return render_template('page/login.html')



# 主界面/热门top50
@app.route('/index')
def index():
    return render_template('page/index.html')


# 评分top50
@app.route('/index2')
def index2():
    return render_template('page/index2.html')


# 所有图书
@app.route('/allbook')
def allbook():
    session["page"]=request.args.get('page')
    return render_template('page/allbook.html')


# 专属推荐
@app.route('/rec')
def rec():
    return render_template('page/rec.html')


# 我的评价
@app.route('/myeva')
def myeva():
    return render_template('page/myeva.html')


# 图书详情界面
@app.route('/detail')
def detail():
    session["bookid"]=request.args.get('bookid')
    return render_template('page/detail.html')


# 搜索界面
@app.route('/searchresult')
def searchresult():
    session["inputtext"]=request.args.get('inputtext')
    return render_template('page/searchresult.html')


# 获取页数
@app.route('/getpage')
def getpage():
    return session.get("page")


# 登陆
@app.route('/checklogin')
def checklogin():
    account = request.args.get('account')
    pwd = request.args.get('pwd')
    msg=user_fun.checklogin(account,pwd)
    if msg=='success':
        session["account"] = account
    return msg


# 获取热评书top50
@app.route('/gethot')
def gethot():
    return book_eva_fun.gethot(50,getbooklist.booklist)


# 获取评价top50
@app.route('/gethigh')
def gethigh():
    return book_eva_fun.gethigh(50,getbooklist.booklist)


# 获取所有书
@app.route('/getallbook')
def getallbook():
    page = session.get("page")
    return book_eva_fun.getallbook(int(page),getbooklist.booklist)


# 获取所有书
@app.route('/getsearchresult')
def getsearchresult():
    inputtext = session.get("inputtext")
    return search_fun.search(inputtext)


# 获取inputtext
@app.route('/getinputtext')
def getinputtext():
    return session.get("inputtext")

# 获取用户的所有评价
@app.route('/getmyeva')
def getmyeva():
    return book_eva_fun.getmyeva(session.get("account"),getbooklist.booklist)


# 获取图书详情
@app.route('/getdetail')
def getdetail():
    return book_eva_fun.getdetail(session.get("bookid"),getbooklist.booklist)


# 获取相似book top10
@app.route('/getsim')
def getsim():
    try:
        return simliar_book_fun.top10_simliar_book(session.get("bookid"), getbooklist.booklist)
    except:
        return book_eva_fun.gethigh(10,getbooklist.booklist)


# 添加一条评分数据
@app.route('/addeva')
def addeva():
    userid = session.get("account")
    bookid=request.args.get("bookid")
    score = request.args.get("score")
    return book_eva_fun.addeva(userid,bookid,score)


# 为用户推荐
@app.route('/getrec')
def getrec():
    try:
        return recommend_fun.recommend(int(session.get("account")),getbooklist.booklist)
    except:
        return "1"+book_eva_fun.gethigh(10,getbooklist.booklist)


if __name__ == '__main__':
    app.run()
