# Functions

def computepay(h, r):
    rt=0
    if h>40:
        rt=(h-40)*rate*1.5
    return (40*r)+rt
       
        

hrs =float(input("Enter Hours:"))
rate=float(input("Enter rate:"))
p = computepay(hrs, rate)
print("Pay", p)