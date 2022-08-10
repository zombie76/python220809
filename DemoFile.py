# DemoFile.py

strURL = "http://ycampus.com/?page=" + str(1)
print(strURL)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("----정렬방식지정---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(5/3))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))

#소수점 올림, 버림
import math
print("item:{0:.2f}".format(math.ceil(5/3)))
print("item:{0:.2f}".format(math.floor(5/3)))