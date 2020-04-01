#!/usr/bin/env python3
# csv 파일을 이용하여 대규모 데이터를 데이터베이스 테이블에 입력하는 방법을 알아보겠다.

import csv
import sqlite3
import sys

# CSV 입력 파일의 경로와 파일명
input_file = sys.argv[1]

# SQLite3 데이터 베이스를 만든다.
con = sqlite3.connect('Suppliers.db')
c = con.cursor()

# 다섯 가지 속성을 지닌 Supplier 테이블에 만든다.
create_table = """CREATE TABLE IF NOT EXISTS Suppliers(
                Supplier_Name VARCHAR2(20),
                Invoice_Number VARCHAR(20),
                Part_Number VARCHAR(20),
                Cost FLOAT,
                Purchase_Date DATE
);"""
c.execute(create_table)
con.commit()

# CSV 파일을 읽는다
file_reader = csv.reader(open(input_file, 'r', newline= ''), delimiter = ',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for col_index in range(len(header)):
        data.append(str(row[col_index]))
    print(data)
# CSV 파일 데이터를 Suppliers 데이터베이스에 입력    
    c.execute("INSERT INTO Suppliers VALUES(?, ?, ?, ?, ?)", data)
con.commit()
print('')

# Suppliers 테이블을 질의한다.
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for col_index in range(len(row)):
        output.append(str(row[col_index]))
    print(output)    

