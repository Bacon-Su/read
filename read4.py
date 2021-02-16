import time#標準函式庫

data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:#每一千筆印一次留言數
			print(len(data))

print(data[0])#讀取第一則留言
print('---------------------------------------------------------')
print(data[1])

sumlen = 0#用字串當清單-->可以求總字數

for s in data:
	sumlen += len(s)
print ('留言平均字數為', sumlen/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆字數小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('共有', len(good), '筆有好評')

start_time = time.time()
wc = {}#每個字的計數
for d in data:
	words = d.split(' ')#words是清單,d是str
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增'那個字'進字典,次數是1

for word in wc:
	if wc[word] > 100:#印出出現超過100次的字
		print(word, wc[word])
end_time = time.time()
print('計算時間', end_time - start_time)

while(True):
	w = input('你想查的字:')
	if w in wc:#怕沒有字時會當掉
		print(wc[w])
	else:
		print('沒有這個字')
