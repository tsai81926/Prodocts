import os #operating system (作業系統模組) 先載入才可詢問中央

#讀取檔案
products = []
if os.path.isfile('products.csv'):#檢查檔案是否存在
	print('找到檔案了!!')
	with open('products.csv', 'r', encoding='utf_8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過此回合到下一個for loop
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
    
else:
	print('找不到檔案...')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
#上列等於
#p = []
#p.append(name)
#p.append(price)
#products.append(p)	
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案	
with open('products.csv', 'w', encoding='utf-8') as f: #utf-8為通用讀取編碼代號
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') 
#csv檔可用Excel打開，有逗點excel才會分格
#'+'號跟'*'號只能用於字串間，所以整數需轉換為字串，如上7 & 21

