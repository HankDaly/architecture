#定义一个相位类
class Phase():
    """接受一个x轴的向量和y轴的向量,x1,y1代表x轴的向量,x2,y2代表y轴的向量"""
    #没有为相位添加原点,这意味着相位类不可脱离点类存在.
    def __init__(self,dx1,dy1,dx2,dy2):
        self.vector_x = [dx1,dy1]
        self.vector_y = [dx2,dy2]
        self.phase0 = [[dx1,dy1],[dx2,dy2]] #零象限包含的向量是x,y
        self.phase1 = [[dx2,dy2],[-1*dx1,-1*dy1]] #一象限包含的向量是y,-x
        self.phase2 = [[-1*dx1,-1*dy1],[-1*dx2,-1*dy2]] #二象限包含的向量是-x,-y
        self.phase4 = [[-1*dx2,-1*dy2],[dx1,dy1]] #三象限包含的向量是-y,x

#定义一个点类
class Point():
    """接受一个原点的坐标"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #生成点的相位的方法
    def generatephase(self,dx1,dy1,dx2,dy2):
        """需要相位类所需要的x轴的向量与y轴的向量"""
        self.phase = Phase(dx1,dy1,dx2,dy2)

#定义一个矩形类
class Rectangle():
    """接受一个原点和三个对于原点的向量，顺序是逆时针"""
    #向量给的并不是其他的点的xy,而是与原点相减后的差值
    def __init__(self,x,y,dx1,dy1,dx2,dy2,dx3,dy3):
        #矩形的原点默认为点类
        self.origin_point = Point(x,y)
        #原点的象限在矩形生成的时候已经确定了
        self.origin_point.generatephase(dx1,dy1,dx3,dy3)
        #定义矩形的三个向量
        self.vector1 = [dx1,dy1]
        self.vector2 = [dx2,dy2]
        self.vector3 = [dx3,dy3]

    