# DB1.py

import sqlite3

#연결객체 생성
#con = sqlite3.connect(":memory:")
#물리 데이터베이스 연결
con = sqlite3.connect("c:\\work\\sample2.db")

#커서 객체 생성
cur = con.cursor()

#테이블 구조(테이블 스키마 생성)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

#입력 파라미터 처리(웹페이지, 모바일앱)
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#1건 레코드(행)을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#작업을 정상적으로 완료(입력, 수정, 삭제)
con.commit()
