import math

#define a função que será usada no problema
def function(x):
    return pow(x,3) - 9*x + 3

# intervalo inicial [a,b]
a = 0
b = 1

#precisão
erro1 = pow(10,-3)

#calcular o número de iterações
k = 1

if((b - a) < erro1):
    x = (b+a)/2
else:
    while(1):

        fa = function(a)
        x = (a+b)/2

        if( fa*function(x) > 0):
            a = x
        else:
            b = x
        if ((b - a) < erro1):
            x = (a+b)/2
            print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x), b - a))
            break
        print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x), b - a))
        k = k + 1

# k : Número de iterações
# x : Raiz aproximada
# function(x) : função da raiz aproximada
# b - a : erro de x