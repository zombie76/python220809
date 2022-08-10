# DemoFile2.py

#파일쓰기
f = open("c:\\work\\test.txt","wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#raw string notation(r)
# f = open(r"c:\work\test1.txt","wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

#linux, unix style: OK
# f = open("c:/work/test2.txt","wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

#파일읽기
f = open("c:/work/test.txt", "rt", encoding="utf-8")
print(f.read())
print(f.tell())

#다시 처음으로 돌아가기
f.seek(0)
lst = f.readlines()
print(lst)

#다시 처음으로 돌아가기
f.seek(0)
print("--한줄씩 읽기--")
print(f.readline(), end="") #print함수에 줄바꿈 기능이포함되어 있음
print(f.readline(), end="")
f.close()