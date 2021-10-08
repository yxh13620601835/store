length = float(input("请输入长度："))
unit = input("请输入单位：")

if unit=="英寸":
   changelength = length*2.54
   print("%.2f英寸是%.2f厘米"%(length,changelength))
elif unit=="厘米":
   changelength = length / 2.54
   print("%.2f厘米是%.2f英寸"%(length,changelength))
else:
   print("单位输入无效！")