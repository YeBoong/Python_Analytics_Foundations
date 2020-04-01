#!/usr/bin/env python3
import sys

input_file = sys.argv[1]    # 입력 파일
output_file = sys.argv[2]   # 출력 파일

messages = {}               # 빈 (외부) 딕셔너리
notes = []                  # 입력 파일 내의 모든 [Note] 메시지를 저장할 리스트

with open(input_file, 'r', newline='') as text_file:        # with open으로 입력파일을 열고 text_file 객체에 담는다.
    for row in text_file:                                   # text_file에 대해 행마다 반복문 실행
        if '[Note]' in row:                                 # 행에 [Note]라는 내용을 포함할 경우
            row_list = row.split(' ', 4)                    # 행 내용을 단일 공백 문자 단위로 최대 4개까지 짤라서 row_list에 저장.
            day = row_list[0].strip()                       # day 변수에 row_list의 첫 번째 요소, 날짜를 저장
            note = row_list[4].strip('\n')                  # note 변수에 row_list의 다섯 번째 요소, [Note] 메시지 내용 저장
            if note not in notes:                           # notes 리스트(입력 파일 내의 모든 [Note] 메시지를 저장할 리스트)에 note 변수의 값이 없을 경우
                notes.append(note)                              # notes 리스트에 note 값 추가
            if day not in messages:                         # day 값이 messages (외부) 딕셔너리의 키로 포함 되지 않았을 경우
                messages[day] = {}                              # messages 딕셔너리에 키로 day를 추가하고 값으로 빈 (내부) 딕셔너리를 준다.
            if note not in messages[day]:                   # note 값이 messages[day] (내부) 딕셔너리의 키로 포함되지 않았을 경우
                messages[day][note] = 1                         # note를 messages[day]의 (내부) 딕셔너리 키로 추가 하고, 값으로 1을 준다.
            else :                                              # note가 (내부) 딕셔너리 키로 이미 포함 되어 있는 경우
                messages[day][note] += 1                            # 기존 키의 값에 1을 더한다.

######################################## 출력 코드 ########################################3

filewriter = open(output_file, 'w', newline='')             # 출력을 위한 filewriter 객체를 만든다.
header = ['Date']                                           # 헤더 리스트
header.extend(notes)                                        # 헤더 리스트에 notes 리스트 요소들을 추가
header = ','.join(map(str, header)) + '\n'                  # 헤더 리스트 요소 사이마다 쉼표를 입력하여 하나의 긴 문자열로 만들어 저장.
print(header)                                               
filewriter.write(header)                                    # 하나로 연결시킨 헤더 값을 출력파일에 쓴다.
for day, day_value in messages.items():                     # 딕셔너리의 키와 값들에 대해 반복문 실행
    row_of_output = []                                      # 행 출력을 위한 리스트 생성.
    row_of_output.append(day)                               # 행 출력 리스트에 딕셔너리의 키들을 추가
    for index in range(len(notes)):                         # notes 리스트 인덱스들에 대해 반복문 실행
        if notes[index] in day_value.keys():                # notes 리스트의 특정 인덱스 요소 값이 msaages[day]의 내부 딕셔너리 키인 note 메시지일 경우
            row_of_output.append(day_value[notes[index]])       # 해당 키의 값을 행 출력 리스트에 추가.
        else:                                               # notes 리스트의 특정 인덱스 요소 값이 msaages[day]의 내부 딕셔너리 키인 note 메시지가 아닐 경우
            row_of_output.append(0)                             # 행 출력 리스트에 값으로 0을 추가.
    output = ','.join(map(str, row_of_output)) + '\n'       # output이라는 변수를 만들어서 행 출력 리스트의 요소마다 쉼표를 추가 한 후 하나의 문자열로 만들어 저장.
    print(output)                                           
    filewriter.write(output)                                # 출력 파일에 최종적으로 output 내용을 쓴다.
filewriter.close()                                          # write를 위해 열었던 출력 객체를 닫는다.