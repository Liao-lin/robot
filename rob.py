import numpy as np
import math
import matplotlib.pyplot as plt


def c(x):
    return np.cos(x)


def s(x):
    return np.sin(x)


def atan2(x, y):
    return np.arctan(x/y)


def xc(x, y):
    return np.matmul(x, y)


l_a, l_b, l_c, l_d, l_e, l_f, l_g = 671, 250, 432, 100, 10, 433, 50
d2 = l_b - l_d
d4 = l_f
a2 = l_c
a3 = l_e


def calculate(x):
    listx =[]
    listy =[]
    angle = None
    point = np.sqrt(5)/5
    TRS = np.array([[1, 0, 0, 242], [0, 1, 0, 150], [0, 0, 1, 188], [0, 0, 0, 1]])
    # 第一条边
    # for step in range(0, 150):
    #     if x in range(6):
    #         TSG = np.array([[1, 0, 0, step], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #         Range = 150

    # 第二条边
    # for step in range(0, 50):
    #     if x in range(6):
    #         TSG1 = np.array([[1, 0, 0, 150+step], [0, 1, 0, 2*step], [0, 0, 1, 0], [0, 0, 0, 1]])
    #         TSG2 = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #         TSG3 = np.array([[point, 2*point, 0, 0], [-2*point, point, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #         TSG = xc(xc(TSG1, TSG2),TSG3)
    #         Range =50

    # #第三条边
    # for step in range(0, 50):
    #     if x in range(6):
    #         TSG1 = np.array([[1, 0, 0, 200-step], [0, 1, 0, 100 + 2*step], [0, 0, 1, 0], [0, 0, 0, 1]])
    #         TSG2 = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #         TSG3 = np.array([[-point, 2*point, 0, 0], [-2*point, -point, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    #         TSG = xc(xc(TSG1, TSG2),TSG3)
    #         Range = 50

    #第四条边
    # for step in range(0, 150):
    #     if x in range(6):
    #         TSG1 = np.array([[1, 0, 0, 150-step], [0, 0, 0, 200], [0, 0, 1, 0], [0, 0, 0, 1]])
    #         TSG2 = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    #         TSG3 = np.array([[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    #         TSG = xc(xc(TSG1, TSG2),TSG3)
    #         Range =150

    # 第五条边
    for step in range(0, 200):
        if x in range(6):
            TSG1 = np.array([[1, 0, 0, 0], [0, 1, 0, 200-step], [0, 0, 1, 0], [0, 0, 0, 1]])
            TSG2 = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
            TSG3 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            TSG = xc(xc(TSG1, TSG2),TSG3)
            Range = 200

        else:
            raise ValueError("请输入1至5，表示需要计算和绘制的边")
        T06 = xc(TRS, TSG)
        px = T06[0][3]
        py = T06[1][3]
        pz = T06[2][3]
        r11 = T06[0][0]
        r13 = T06[0][2]
        r23 = T06[1][2]
        r33 = T06[2][2]
        r21 = T06[1][0]
        r31 = T06[2][0]
# 角1
        o1 = atan2(py, px) - atan2(d2, (math.sqrt(px * px + py * py - d2 * d2)))
        s1 = s(o1)
        c1 = c(o1)
# 角3
        K = (px * px + py * py + pz * pz - l_e * l_e - l_c * l_c - d2 * d2 - d4 * d4) / (2 * l_c)
        o3 = atan2(l_e, d4)-atan2(K, (np.sqrt(l_e*l_e + d4*d4 - K*K)))
        c3 = c(o3)
        s3 = s(o3)
# 角2
        o23 = atan2(((-l_e-l_c*c3)*pz-(c1*px+s1*py)*(d4-l_c*s3)),((l_c*s3-d4)*pz+(l_e+l_c*c3)*(c1*px+s1*py)))
        o2 = o23 - o3
        c2 = c(o2)
        s2 = s(o2)

# 角4
        c23 = c2 * c3 - s2 * s3
        s23 = s2 * c3 + c2 * s3
        o4 = atan2((-r13*s1+r23*c1),(-r13*c1*c23-r23*s1*c23+r33*s23))
        c4 = c(o4)
        s4 = s(o4)
