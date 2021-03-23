import math

#define a função que será usada no problema
def function(x):
    return pow(x,3) - 9*x + 3

#precisões
erro1 = 5*pow(10,-4)
erro2 = 5*pow(10,-4)

x0 = 0
x1 = 1

#calcular o número de iterações
k = 1

if(math.fabs(function(x0)) < erro1):
    x = x0
else:
    if(math.fabs(function(x1)) < erro1 or math.fabs(x1-x0) < erro2):
        x = x1
    else:
        while(1):
            x = x1 - (function(x1))/(function(x1)-function(x0))*(x1-x0)
            if(abs(function(x)) < erro1 or abs(x-x1) < erro2):
                break

            print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x), abs(x-x1)))
            x0 = x1
            x1 = x
            k = k + 1
    print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x),abs(x-x1)))

# k : Número de iterações
# x : Raiz aproximada
# function(x) : função da raiz aproximada
# abs(x-x1) : erro de x