f2 = open(r'F:\Date\book\BX-Books.csv', encoding="ISO-8859-1")
booklist=[]
for i, it in enumerate(f2.readlines()):
        it = it.replace(",", " ");
        it = it.strip()[1:-1].split(r'";"')
        booklist.append(it)


# import json
# def book2json():
#     f2 = open(r'F:\Date\book\BX-Books.csv', encoding="ISO-8859-1")
#     rdict = {}
#     for i, it in enumerate(f2.readlines()):
#         if i == 0:
#             continue
#         it = it.replace(",", " ");
#         # it = it.strip().replace("\"", "").split(';')
#         it = it.strip()[1:-1].split(r'";"')
#         rdict[it[0]] = {
#             'title': it[1],
#             'author': it[2],
#             'year': it[3],
#             'publisher': it[4],
#             'img': it[7],
#         }
#     with open(r'F:\Date\book\BX-Books.json', 'w', encoding='utf-8') as f:
#         json.dump(rdict, f)
#
# f = open(r'F:\Date\book\BX-Books.json', 'r', encoding = 'utf-8')
# dict_data = json.load(f)
# print(dict_data)