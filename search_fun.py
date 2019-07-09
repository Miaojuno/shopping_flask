from flask import json
from whoosh.fields import *
import os.path
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, MultifieldParser



def createindex():
    schema = Schema(title=TEXT(stored=True),
                    author=TEXT(stored=True),
                    year=NUMERIC(stored=True),
                    publisher=TEXT(stored=True),
                    id=TEXT(stored=True),
                    img=TEXT(stored=True)
                    )
    if not os.path.exists('index'):  # 如果目录index不存在则创建
        os.mkdir('index')
    ix = create_in("index", schema)  # 按照schema模式建立索引目录
    ix = open_dir("index")
    writer = ix.writer()
    f2 = open(r'F:\Date\book\BX-Books.csv', encoding="ISO-8859-1")
    for i, it in enumerate(f2.readlines()):
        try:
            it = it.strip()[1:-1].split(r'";"')
            writer.add_document(
                title=it[1],
                author=it[2],
                year=int(it[3]),
                publisher=it[4],
                id=it[0],
                img=it[7]
            )
        except:
            print(it)
    writer.commit()

def search(inputtext):
    index = open_dir("index")  #读取建立好的索引
    rdict={}
    with index.searcher() as searcher:
        # parser = QueryParser("year", index.schema)
        # myquery = parser.parse("1998")
        parser = MultifieldParser(["title", "author" , "year" , "publisher"], index.schema)
        myquery = parser.parse(inputtext)
        # facet = FieldFacet("price", reverse=True)  #按序排列搜索结果
        # results = searcher.search(myquery, limit=None, sortedby=facet)  #limit为搜索结果的限制，默认为10，详见博客开头的官方文档
        results = searcher.search(myquery, limit=None)  #limit为搜索结果的限制，默认为10，详见博客开头的官方文档
        for result1 in results:
            rdict[dict(result1)["id"]]=dict(result1)
    return json.dumps(rdict)

