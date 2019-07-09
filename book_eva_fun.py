from flask import json


# 排序用函数
def takeNum(elem):
    try:
        return float(elem[8])
    except:
        return float(elem[9])


def gethot(getnum,booklist):
    f3 = open(r'F:\Date\book\ratings.csv')
    hotbook_dict = {}
    for i, it in enumerate(f3.readlines()):
        it = it.strip().split(';')
        if it[1] not in hotbook_dict:
            hotbook_dict[it[1]] = 1
        else:
            hotbook_dict[it[1]] += 1
    #         排序
    hotbook_dict50 = {}
    list1 = sorted(hotbook_dict.items(), key=lambda x: x[1], reverse=True)
    for i, x in enumerate(list1):
        if i < getnum:
            hotbook_dict50[x[0]] = x[1]
    hotbook_list = []
    for it in booklist:
        if it[0] in hotbook_dict50:
            it.append(hotbook_dict50[it[0]])
            hotbook_list.append(it)

    hotbook_list.sort(key=takeNum, reverse=True)
    return str(hotbook_list)


def gethigh(getnum,booklist):
    f3 = open(r'F:\Date\book\ratings.csv')
    book_dict = {}
    for i, it in enumerate(f3.readlines()):
        if i == 0:
            continue
        it = it.strip().split(';')
        if it[1] not in book_dict:
            book_dict[it[1]] = {"score": int(it[2]), "num": 1}
        else:
            val = book_dict[it[1]]
            val["score"] += int(it[2])
            val["num"] += 1
            book_dict[it[1]] = val
    book_dict2={}
    for key in book_dict:
        # 评分数量<5的不返回
        if book_dict[key]['num']>=5:
            book_dict2[key] = book_dict[key]["score"] / book_dict[key]['num']
    #         排序
    hotbook_dict50 = {}
    list1 = sorted(book_dict2.items(), key=lambda x: x[1], reverse=True)
    for i, x in enumerate(list1):
        if i < getnum:
            hotbook_dict50[x[0]] = x[1]
    hotbook_list = []
    for it in booklist:
        if it[0] in hotbook_dict50:
            it.append(hotbook_dict50[it[0]])
            hotbook_list.append(it)

    hotbook_list.sort(key=takeNum, reverse=True)
    return str(hotbook_list)


def getmyeva(account,booklist):
    f3 = open(r'F:\Date\book\ratings.csv')
    eva_dict = {}
    for i, it in enumerate(f3.readlines()):
        it = it.strip().split(';')
        if it[0] == account:
            eva_dict[it[1]] = [it[2]]
    for it in booklist:
        if it[0] in eva_dict:
            eva_dict[it[0]] = eva_dict[it[0]] + it[1:]

    return json.dumps(eva_dict)


def getdetail(bookid,booklist):
    for it in booklist:
        if it[0]==bookid:
            return str(it)


def addeva(userid,bookid,score):
    f3 = open(r'F:\Date\book\ratings.csv','a')
    f3.write(userid+";"+bookid+";"+score)
    return '评价成功'


def getallbook(page,booklist):
    rlist = []
    startid = (page - 1) * 50 + 1
    endid = page * 50
    for i, it in enumerate(booklist):
        if i >= startid and i <= endid:
            rlist.append(it)
    return str(rlist)



