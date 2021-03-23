import math

#define a função que será usada no problema
def function(x):
    return pow(x,3) - 9*x + 3

# intervalo inicial [a,b]
a = 0
b = 1

#precisões
erro1 = 5*pow(10,-4)
erro2 = 5*pow(10,-4)

fa = function(a)
fb = function(b)

#calcular o número de iterações
k = 1

if((b-a) < erro1):
   x = ((a*fb-b*fa)/(fb-fa))
else:
    if ((math.fabs(fa) < erro2) or (math.fabs(fb) < erro2)):
        x = a
    else:
        while(1):
            fa = function(a)
            fb = function(b)
            x = (a*fb - b*fa)/(fb - fa)

            if(math.fabs(function(x)) < erro2):
                break

            if(fa*function(x) > 0):
                a = x
            elif(fa*function(x) < 0):
                b = x

            if((b-a) < erro1):
                break

            print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x), b - a))
            k = k + 1

        print("%d  ;  %.8f  ;  %.8f ; %.8f " % (k, x, function(x), b - a))

# k : Número de iterações
# x : Raiz aproximada
# function(x) : função da raiz aproximada
# b - a : erro de x