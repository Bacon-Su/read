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