#!/usr/bin/env python3
# 테이블 검색 및 결과물을 CSV로 출력하기
import csv
import MySQLdb
import sys

# CSV 입력 파일 경로와 파일명
output_file = sys.argv[1]

# MySQLdb 데이터베이스에 접속
con = MySQLdb.connect(host = 'localhost', port = 3306, db = 'my_suppliers', user = 'cyj', passwd = '1234')
c = con.cursor()

# 파일 객체를 만든다.
file_writer = csv.writer(open(output_file, 'w', newline = ''), delimiter = ',')

# 헤더 행을 작성한다.
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
file_writer.writerow(header)

# Suppliers 테이블을 검색하고 결과를 CSV 파일에 쓴다.
c.execute("SELECT * FROM Suppliers WHERE Cost > 700.0;")            #   WHERE 이후로 특정 조건 지정
rows = c.fetchall()
for row in rows:
    file_writer.writerow(row)
    
