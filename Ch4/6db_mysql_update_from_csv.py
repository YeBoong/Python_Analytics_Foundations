#!/usr/bin/env python3
# MySQL 데이터베이스의 테이블 내 레코드 갱신하기
import csv
import MySQLdb
import sys

# CSV 입력 파일 경로와 파일명
input_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다.
con = MySQLdb.connect(host = 'localhost', port = 3306, db = 'my_suppliers', user = 'cyj', passwd = '1234')
c = con.cursor()

# CSV 파일을 읽는다
file_reader = csv.reader(open(input_file, 'r', newline = ''), delimiter = ',')

# CSV 파일의 특정 행을 갱신한다.
header = next(file_reader, None)
for row in file_reader:
    data = []
    for col_index in range(len(row)):
        data.append(str(row[col_index]).strip())
    print(data)
    c.execute("UPDATE Suppliers SET Cost = %s, Purchase_Date = %s WHERE Supplier_Name = %s;", data)
con.commit()

# 갱신한 Suppliers 테이블 질의
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for col_index in range(len(row)):
        output.append(str(row[col_index]))
    print(output)
