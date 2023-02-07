# Written by Yunrong Cai
# Feb 6 2023
#parameters = [(x1,y1),(x2,y2),x]

def ycoordinate(parameters):
    # ay+bx+c = 0, find the analytical solution
    x1 = parameters[0][0]; x2 = parameters[1][0]; y1 = parameters[0][1]; y2 = parameters[1][1]; x = parameters[2]
    a = 1/(y2-y1)
    b = -1/(x2-x1)
    c = x1/(x2-x1)-y1/(y2-y1)
    y = -(b*x+c)/a
    return y

#parameters = [(1,2),(4,10),2]
#y = ycoordinate(parameters)
#print(y)

#input = [(x1,y1),(x2,y2),(x3,y3)]
def intersection_check(input):
    x1 = input[0][0]; x2 = input[1][0]; x3 = input[2][0]; y1 = input[0][1]; y2 = input[1][1]; y3 = input[2][1]
    a = 1 / (y2 - y1)
    b = -1 / (x2 - x1)
    c = x1 / (x2 - x1) - y1 / (y2 - y1)
    y = -(b*x3+c)/a
    if y == y3:
        return True
    else:
        return False

#input = [(1,2),(4,8),(3,9)]
#y = intersection_check(input)
#print(y)