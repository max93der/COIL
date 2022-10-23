MAXIMUM_ITERATION = 500
from copy import *


def get_arg2():
    print("The function you should enter is formated like this :")
    print("Sum_{i=O}^{n} (a_i)*x^i = 0 \n")
    print("Please enter the degree of the polynomial")
    n = int(input())

    print("Enter the coefficient, starting from the independant term, and finishing with the highest degree, separated by spaces")
    a_i = [float(x) for x in input().split()]

    print("In which x you want ot evaluate the derivative ?")
    x = float(input())

    return n, a_i, x

def derivate2(n,a_i):
    i = 1
    Da_i = copy(a_i)
    while(i<=n):
        Da_i[i] = Da_i[i]*i
        i+=1

    Da_i.pop(0)

    return Da_i, n-1

def evaluation2(n,a_i, x):
    evaluation = 0
    i=0
    while (i <= n):
        evaluation += a_i[i] * (x ** i)
        i += 1

    return evaluation

def Newton2(a_i, n):
    print("What degree of precision is desired ? 10^- ")
    tol = int(input())
    i=0
    x_n=-1
    Da_i, Dn = derivate2(n, a_i)

    while(i<MAXIMUM_ITERATION):

        if (evaluation2(Dn,Da_i,x_n) == 0):
            print("Division by 0 encountered. The nearest value found is", x_n, "with", i,"iterations")
            return x_n

        x_n1 = x_n - evaluation2(n,a_i, x_n)/evaluation2(Dn,Da_i,x_n)

        if (abs(x_n - x_n1) <= (10**(-tol))):
            return x_n1

        x_n = x_n1
        i+=1

    return None