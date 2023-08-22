# mysql
import pymysql
#链接数据库
db = pymysql.connect(user='root',password='sq',host='192.168.91.129',port=3306,database='sq-waimai')
#获取游标
cursor = db.cursor()
#执行sql语句
cursor.execute('select * from t_cms_article')
result = cursor.fetchall()
print(result)
cursor.close()
db.close()


# cursor.fetchone 查询一条
#       .fetchall 查询所有
# 除了查询 其他操作需要提交
# 增
# insert into xxxx(ip,lognae,message)values('','','')
# 改
# update xxxx set ip='locohost'  where logname = 'sq';
# 删
# delete from xxx   where logname = 'sq';
# 回滚
# db.rollback()
# 提交
# db.commit()
