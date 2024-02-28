import matplotlib.pyplot as plt

top_5 = dex_data.nlargest(5, '')
others = dex_data[5:].sum()
others['Project'] = 'Others'

# 상위 5개와 'Others'를 포함한 새로운 데이터프레임 생성
pie_data = top_5.append(others, ignore_index=True)

# 파이 차트에 사용할 색상 지정
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'purple']

# 파이 차트 생성
plt.figure(figsize=(8, 8))
plt.pie(pie_data['7 Days Volume'], labels=pie_data['Project'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Top 5 DEX Projects - 7 Days Trading Volume')
plt.show()