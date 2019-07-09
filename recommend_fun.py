from math import *



# {userid:{bookid:score,    ....},    ........}
def getdata():
    f3 = open(r'F:\Date\book\ratings.csv')
    data = {}
    for i, it in enumerate(f3.readlines()):
        it = it.strip().split(";")
        try:
            userid = int(it[0])
            bookid = it[1]
            score = int(it[2])
            if userid not in data:
                data[userid] = {bookid: score}
            else:
                data[userid][bookid] = score
        except:
            pass
    return data


def pearson_sim(user1, user2,data):
    user1_data = data[user1]
    user2_data = data[user2]
    distance = 0
    common = {}

    # 找到两位用户都评论过的
    for key in user1_data.keys():
        if key in user2_data.keys():
            common[key] = 1
    if len(common) == 0:
        return 1  # 如果没有共同评论过的，则返回1
    n = len(common)  # 共同评论数目

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


# 计算某个用户与其他用户的相似度
def Euclidean(user1, user2 ,data):
    # 取出两位用户评论过的电影和评分
    user1_data = data[user1]
    user2_data = data[user2]
    distance = 0
    # 找到两位用户都评论过的book，并计算欧式距离
    for key in user1_data.keys():
        if key in user2_data.keys():
            # 注意，distance越大表示两者越相似
            distance += pow(float(user1_data[key]) - float(user2_data[key]), 2)

    return 1 / (1 + sqrt(distance))  # 这里返回值越小，相似度越大

# 计算某个用户最相似的30个用户 # 相似值越小 越相似
def top30_simliar(userID,data):
    res = []
    for userid in data.keys():
        # 排除与自己计算相似度
        if not userid == userID:
            simliar = pearson_sim(userID, userid ,data)
            res.append((userid, simliar))
    res.sort(key=lambda val: val[1])
    return res[:30]


# 按照相似度返回用户 # 相似值越小 越相似
def all_simliar(userID,data):
    res = []
    for userid in data.keys():
        # 排除与自己计算相似度
        if not userid == userID:
            simliar = pearson_sim(userID, userid ,data)
            res.append((userid, simliar))
    res.sort(key=lambda val: val[1])
    return res

# 排序用函数
def takeNum(elem):
    try:
        return float(elem[8])
    except:
        return float(elem[9])

# 根据用户推荐book给其他人
def recommend(user,booklist):
    data=getdata()
    dict1={} # {bookid:{评分，数量}}
    # 获取最相似的30个用户的评分记录组成字典
    for it in top30_simliar(user,data):
        for bookid in data[it[0]]:
            if bookid not in dict1:
                dict1[bookid]={"score":data[it[0]][bookid],"num":1}
            else:
                dict1[bookid]["score"] += data[it[0]][bookid]
                dict1[bookid]["num"] += 1
    recommendations=[]
    for bookid in dict1:
        # 至少有3个相似用户评分过
        if dict1[bookid]["num"]>2:
            if bookid not in data[user].keys():
                recommendations.append((bookid, dict1[bookid]["score"]/dict1[bookid]["num"]))
    recommendations.sort(key=lambda val: val[1], reverse=True)  # 按照评分排序
    # 返回评分最高的10本book
    ndict = {}
    for i in recommendations[:10]:
        ndict[i[0]] = i[1]
    nls=[]
    for it in booklist:
        if it[0] in ndict:
            it.append(ndict[it[0]])
            nls.append(it)

    nls.sort(key=takeNum, reverse=True)
    return str(nls)
