import csv
lis = [];
dele = [];
count = -1;
with open("number.csv","r") as csvf:
	read = csv.reader(csvf);
	for idt in list(read)[0]: 
		#print(idt,count+1);
		count=count+1;
		d = {};
		if(idt == ""):
			if(count%2 == 0):
				dele.append(count);
			else:
				d['id']=count;
		else:
			d['id'] = int(idt);
		if(len(d.keys())>0):
			lis.append(d);
#print(lis);
size = count - len(dele);
count=-1;
with open("fruits.csv","r") as csvf:
	read = csv.reader(csvf);
	for name in list(read)[0]:
		count=count+1;
		if count not in dele:
			for d in lis:
				if(d['id']==count):
					d['name']=name;
					print(d['name'])
	i=0;
	for d in lis:
		if(d['name']==""):
			d['name'] = lis[(i - 9)%size]['name']
		i=i+1;
count = -1
with open("price.csv","r") as csvf:
	read = csv.reader(csvf)
	for price in list(read)[0]:
		count = count + 1;
		for d in lis:
			if(d['id']== count):
				if(price == ""):
					price = 0.0
				else:
					price = float(price)
				d['price'] = price
count = -1
with open("rotten.csv","r") as csvf:
	read = csv.reader(csvf)
	for rot in list(read)[0]:
		count+=1
		for d in lis:
			if(d['id']== count):
				if(rot == "0"):
					rot = "f"
				if(rot == "1"):
					rot = "t"
				if(rot == "t"):
					d['price']=0.0
				d['rot'] = rot
with open("data.csv","w") as csvf:
	writ = csv.DictWriter(csvf,fieldnames = ['id','name','price','rot']);
	writ.writeheader();
	for d in lis:
		writ.writerow(d);
with open("number.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['id'] for d in lis])
with open("fruits.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['name'] for d in lis])
with open("price.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['price'] for d in lis])
with open("rotten.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['rot'] for d in lis])
	
								
				
