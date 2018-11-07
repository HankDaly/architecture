import math
###
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
        self.phase1 = [vectory,vectorx_na] #一象限包含的向量是y,-x
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
    a = point1.x
    b = point1.y
    c = point2.x
    d = point2.y
    x1 = vector1.x
    y1 = vector1.y
    x2 = vector2.x
    y2 = vector2.y
    t2 = (c*y1-a*y1-d*x1+b*x1)/(y2*x1-x2*y1)
    point = Point2D([c+x2*t2,d+y2*t2])
    return point

#得到最小角度的向量
def minanglevector(phase1,phase2,veca,vecb):
    #获取各个象限的向量
    vec1 = phase1.start_vec
    vec2 = phase1.end_vec
    vec3 = phase2.start_vec
    vec4 = phase2.end_vec
    #这里需要调用求向量长度的方法
    vec_list = [vec1,vec2,vec3,vec4]
    vec1_len = vec1.len()
    vec2_len = vec2.len()
    vec3_len = vec3.len()
    vec4_len = vec4.len()
    k_2 = vec1_len/vec2_len
    k_3 = vec1_len/vec3_len
    k_4 = vec1_len/vec4_len
    #下面需要用到向量的点积算法
    angle_a1 = veca.dot(vec1)
    angle_a2 = k_2*veca.dot(vec2)
    angle_b3 = k_3*vecb.dot(vec3)
    angle_b4 = k_4*vecb.dot(vec4)
    #找到最小的角度以及对应的vector
    angle_list = [angle_a1,angle_a2,angle_b3,angle_b4]
    min_angle = angle_a1
    min_index = 0
    min_index_other = 0
    for i in range(1,4):
        if angle_list[i] < min_angle:
            min_angle = angle_list[i]
            min_index = i
    #下面需要用到向量的叉积算法
    cross_a1 = veca.cross(vec1)
    cross_a2 = veca.cross(vec2)
    cross_b3 = vecb.cross(vec3)
    cross_b4 = vecb.cross(vec4)
    cross_list = [cross_a1,cross_a2,cross_b3,cross_b4]
    #找到最小角度向量对应的另一边的向量
    if i <= 1:
        if cross_list[i] * cross_list[2] < 0:
            min_index_other = 2
        else:
            min_index_other = 3
    else:
        if cross_list[i] * cross_list[0] < 0:
            min_index_other = 0
        else:
            min_index_other = 1
    #最后按照phase1，phase2的顺序输出向量
    if min_index > min_index_other:
        return vec_list[min_index_other],vec_list[min_index]
    else:
        return vec_list[min_index],vec_list[min_index_other]
        
        


    