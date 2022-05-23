# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
counter=0
result=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num=line.find(':')
    number=line[num+1: ]
    value=number.strip()
    n=float(value)
    result=result+n
    counter=counter+1
print("Average spam confidence:",(result/counter))
