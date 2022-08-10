# DemoTuple.py

#튜플을 사용하는 경우
def calc(a,b):
    return a+b, a*b

#첫열로 나와서
result = calc(3,4)
print(result)
#결과는 (7,12)로 출력
#슬라이싱하여 출력
print(result[0])
print(result[1])

#여러개의 인자를 넘기는 경우
print("id:%s, name:%s" %("kim", "김유신"))

#set 형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print( type(b) )
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )

#형식을 변경
a = set((1,2,3))
print(a)
a.add((5))
print(a)
print(type(a))
b = list(a)
b.append(4)
print(b)
print(type(b))

#반복구문
for item in b:
    print(item)