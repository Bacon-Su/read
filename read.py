#讀取練習

data = []

with open ('games.txt', 'r') as s:#'r'是read讀取的簡寫
	for game in s:
		print(game)#印出來後多空行
		data.append(game.strip())#將game讀進data清單並用strip()將空行去除
#5-8行時是檔案打開狀態，離開後不能讀取
print()

for game2 in data:
	print(game2)