# Conditional Execution
hrs = input("Enter Hours:")
h = float(hrs)
rate=float(input("rate:"))
r=0;
if h>40:
 r=(rate*1.5)*(h-40)
 
pay=((h-5)*rate)+r
print(pay)