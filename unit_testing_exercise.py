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