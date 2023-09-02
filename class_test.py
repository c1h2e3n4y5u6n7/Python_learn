# class Swan:
#     __neck_swan='天鹅类'       # 私有属性
#     def __init__(self):
#         print("__init__()：",Swan.__neck_swan)  # 在实例方法中访问私有属性
# swan=Swan()  # 创建Swan实例
# print("加入类名：",swan._Swan__neck_swan)  # 私有属性可以通过“类的实例名._类名__xxx”方式访问
# print("直接访问：",swan.__neck_swan)  # 私有不能属性可以通过实例名访问，会报错
class Swan:
    _neck_swan='天鹅类'       # 保护属性
    def __init__(self):
        print("__init__()：",Swan._neck_swan)  # 在实例方法中访问保护属性
swan=Swan()  # 创建Swan实例
print("直接访问：",Swan._neck_swan)  #保护属性可以通过类名访问
print("直接访问：",swan._neck_swan)  #保护属性可以通过实例名访问