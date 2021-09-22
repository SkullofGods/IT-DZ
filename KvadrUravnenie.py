print("Print a")
a=float(input())
print("Print b")
b=float(input())
print("Print c")
c=float(input())
D=b*b-4*a*c
if D>0:
    print("x1=",(-b-D**0.5)/(2*a)," ; x2=", (-b+D**0.5)/(2*a))
if D==0:
    print("x=", (-b - D**0.5) / (2 * a))
if D<0:
    print("Net deystvitelnih korney")