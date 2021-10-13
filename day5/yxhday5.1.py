'''
    dict = {"k1":"v1","k2":"v2","k3":"v3"}
    1、请循环遍历出所有的key
    2、请循环遍历出所有的value
    3、请在字典中增加一个键值对,"k4":"v4"
'''
dict = {"k1":"v1","k2":"v2","k3":"v3"}
# 1、请循环遍历出所有的key
for key in dict:
    print(key)
# 2、请循环遍历出所有的value
for key in dict:
    print(dict[key])
# 3、请在字典中增加一个键值对,"k4":"v4"
dict["k4"]="v4"
print(dict)