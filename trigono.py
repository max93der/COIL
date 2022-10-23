import math
MAXIMUM_ITERATION = 500


def get_arg1():
    print("The function you should enter is formated like this :")
    print("Sum_{i=1}^{k} (a_i)*cos(ix) + Sum_{j=1}^{l} (b_j)*sin(jx) + C\n")

    print("Enter your k")
    k = int(input())
    print("Enter your l")
    l = int(input())

    print("Enter your list of a_i, seprated by spaces")
    a_i = [float(x) for x in input().split()]

    print("Enter your list of b_j, seprated by spaces")
    b_j = [float(x) for x in input().split()]

    print("Enter your C")
    C = int(input())

    print("In which x you want ot evaluate the derivative ?")
    x = float(input())

    return k, l, a_i, b_j, x, C

def derivate1(k,l,a_i,b_j):
    print("The derivative of the Trigonometric Form you entered is:")
    i=0
    while(i<k):
        if(a_i[i] == 0):
            pass
        else:
            print("+",a_i[i]*(i+1),"* (-sin(",i+1,"* x))")
        i+=1

    j=0
    while (j < l):
        if (b_j[j] == 0):
            pass
        else:
            print("+", b_j[j] * (j + 1), "* (cos(", j+1, "* x))")
        j += 1


def evaluation1_derivative(k,l,a_i,b_j, x):
    i = 0
    evaluation = 0
    while (i < k):
        if (a_i[i] == 0):
            pass
        else:
            evaluation += a_i[i] * (i + 1) * -math.sin((i + 1) * x)
        i += 1

    j = 0
    while (j < l):
        if (b_j[j] == 0):
            pass
        else:
            evaluation += b_j[j] * (j + 1) * math.cos((j + 1) * x)
        j += 1

    return evaluation

def evaluation1(k,l,a_i,b_j, x, c):
    i = 0
    evaluation = 0
    while (i < k):
        if (a_i[i] == 0):
            pass
        else:
            evaluation += a_i[i] * math.cos((i + 1) * x)
        i += 1

    j = 0
    while (j < l):
        if (b_j[j] == 0):
            pass
        else:
            evaluation += b_j[j] * math.sin((j + 1) * x)
        j += 1

    evaluation+=c


    return evaluation

def Newton1(k,l,a_i,b_j, c):
    print("What degree of precision is desired ? 10^- ")
    tol = int(input())
    i = 0
    x_n = 1

    while (i < MAXIMUM_ITERATION):

        if (evaluation1_derivative(k,l,a_i,b_j, x_n) == 0):
            print("Division by 0 encountered. The nearest value found is", x_n, "with", i,"iterations")
            return x_n

        x_n1 = x_n - evaluation1(k,l,a_i,b_j,x_n, c) / evaluation1_derivative(k,l,a_i,b_j, x_n)

        if (abs(x_n - x_n1) <= (10 ** (-tol))):
            return x_n1

        x_n = x_n1
        i += 1

    return None