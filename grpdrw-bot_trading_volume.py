import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# call the data ''

# 날짜 파싱 및 데이터 전처리
df['time'] = pd.to_datetime(df['time'])
df['bot_trades'] = df['number_of_trades'] * df['percent_trades']
df['user_trades'] = df['number_of_trades'] * (1 - df['percent_trades'])
df['bot_volume'] = df['trade_volume_usd'] * df['percent_volume']
df['user_volume'] = df['trade_volume_usd'] * (1 - df['percent_volume'])

# 시간에 따른 'number_of_trades' 그래프
plt.figure(figsize=(12, 6))
plt.plot(df['time'], df['bot_trades'], label='Bot Trades')
plt.plot(df['time'], df['user_trades'], label='Regular User Trades')
plt.xlabel('Time')
plt.ylabel('Number of Trades')
plt.title('Number of Trades Over Time')
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.grid(visible=True)
plt.show()

# 시간에 따른 'trade_volume_usd' 그래프
plt.figure(figsize=(12, 6))
plt.plot(df['time'], df['bot_volume'], label='Bot Trade Volume (USD)')
plt.plot(df['time'], df['user_volume'], label='Regular User Trade Volume (USD)')
plt.xlabel('Time')
plt.ylabel('Trade Volume (USD)')
plt.title('Trade Volume (USD) Over Time')
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.grid(visible=True)
plt.show()
