'''
    杯子：
    属性：高度、容积、颜色、材质、种类
    方法：存放水
'''
class Cup:
    __height = 0
    __volume = 0
    __color = ""
    __materials = ""
    __variety = ""

    def setHeight(self,height):
        if height<0 or height>50:
            print("输入非法！")
        else:
            self.__height=height
    def getHeight(self):
        return self.__height

    def setVolume(self,volume):
        if volume<0 or volume >2000:
            print("输入非法！")
        else:
            self.__volume=volume
    def getVolume(self):
        return self.__volume

    def setColor(self,color):
        if color.isdigit():
            print("输入非法！")
        elif not color.endswith("色"):
            print("颜色必须以色字结尾！")
        else:
            self.__color=color
    def getColor(self):
        return self.__color

    #设置材质
    def setMaterials(self,materials):
        if materials.isdigit():
            print("输入非法！")
        else:
            self.__materials=materials
    def getMaterials(self):
        return self.__materials

    #设置种类
    def setVariety(self,variety):
        if variety.isdigit():
            print("输入非法！")
        else:
            self.__variety = variety

    def getVariety(self):
        return self.__variety

    def storeWater(self):
        print(self.__variety,"是",self.__color,"的，有",self.__height,"cm高，是",self.__materials,"材质，可以装",self.__volume,"ml的水。")

if __name__ == "__main__":
    cup = Cup()
    cup.setHeight(20)
    cup.setVolume(300)
    cup.setColor("粉色")
    cup.setMaterials("304不锈钢")
    cup.setVariety("保温杯")
    cup.storeWater()