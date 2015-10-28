f = open("output",'r')
r = open("rf_benchmark.csv",'r')
import shlex

acc=0;
r.readline()
f.readline()
for line in f.readlines():
	line2 = r.readline();
	l = line.strip().split('\"')[1]
	word = line2.strip().split('\"')[1]
	if int(l)==int(word):
		acc=acc+1	

print(acc/(float(28000)))