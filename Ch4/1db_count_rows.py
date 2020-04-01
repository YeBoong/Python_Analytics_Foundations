#!/usr/bin/env python3
# SQL 쿼리가 출력한 행의 수(데이터의 수) 계산
import sqlite3

# 메모리에 SQLite3 데이터베이스를 만든다.
con = sqlite3.connect(':memory:')       # RAM 에 데이터베이스 생성.
c = con.cursor()

# 네 가지 속성을 지닌 sales 테이블을 만든다.
create_table = """CREATE TABLE sales(
                customer VARCHAR2(20),
                product VARCHAR2(40),
                amount FLOAT,
                date DATE
);"""
c.execute(create_table)
con.commit()            # 저장

# sales 테이블에 데이터를 삽입한다.
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
('Svetlan Crow', 'Printer', 155.75, '2014-02-03'),
('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
c.executemany(statement, data)
con.commit()            # 저장

# sales 테이블을 질의한다. 행의 수를 계산할 count 변수를 생성한다.
row_count = 0
c.execute("SELECT * FROM sales")
rows = c.fetchall()     # Select * FROM sales 명령으로 받아온 sales 테이블의 모든 데이터를 rows 라는 튜플 단위의 리스트 객체에 저장
for row in rows:
    print(row)
    row_count+=1
print('Number of rows : {}'.format(row_count))