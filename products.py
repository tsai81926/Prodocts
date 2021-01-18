products = []
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

for p in products:
	print(p[0], '的價格是', p[1])
	
with open('products.csv', 'w', encoding='utf-8') as f: #utf-8為通用讀取編碼代號
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') 
#csv檔可用Excel打開，有逗點excel才會分格
#'+'號跟'*'號只能用於字串間，所以整數需轉換為字串，如上7 & 21

