from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt


def GetObject():
    print("please enter the type of the object")
    eee = input("choose from point,line or polygon :")

    if eee == "point":
        print("please enter the coordinate in the type of (x,y)")
        x = input("input x:")
        y = input("input y:")
        point_2D = Point(x, y)

        return point_2D, 1

    elif eee == "line":
        print("please enter two points in the line")
        print("please enter the coordinate in the type of (x,y)")
        x1 = input("input the first x:")
        y1 = input("input the first y:")
        x2 = input("input the second x:")
        y2 = input("input the second y:")
        coordinates = [(x1, y1), (x2, y2)]
        line_2D = LineString(coordinates)
        return line_2D, 2

    elif eee == "polygon":
        num = input("Please enter the number of vertices of the polygon")
        points = []
        for i in range(1, (int(num) + 1)):
            dian = []
            dian.append(float(input(f"input the {i}-th x:")))
            dian.append(float(input(f"input the {i}-th y:")))
            points.append(dian)
        polygon_2D = Polygon(points)
        return polygon_2D, 3


print("---codes from 刘启迪2022302131278---")
print("---This project is used to realize topological relationship judgment based on vector data---")
# 获取两个object
print("this is the first object")
object1, num1 = GetObject()
print("this is the second object")
object2, num2 = GetObject()

# 绘制object1的图像
if num1 == 1:
    x1, y1 = object1.xy
    plt.plot(x1, y1, 'ro', label='Point1')

elif num1 == 2:
    x1, y1 = object1.xy
    plt.plot(x1, y1, 'g-', label='Line1')

elif num1 == 3:
    polygon_x, polygon_y = object1.exterior.xy
    plt.fill(polygon_x, polygon_y, alpha=0.5, fc='b', ec='none', label='Polygon1')

# 绘制object2的图像
if num2 == 1:
    x1, y1 = object2.xy
    plt.plot(x1, y1, 'go', label='Point2')

elif num2 == 2:
    x1, y1 = object2.xy
    plt.plot(x1, y1, 'b-', label='Line2')

elif num2 == 3:
    polygon_x2, polygon_y2 = object2.exterior.xy
    plt.fill(polygon_x2, polygon_y2, alpha=0.5, fc='r', ec='none', label='Polygon2')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Geometric Objects')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()

# 判断两者拓扑关系
if object1 == object2:
    print("两者为重合关系")
if object1.disjoint(object2):
    print("两者为相离关系")


if object1.overlaps(object2):
    print("两者为重叠关系")
elif object1.touches(object2):
    print("两者为邻接关系")
elif object1.intersects(object2):
    print("两者为相交关系")


if object2.within(object1):
    print("第一个对象包含第二个对象")
elif object1.within(object2):
    print("第一个对象在第二个对象内")

input("Enter any value to exit the project...")
