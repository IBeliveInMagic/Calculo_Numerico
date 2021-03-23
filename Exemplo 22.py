import math

def function(x):
    return (pow(x,3))-(3.5*pow(x,2))+(4*x)-(1.5)

def derivada(x):
    return (3*pow(x,2))-(7*x)+(4)

#-------------precisão usada no método da bissecção---------
erro1 = pow(10,-2);
#------------- precisão usada no método de Newton-Rhapson---
erro2 = pow(10,-7);

print("_____________________________________________________________________________________________________________________________")
print("|Exemplo 22\t\t|\tDados Iniciais\t|\tRaiz Aproximada\t|\tFuncao da Raiz Aproximada\t|\tErro em x\t|\tNº de iteracoes |")

#-----------------------------------------Teste 1 ----------------------------------------------

xinicial = 0.5
z = xinicial

k = 1

if(abs(function(xinicial)) < erro2):
    x = xinicial
else:
    while(1):
        x = xinicial - (function(xinicial)/derivada(xinicial))
        if(abs(function(x)) < erro2 or abs(x - xinicial) < erro2):
            break

        xinicial = x
        k = k + 1

    print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
    print("|Teste 1\t\t|\t x0 = %.1f \t\t|\t %.8f \t|\t\t\t %.8f \t\t|\t%.8f\t|\t\t %d \t\t|" % (z,x,function(x),abs(x-xinicial),k))

#-----------------------------------------Teste 2 ----------------------------------------------

xinicial = 1.33333
z = xinicial

k = 1

if(abs(function(xinicial)) < erro2):
    x = xinicial
else:
    while(1):
        x = xinicial - (function(xinicial)/derivada(xinicial))
        if(abs(function(x)) < erro2 or abs(x - xinicial) < erro2):
            break

        xinicial = x
        k = k + 1

    print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
    print("|Teste 2\t\t|\tx0 = %.5f\t|\t %.8f \t|\t\t\t%.8f\t\t\t|\t%.8f\t|\t\t %d \t\t|"% (z,x,function(x),abs(x-xinicial),k))

#-----------------------------------------Teste 3 ----------------------------------------------

xinicial = 1.33334
z = xinicial

k = 1

if(abs(function(xinicial)) < erro2):
    x = xinicial
else:
    while(1):
        x = xinicial - (function(xinicial)/derivada(xinicial))
        if(abs(function(x)) < erro2 or abs(x - xinicial) < erro2):
            break

        xinicial = x
        k = k + 1

    print("|---------------|-------------------|-------------------|-------------------------------|---------------|-------------------|")
    print("|Teste 3\t\t|\tx0 = %.5f\t|\t %.8f \t|\t\t\t%.8f\t\t\t|\t%.8f\t|\t\t %d \t\t|"% (z,x,function(x),abs(x-xinicial),k))
    print("|_______________|___________________|___________________|_______________________________|_______________|___________________|")