from math import *



# {bookid:{userid:score,    ....},    ........}
def getdata():
    f3 = open(r'F:\Date\book\ratings.csv')
    data = {}
    for i, it in enumerate(f3.readlines()):
        it = it.strip().split(";")
        try:
            userid = int(it[0])
            bookid = it[1]
            score = int(it[2])
            if bookid not in data:
                data[bookid] = {userid: score}
            else:
                data[bookid][userid] = score
        except:
            pass
    return data



def pearson_sim(user1, user2,data):
    user1_data = data[user1]
    user2_data = data[user2]
    distance = 0
    common = {}

    for key in user1_data.keys():
        if key in user2_data.keys():
            common[key] = 1
    if len(common) == 0:
        return 1
    n = len(common)

    ##计算评分和
    sum1 = sum([float(user1_data[movie]) for movie in common])
    sum2 = sum([float(user2_data[movie]) for movie in common])

    ##计算评分平方和
    sum1Sq = sum([pow(float(user1_data[movie]), 2) for movie in common])
    sum2Sq = sum([pow(float(user2_data[movie]), 2) for movie in common])

    ##计算乘积和
    PSum = sum([float(user1_data[it]) * float(user2_data[it]) for it in common])

    ##计算相关系数
    num = PSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 1
    r = num / den
    return 1-r # 这里返回值越小，相似度越大


# 计算某本书最相似的10本书 # 相似值越小 越相似
def top10_simliar_book(bookID,booklist):
    data=getdata()
    res = []
    for bookid in data.keys():
        # 排除与自己计算相似度
        if not bookid == bookID:
            simliar = pearson_sim(bookID, bookid ,data)
            res.append((bookid, simliar))
    res.sort(key=lambda val: val[1])
    ndict = {}
    for i in res[:10]:
        ndict[i[0]] = i[1]
    nls = []
    for it in booklist:
        if it[0] in ndict:
            it.append(ndict[it[0]])
            nls.append(it)

    nls.sort(key=takeNum, reverse=True)
    return str(nls)


# 排序用函数
def takeNum(elem):
    try:
        return float(elem[8])
    except:
        return float(elem[9])