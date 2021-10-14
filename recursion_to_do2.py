#    1  Recursive Fibonacci-    Write rFib(num). Recursively compute and return numth Fibonacci value. As earlier, treat first two (num = 0, num = 1)
def Fib(x):
    if x==0:
        return 0
    if x ==1:
        return 1
    return Fib(x-1)+ Fib(x-2)

print(Fib(8))
print(Fib(7))
print(Fib(6))



#   2   Recursive “Tribonacci” -    Write function rTrib(num) to mimic Fibonacci, adding previous three values instead of two. First three Tribonacci numbers are 0, 0, 1, 
def trib(x):
    if x <= 2:
        return 0
    if x == 3:
        return 1
    return trib(x-1) + trib(x-2) + trib(x-3)

print(trib(5))
print(trib(4))
print(trib(8))
print(trib(10))


#   3   Paging Dr. Ackermann
#       The Ackermann function is among the earliest examples of a computable but not primitive-recursive function. It grows rapidly and hence can overflow the JavaScript stack frame even at very low values. This function accepts two non-negative integer values, num1 and num2, and follows these rules:
#       ackermann(0,num2) == num2+1;
#       ackermann(num1,0) == ackermann(num1-1,1) if num1 > 0 );
#       ackermann(num1,num2) == ackermann(num1-1,ackermann(num1,num2-1)).
#       Don’t be dismayed if a num1 value as low as 4 “blows your stack”. That’s the nature of this function!   
def Acker(x,y):
    if x==0:
        return y+1
    elif y==0:
        return Acker(x-1, 1)
    return Acker(x-1, Acker(x,y-1))

print(Acker(2,0))
print(Acker(0,3))
print(Acker(2,4))


#   4   Zibonacci
#       This function borrows ideas from the Fibonacci series, but the calculated results appear to zig and zag, hence the name. A so-called ‘Zibonacci’ series would be defined by the following rules:
#       Zib(0) == 1;
#       Zib(1) == 1;
#       Zib(2) == 2;
#       Zib(2n+1) == Zib(n)+Zib(n-1)+1, if n > 0 (i.e. odd values 3 and higher);
#       Zib(2n) == Zib(n)+Zib(n+1)+1, if n > 1 (i.e. even values 4 and higher).
#       Create the Zibonacci(num) function. 
#       What is Zibonacci(10)? Zibonacci(100)?
#       Second: For a given number that might be a Zibonacci result, find the largest index that maps to that result. bestZibNum(3186) == 2467, bestZibNum(3183) == null.

def zib(x):
    if x==0 or x==1:
        return 1
    elif x ==2:
        return 2
    elif x>0 and x%2==0:
        return 2*x+1 == zib(x)+zib(x-1)+1
    elif x>1 and x%2 != 0:
        return 2*x == zib(x) + zib(x+1)+1

zib(10)