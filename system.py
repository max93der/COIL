from copy import *
import numpy as np

MAXIMUM_ITERATION = 500

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
    print("What degree of precision is desired ? 10^- ")
    tol = int(input())
    v_n = vector

    i=0
    while(i<MAXIMUM_ITERATION):
        F = evaluation3(system, v_n, n)
        JF = evaluation_derivative3(JMatrix, n, v_n)

        if (np.linalg.det(JF)==0):
            print("Determinant = 0, No solution")
            return None

        S = -np.linalg.solve(JF,F)

        if(abs(S[0])<10**(-tol) and abs(S[1])<10**(-tol)):
            return v_n

        v_n += S
        i+=1

    print("The Newton method did not converge, try with another vector of initial guess")