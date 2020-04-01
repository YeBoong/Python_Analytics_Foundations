#!/usr/bin/env python3
# 사용할 모듈과 함수 import
import csv
import sys
from datetime import date, datetime

# 사용자 정의 함수 : 두 날짜 간의 차이 계산
def date_diff(date1, date2):
    try:    # strptime()으로 날짜 문자열로부터 datetime 객체를 생성하고 str()로 묶어 문자열로 변환
        diff = str(datetime.strptime(date1, '%m/%d/%Y')-datetime.strptime(date2, '%m/%d/%Y')).split()[0]
    except: # 읽은 문자열의 형식이 '%m/%d/%Y' 이 아닌경우
        diff = 0
    if diff == '0:00:00':
        diff = 0
    return diff

input_file = sys.argv[1]        # 입력 파일
output_file = sys.argv[2]       # 출력 파일

packages = {}                                   # :         빈 외부 딕셔너리 생성.
previous_name = 'N/A'                           # 고객 :    외부 딕셔너리 키. 
previous_package = 'N/A'                        # 패키지명 : 외부 딕셔너리 값. 고객에 대한 내부 딕셔너리. 내부 딕셔너리의 키.
previous_package_date = 'N/A'                   # 패키지 유지 기간 : 내부 딕셔너리의 값.
first_row = True                                
today = date.today().strftime('%m/%d/%Y')       

with open(input_file, 'r', newline='') as input_csv_file:       # with open으로 input_file을 열고 input_csv_file 객체에 담는다
    filereader = csv.reader(input_csv_file)                     # csv.reader()로 input_csv_file을 읽는다.
    header = next(filereader)                                   # header 저장
    for row in filereader:
        current_name = row[0]
        current_package = row[1]
        current_package_date = row[3]
        if current_name not in packages:                        # current_name 값이 packages (외부)딕셔너리에 없다면
            packages[current_name] = {}                         # current_name을 packages 의 키로 지정하고, 이에 해당하는 값을 빈 (내부)딕셔너리로 한다.
        if current_package not in packages[current_name]:       # current_package 값이 packages[current_name]의 내부 딕셔너리에 없다면  
            packages[current_name][current_package] = 0         # 내부 딕셔너리에 current_package 값을 키로 저장하고, 값은 정수 0으로 저장.
        if current_name != previous_name:           # 이름이 다를 때
            if first_row:
                first_row = False
            else:
                diff = date_diff(today, previous_package_date)  # 사용자 정의 함수(오늘 - 과거 패키지 기간)
                if previous_package not in packages[previous_name]:  
                    packages[previous_name][previous_package] = int(diff)   
                else:
                    packages[previous_name][previous_package] += int(diff)
        else:
            diff = date_diff(current_package_date, previous_package_date) # 사용자 정의 함수
            packages[previous_name][previous_package] += int(diff)
        previous_name = current_name
        previous_package = current_package
        previous_package_date = current_package_date

#####################################출력 코드########################################
header = ['Customer', 'Category', 'Total Time (in Days)']
with open(output_file, 'w', newline='') as output_csv_file:
    filewriter = csv.writer(output_csv_file)
    filewriter.writerow(header)
    for customer_name, customer_name_value in packages.items():
        for package_category, package_category_value in packages[customer_name].items():
            row_of_output = []
            print(customer_name, package_category, package_category_value)
            row_of_output.append(customer_name)
            row_of_output.append(package_category)
            row_of_output.append(package_category_value)
            filewriter.writerow(row_of_output)