# 角5
        s5 = 0 - (r13*(c1*c23*c4 + s1*s4) + r23*(s1*c23*c4-c1*s4) - r33*s23*c4)
        c5 = r13*(-c1*s23) + r23*(-s1*s23) + r33*(-c23)
        o5 = atan2(s5, c5)
# 角6
        s6 = 0 - r11*(c1*c23*s4 - s1*c4) - r21*(s1*c23*s4 + c1*c4) + r31*s23*s4
        c6 = r11*((c1*c23*c4 + s1*s4)*c5 - c1*s23*s5) + r21*(
                    (s1*c23*c4 - c1*s4)*c5 - s1*s23*s5) - r31*(s23*c4*c5 + c23*s5)
        o6 = atan2(s6, c6)

        angle_one = np.array([[o1], [o2], [o3], [o4], [o5], [o6]])
        if step == 0:
            angle = angle_one
        else:
            angle = np.column_stack((angle, angle_one))

# 正向求解末端 用于末端绘图
        T01 = np.array([[c1, -s1, 0, 0], [s1, c1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        T12 = np.array([[c2, -s2, 0, 0], [0, 0, 1, l_b-l_d], [-s2, -c2, 0, 0], [0, 0, 0, 1]])
        T23 = np.array([[c3, -s3, 0, l_c], [s3, c3, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        T34 = np.array([[c4, -s4, 0, l_e], [0, 0, 1, l_f], [-s4, -c4, 0, 0], [0, 0, 0, 1]])
        T45 = np.array([[c5, -s5, 0, 0], [0, 0, -1, 0], [s5, c5, 0, 0], [0, 0, 0, 1]])
        T56 = np.array([[c6, -s6, 0, 0], [0, 0, 1, 0], [-s6, -c6, 0, 0], [0, 0, 0, 1]])
        T0_6 = xc(xc(xc(xc(xc(T01, T12), T23), T34), T45), T56)
        p_x = T0_6[0][3]
        p_y = T0_6[1][3]
        listx.append(p_x)
        listy.append(p_y)
    return [angle, listx, listy, Range]


# 绘制末端线路
def draw_logo(x):
    x_list = calculate(x)[1]
    y_list= calculate(x)[2]
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure('画第{}条边末端执行器运动'.format(x))
    ax = plt.gca()
    # 设置x轴、y轴名称
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # 画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
    # 参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
    ax.plot(x_list, y_list, color='r', linewidth=1, alpha=0.6)
    plt.show()


# 绘制角度变化图
def draw(x):
    angle = calculate(x)[0]
    Range = calculate(x)[3]
    angle1 = angle[0]
    angle2 = angle[1]
    angle3 = angle[2]
    angle4 = angle[3]
    angle5 = angle[4]
    angle6 = angle[5]
    tex = np.linspace(0, 15, Range, endpoint=True)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure('画第{}条边角度变化'.format(x))

    plt.plot(tex, angle1, color="blue", linewidth=2.5, linestyle="-", label="angle1")
    plt.plot(tex, angle2, color="green", linewidth=2.5, linestyle="-", label="angle2")
    plt.plot(tex, angle3, color="orange", linewidth=2.5, linestyle="-", label="angle3")
    plt.plot(tex, angle4, color="red", linewidth=2.5, linestyle="-", label="angle4")
    plt.plot(tex, angle5, color="gray", linewidth=2.5, linestyle="-", label="angle5")
    plt.plot(tex, angle6, color="purple", linewidth=2.5, linestyle="-", label="angle6")
    plt.legend(loc='center left')
    plt.xlabel("时间")
    plt.ylabel("角度")
    plt.show()


# 输出角度变化txt文件
def write(x):
    temp = calculate(x)[0]
    temp = str(temp)
    with open('画第{}条边时角度数据.txt'.format(x), 'a') as f:
        f.write(temp)


def integration(x):
    draw(x)
    write(x)
    draw_logo(x)


def main():
    integration(3)


main()



