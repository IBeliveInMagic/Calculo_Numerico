import math

#define a função que será usada no problema
def function(x):
    return pow(x,3) - 9*x + 3

def derivada(x):
    return 3*pow(x,2)-9

#precisões
erro1 = pow(10,-4)
erro2 = pow(10,-4)

xinicial = 0.5

#calcular o número de iterações
k = 1

if(abs(function(xinicial)) < erro1):
    x = xinicial
else:
    while(1):
        x = xinicial - (function(xinicial)/derivada(xinicial))
        if(abs(function(x)) < erro1 or abs(x - xinicial) < erro2):
            break

        print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x),abs(x - xinicial)))
        xinicial = x
        k = k + 1

    print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x),abs(x - xinicial)))

# k : Número de iterações
# x : Raiz aproximada
# function(x) : função da raiz aproximada
# abs(x - xinicial) : erro de x