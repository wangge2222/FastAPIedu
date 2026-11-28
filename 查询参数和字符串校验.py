from idlelib import query

from fastapi import FastAPI,Query
app=FastAPI()
"""@app.get("/items/")
async def read_items(q:str|None=None):#查询Q的类型为str|NOne 意味着它又可以是str又可以是None默认值确实为None 那么q就不是必填的
    results={"items":[{"item_id":"Foo"},{"item_id":"bar"}]}
    if q:
        results.update({"q":q})
    return results"""
"""
额外校验：
我们打算添加约束：即使q是可选的，但只要提供了该参数，其长度就不能超过50个字符
为此：
"""
from fastapi import Query
from typing import Annotated
"""@app.get("/items/")
async def read_items(q:Annotated[str|None,Query(max_length=50)]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"bar"}]}
    if q:
        results.update({"q":q})
    return results"""
"""
q:Annotated[str|None,Query(max_length=50)]=None
"""
"""
query告诉fastapi这个只需要校验最大长度为50个字符
"""
"""
添加正则表达式

"""
"""@app.get("/items/")
async def read_items(
        q:Annotated[
            str|None,Query(min_length=3,max_length=50,pattern="^fixedquery$")
        ]=None,
):
    results={"items":[{"item_id":"Foo"},{"item_id":"bar"}]}
    if q:
        results.update({"q":q})
    return results"""

# 要声明一个在url中出现多次的查询参数q
"""@app.get("/items/")
async def read_items(q:Annotated[list[str]|None,Query()]=["Foo","Bar"]):
    query_items={"q":q}
    return query_items"""

#可以更多元
@app.get("/items/")
async def read_items(
        q:Annotated[str|None,Query(title="Query string",min_length=3)]=None
):
    results={"items":[{"item_id":"Foo"},{"item_id":"bar"}]}
    if q:
        results.upadate({"q":q})
    return results
