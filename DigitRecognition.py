from sklearn.neighbors import NearestNeighbors
import numpy as np

f = open("train.csv")
t = open("test.csv")
output = open("output","w")
train = []
test = []
label = []

for lines in f.readlines():
	words = lines.strip().split(',')
	if words[0]=='label':
		continue
	numbers = [int(w) for w in words]
	train.append(numbers[1:])
	label.append(numbers[0])

for lines in t.readlines():
	words = lines.strip().split(',')
	if words[0]=='pixel0':
		continue
	numbers = [int(w)/100 for w in words]
	test.append(numbers)

X = np.array(train)
Z = np.array(test)

print("Running nearest neighbors")

probability=[0]*10
counts=[0]*10
total=0

for value in label:
	counts[value]=counts[value]+1
	total=total+1

for index in range(10):
	probability[index]=float(counts[index]/float(total))

print(probability)

output.write("ImageId,\"Label\"\n")

nbrs = NearestNeighbors(n_neighbors=2,algorithm='ball_tree').fit(X)
for index in range(28000):
	_, indices = nbrs.kneighbors(Z[index])
	#np.savetxt(output,indices,delimiter=",")
	indexes = indices.astype(int)

	first = indexes[0][0]
	second = indexes[0][1]
	if label[first]==label[second]:
		output.write(str(index+1)+",\""+str(label[first])+"\"\n")
	else:
		if probability[label[first]] >= probability[label[second]]:
			output.write(str(index+1)+",\""+str(label[first])+"\"\n")
		else:
			output.write(str(index+1)+",\""+str(label[second])+"\"\n")

