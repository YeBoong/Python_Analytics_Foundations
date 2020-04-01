#!/usr/bin/env python3
import matplotlib.pyplot as plt
plt.style.use('ggplot')     # ggplot 형식의 스타일시트 사용
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO'] # x축 눈금 레이블의 이름들
customers_index = range(len(customers))          # x축
sale_amount = [127, 90, 201, 111, 232]          # y축
fig = plt.figure()                              # 그림을 그린다.
ax1 = fig.add_subplot(1,1,1)                    # 1행, 1열, 1개의 그래프
ax1.bar(customers_index, sale_amount, align='center', color = 'darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, rotation = 0, fontsize = 'small')
plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()
