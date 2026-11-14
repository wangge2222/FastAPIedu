'''
前置说明：
Python 3.9+ 原生支持 `list[]`、`dict[]`（不用从 `typing` 导入 `List, Dict`）；
3.8 及更早需要 `from typing import List, Dict`；
下面全部用**现代写法（3.9+）**，FastAPI 项目非常适合这套注解，也是 FastAPI 高频用到的。
类型注解**只是提示，不强制运行时校验**（除非用 pydantic）。
'''

#---------------Optional
from typing import Optional
#老写法
def get_user_name()->Optional[str]:
    #有可能找到名字str，也有可能找不到返回None
    return None;

#新写法
def get_user_name()-> str |None:
    return None;

#搭配参数实例：
def find_item(id:int) -> str | None:
    if id==1:
        return "apple"
    return None;


#---------------list[dict]
#列表，元素是dict
def get_users() -> list[dict]:
    return [{"id":1,"name":"xxx"}]
users=get_users()
for u in users:
    u["id"]



#---------------TypedDict
#作用：给字典定义固定结构，规定有哪些key，每个key的类型
#typedDict专门解决上面list[dict]信息丢失的问题
from typing import TypedDict
class User(TypedDict,total=False):#total=False：字段不是全部必填 部分key可选
    id: int
    name: str
    age: int | None

#使用
u: User = {"id": 1,"name": "wangge", "age": 18}

#列表版本：list[user],代替模糊的list[dict]
user_list: list[User]=[
    {"id": 1, "name": "a", "age": 18},
    {"id": 2, "name": "b", "age": None}
]


#----------------Literal
#作用：限定变量只能是指定的几个固定字面量 只能是你写好的值，不能是别的同类型值
from typing import Literal
Role = Literal["admin","user","guest"]
#只能是admin user guest三者之一
def check_role(role: Role):
    if role=="admin":
        print("管理员")
    elif role == "user":
        print("普通用户")

check_role("admin")#合法
check_role("test")#不合法

