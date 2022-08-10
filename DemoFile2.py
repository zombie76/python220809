# DemoFile2.py

#파일쓰기
# f = open("c:\\work\\test.txt","wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

#raw string notation(r)
# f = open(r"c:\work\test1.txt","wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

#linux, unix style: OK
f = open("c:/work/test2.txt","wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()