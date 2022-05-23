# Strings

text = "X-DSPAM-Confidence:    0.8475"
x= text.find(" ")
num= float(text[x: ])
print(num)