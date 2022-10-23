from variable import *
from trigono import *
from polyno import *

from copy import *
import numpy as np


MAXIMUM_ITERATION = 500

###########################
#########FUNCTIONS#########
###########################
def print_menu():
    print("What do you want to evaluate ?\n")
    print("1) A trigonometric form\n")
    print("2) A polynomial form of degree n\n")
    print("3) A system of n quadratic equations with n unknowns\n")
    print("4) A system of n polynomial equations with n unknowns\n")



def derivate3(system, n):
    #Creation of a Matrix n*n ready to accept part derivative of equations
    JMatrix = []
    for x in range(n):
        JMatrix.append([])
        for y in range(n):
            JMatrix[x].append([])

    for i in range(n):
        for x in range(n):
            j=0
            for k in range(len(system[i])):
                JMatrix[i][x].append([]) #create the cell for each term of the equation

                derivative = copy(system[i][j])
                derivative[0] = copy(derivative[0]*derivative[x+1])
                derivative[x+1] = copy(derivative[x+1]-1)

                JMatrix[i][x][j]= copy(derivative)

                j+=1

    print(JMatrix)

    f = open("result.txt", "w")
    f.write(str(JMatrix))
    f.close()
    return JMatrix

def evaluation_derivative3(JMatrix, n, vector):
    evaluation = []
    for x in range(n):
        evaluation.append([])
        for y in range(n):
            evaluation[x].append([])


    for i in range(n):
        for x in range(n):
            j=0
            evaluation[i][x] = 0
            for k in range(len(JMatrix[i][x])):
                derivative = copy(JMatrix[i][x][j])

                evaluation_term = derivative[0]
                for a in range(len(vector)):
                   evaluation_term *= copy(vector[a]**derivative[a+1])

                evaluation[i][x] += copy(evaluation_term)

                j+=1

    return evaluation

def evaluation3(system, vector, n):
    evaluation = []
    for x in range(n):
        evaluation.append(0)

    for i in range(n):
        for j in range(len(system[i])):
            term = copy(system[i][j])

            evaluation_term = term[0]

            for a in range(len(vector)):
                evaluation_term *= copy(vector[a]**term[a+1])

            evaluation[i] += copy(evaluation_term)

    return evaluation



def Newton3(JMatrix, n, vector, system):


    print(np.linalg.det(system))

    F1 = evaluation3(system, vector, n)
    F2 = evaluation_derivative3(JMatrix, n, vector)

    


######################
#########CODE#########
######################


print_menu()
choice = int(input())

if(choice == 1):
    k,l,a_i1,b_j1, x1, c1= get_arg1()
    derivate1(k, l, a_i1, b_j1)
    print("The value of the derivative in", x1, "is equal to", evaluation1_derivative(k,l,a_i1,b_j1, x1))
    print("The root found with the Newton's method is",Newton1(k,l,a_i1,b_j1, c1))


elif(choice == 2):
    n2,a_i2, x2 = get_arg2()
    Da_i2, Dn2 = derivate2(n2, a_i2)

    print("The derivative of the Polynomial Form you entered is:")
    i=Dn2
    while (i>=0):
        print("+",Da_i2[i],"* x^",i)
        i-=1

    print("The value of the derivative in", x2, "is equal to", evaluation2(n2,a_i2, x2))
    print("The root found with the Newton's method is",Newton2(a_i2, n2))



elif(choice == 3):
    print("Now importing the file variable.py ...")

    JMatrix3 = derivate3(system3, n3)
    Evaluation3 = evaluation_derivative3(JMatrix3, n3, vector3)
    print(Evaluation3)

    Newton3(JMatrix3, n3, vector3, system3)

elif(choice == 4):
    print("Now importing the file variable.py ...")

    JMatrix3 = derivate3(system3, n3)
    Evaluation3 = evaluation_derivative3(JMatrix3, n3, vector3)
    print(Evaluation3)

    #Newton3(JMatrix3, n3, vector3, system3)

else:
    print("ERROR: Please enter a value between 1 and 4\n")
    quit()


