data = []
count = 0
l = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		l = l + len(line)
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')
sum_count = 0
for d in data:
	sum_count += len(d)

print('留言平均長度為', sum_count / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')