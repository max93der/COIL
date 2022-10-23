from variable import *
from trigono import *
from polyno import *
from system import *
MAXIMUM_ITERATION = 500


def print_menu():
    print("What do you want to evaluate ?\n")
    print("1) A trigonometric form\n")
    print("2) A polynomial form of degree n\n")
    print("3) A system of n quadratic equations with n unknowns\n")
    print("4) A system of n polynomial equations with n unknowns\n")



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
    print("Evaluation of the derivative in the given vector", Evaluation3)

    print("Solution for the system: ", Newton3(JMatrix3, n3, vector3, system3))

elif(choice == 4):
    print("Now importing the file variable.py ...")

    JMatrix3 = derivate3(system3, n3)
    print("The Jacobian Matrix for the system is:",JMatrix3)

    Evaluation3 = evaluation_derivative3(JMatrix3, n3, vector3)
    print("Evaluation of the derivative in the given vector",Evaluation3)

    print("Solution for the system: ", Newton3(JMatrix3, n3, vector3, system3))

else:
    print("ERROR: Please enter a value between 1 and 4\n")
    quit()


