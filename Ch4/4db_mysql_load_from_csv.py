#!/usr/bin/env python3
# MYSQL 데이터베이스의 테이블에 새 레코드 입력하기
import sys
import csv
import MySQLdb
from datetime import datetime, date

# CSV 입력 파일 경로와 파일명
input_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다.
con = MySQLdb.connect(host = 'localhost', port = 3306, db = 'my_suppliers', user = 'cyj', passwd='1234')
c = con.cursor()

# CSV 파일 읽기
file_reader = csv.reader(open(input_file, 'r', newline = ''), delimiter = ',')

# Suppliers 테이블에 데이터 입력
header = next(file_reader, None)
for row in file_reader:
    data = []
    for col_index in range(len(header)):
        if col_index < 4:
            data.append(str(row[col_index]).lstrip('$').replace(',', '').strip())
        else:
            a_date = datetime.date(datetime.strptime(str(row[col_index]), '%m/%d/%y'))
            # %Y를 쓰면 4자리로 년도를 나타내고, %y를 쓰면 2자리로 년도를 나타낸다.
            # 읽을 CSV의 날짜 열의 저장된 형식을 볼 필요가 있다.
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    print(data)
    c.execute("INSERT INTO Suppliers VALUES(%s, %s, %s, %s, %s)", data)     # 테이블에 data 추가.
con.commit()       # 저장
print('')

# 데이터를 추가한 Suppliers 테이블 질의
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_output = []
    for col_index in range(len(row)):
        row_output.append(str(row[col_index]))
    print(row_output)

