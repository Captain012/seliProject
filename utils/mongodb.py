# mongodb
import pymongo
#创建连接
client = pymongo.MongoClient("mongodb://admin:sq@192.168.91.129:27017")
#指定数据库
db = client['sq-waimai']

#指定集合
categories = db['categories']
# ******************************************************

#增
# categories.insert_one({"count":"11","level":"2","name":"变动的的"})
# list=[
#     {},{},{}
# ]
# categories.insert_many(list)

# *********************************************************

# 查询
result = categories.find_one({"count":24,'sub_categories.name':'全部甜品饮品'},{'sub_categories.$':1})
                # 搜索count是24,其中sub_categories中的name是'全部甜品饮品'的数据,  sub_categories只返回name是上述条件的子集合
print(result)
# 多个结果
# results = categories.find({"":""})
# for i in results:
#     print(i)

# *************************************************************

# 修改
# categories.update_one({'count':'14'},{'$set':{'name':'皮皮'}})
#                           前面的条件，后面是设置
# result = categories.find_one({'count':'14'})
# print(result)


# 删除
# categories.delete_one({'count':'xx'})