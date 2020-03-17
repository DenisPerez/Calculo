import numpy as np
import scipy

h1 =5
p1 = 1000
p2 = 2000
s = 10

def derparcialCx(x,h2):
    return (3*h2*p2*(s-x))/((s-x)**2 + h2**2)**(5/2)

def derparcialCh2(x,h2):
    return -(3*h1*p1*x)/((x**2+h1**2)**(5/2))
    
def gradienteC(x,h2):
    return [derparcialCx(x,h2), derparcialCh2(x,h2)]
    

def derparcialCxx(x,h2):
    return -((3*h1*p1)/(x**2+h1**2)**(5/2))  + ((15*h1*p1*x**2)/(x**2+h1**2)**(7/2)) + ((15*h2*p2*(s-x)**2)/(((s-x)**2)+h2**2)**(7/2)) -((3*h2*p2)/(((s-x)**2) + h2**2)**(5/2))
    
def derparcialCh2h2(x,h2):
    return ((3*h2*p2*(2*(h2**2) - 3*(x**2) + 6*s*x - 3*(s**2) ))/(h2**2 + (s-x)**2)**(7/2))
    
def derparcialCxh2(x,h2):
    return ((3*p2*(x-s)*(4*h2**2 - x**2 + 2*s*x - s**2))/(h2**2 + (s-x)**2)**(7/2))

def HessianaC(x,h2):
    return [[derparcialCxx(x,h2), derparcialCxh2(x,h2) ],[ derparcialCxh2(x,h2) , derparcialCh2h2(x,h2)]]

def BFGS(xinit, tol, maxiter):
    X = [xinit]
    H = [np.array(HessianaC(X[0][0], X[0][1]))]
    P = []
    Y = []
    for k in range(maxiter):
        P.append(np.linalg.solve(H[k], (-1)*np.array((gradienteC(X[k][0], X[k][1])))))
        X.append(np.array(X[k]) + np.array(P[k]))
        Y.append(np.array(gradienteC(X[k+1][0], X[k+1][1])) - np.array(gradienteC(X[k][0], X[k][1])))
        H.append(H[k] + (np.dot(Y[k], Y[k].transpose()))/(np.dot(Y[k].transpose(), P[k])) + np.dot(np.array(gradienteC(X[k+1][0], X[k+1][1])), (np.array((gradienteC(X[k][0], X[k][1]))).transpose())/(np.dot(P[k].transpose(), np.array(gradienteC(X[k][0], X[k][1]))))))
        if(np.linalg.norm(gradienteC(X[k+1][0], X[k+1][1])) <= tol):
            break
    return X[k+1]

C = lambda x,h2 : (p1*h1/np.math.sqrt((h1**2 + x**2)**3)) + (p2*h2/np.math.sqrt(h2**2+(s-x)**2)**3)

xinit = [12.316667270381004, 7.92593]

print(BFGS(np.array(xinit), 1e-14, 20))
print(scipy.optimize.minimize(C, xinit[0], xinit[1], method='BFGS', tol=1e-14))