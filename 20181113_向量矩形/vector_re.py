import math

#定义一个向量类
class Vector():
    #没有定义原点，所以完整的向量不可脱离点类存在
    def __init__(self,dx,dy):
        self.vector = [dx,dy]

#定义一个相位类
class Phase():
    """接受一个x轴的向量和y轴的向量,x1,y1代表x轴的向量,x2,y2代表y轴的向量"""
    #没有为相位添加原点,这意味着相位类不可脱离点类存在.
    def __init__(self,vectorx,vectory,vectorx_na,vectory_na):
        self.phase0 = [vectorx,vectory] #零象限包含的向量是x,y
        self.phase1 = [vector_y,vectorx_na] #一象限包含的向量是y,-x
        self.phase2 = [vectorx_na,vectory_na] #二象限包含的向量是-x,-y
        self.phase4 = [vectory_na,vectorx] #三象限包含的向量是-y,x

#定义一个点类
class Point():
    """接受一个原点的坐标"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #生成点的相位的方法
    def generatephase(self,vectorx,vectory,vectorx_na,vectory_na):
        """需要相位类所需要的x轴的向量与y轴的向量"""
        self.phase = Phase(vectorx,vectory,vectorx_na,vectory_na)

#定义一个矩形类
class Rectangle():
    """接受一个原点和三个对于原点的向量，顺序是逆时针"""
    #向量给的并不是其他的点的xy,而是与原点相减后的差值
    def __init__(self,x,y,dx1,dy1,dx2,dy2,dx3,dy3):
        #定义矩形的点类,一个原点和三个端点(逆时针)
        self.origin_point = Point(x,y)
        self.origin_point.generatephase(dx1,dy1,dx3,dy3)
        self.point1 = Point(x+dx1,y+dy1)
        self.point1.generatephase(dx1,dy1,dx3,dy3)
        self.point2 = Point(x+dx2,y+dy2)
        self.point2.generatephase(dx1,dy1,dx3,dy3)
        self.point3 = Point(x+dx3,y+dy3)
        self.point3.generatephase(dx1,dy1,dx3,dy3)
        #定义矩形的三个向量
        self.vector1 = [dx1,dy1]
        self.vector2 = [dx2,dy2]
        self.vector3 = [dx3,dy3]

#给定三个向量，判断第一个是否被后两个相夹
def iffolder(vectora,vectorb,vectorc):
    """返回1就是相夹,0就是不相夹,2就是共线"""
    cross_product1 = (vectora[0]*vectorb[1])-(vectora[1]*vectorb[0])
    cross_product2 = (vectora[0]*vectorc[1])-(vectora[1]*vectorc[0])
    cross_product = cross_product1*cross_product2
    if cross_product > 0:
        #叉积大于0直接0
        return 0
    else:
        dot_product1 = (vectora[0]*vectorb[0])+(vectora[1]*vectorb[1])
        if dot_product1 > 0:
            #在点积大于零的情况下，判断是否共线
            if cross_product == 0:
                return 2
            else:
                return 1
        #如果点积小于零，那么也就都是0
        else:
            return 0
#分别给定两条射线的起始点与向量,得到交点,注意输入的不能是平行或共线的射线
def rayrayintersect(point1,vector1,point2,vector2):
    a = point1[0]
    b = point1[1]
    c = point2[0]
    d = point2[1]
    x1 = vector1[0]
    y1 = vector1[1]
    x2 = vector2[0]
    y2 = vector2[1]
    t2 = (c*y1-ay1-dx1+bx1)/(y2*x1-x2*y1)
    point = Point2D([c+x2*t2,d+y2*t2])
    return point

#得到最小角度的向量
def minanglevector(vectora,vector1,vector2,vectorb,vector3,vector4):
    #这里需要调用求向量长度的方法
    vector1_len = vector1.len()
    vector2_len = vector2.len()
    vector3_len = vector3.len()
    vector4_len = vector4.len()
    k_2 = vector1_len/vector2_len
    k_3 = vector1_len/vector3_len
    k_4 = vector1_len/vector4_len
    #下面需要用到向量的点积算法
    angle_a1 = vectora.dot_product(vector1)
    angle_a2 = k_2*vectora.dot_product(vector2)
    angle_b3 = k_3*vectorb.dot_product(vector3)
    angle_b4 = k_4*vectorb.dot_product(vector4)
    #找到最小的角度以及对应的vector
    angle_list = [angle_a1,angle_a2,angle_b3,angle_b4]
    min_angle = angle_a1
    min_index = 0
    for i in range(1,4):
        if angle_list[i] < min_angle:
            min_angle = angle_list[i]
            min_index = i



    