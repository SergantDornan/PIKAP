import os
import random
import time
import math
import numpy as np
from scipy.linalg import solve
def generateVector(n, a, b):
	vector = [random.uniform(a, b) for _ in range(n)]
	return vector

def write(filename, vector):
	with open(filename, 'w') as f:
		for i in vector:
        		f.write(str(i) + ' ')

def powerAp(mp,power):
	a = np.zeros(2*power)
	b = np.zeros(power+1)
	for key, value in mp.items():
		for i in range(0, len(a)):
			a[i] += (key**(i+1))
		for i in range(0, len(b)):
			b[i] += (value * (key**(power - i)))
	matrix = np.zeros((power+1,power+1), dtype=float)
	for i in range(0, power + 1):
		row = []
		for j in range(0, power + 1):
			if((len(a) - 1 - i - j) < 0):
				row.append(len(mp))
			else:
				row.append(a[len(a) - 1 - i - j])
		matrix[i] = row
	x = solve(matrix, b)
	print(x[0])


testFile = "testFile_2"
textFile = "analFile"
mp = dict()
i = 0
testV = generateVector(10000,1,1000)
os.system("touch " + textFile)
write(textFile, testV)
start_time = time.perf_counter()
os.system("./" + testFile + " " + textFile + " Dummy")
end_time = time.perf_counter()
testTime = (end_time - start_time)*10000
n = 0
delta = 0
if (testTime < 1000):
	delta = 20000
	n = 50000
else:
	delta = 10000
	n = 10000
for xi in range(n, n + delta +1,500):
	vector = generateVector(xi,1,1000)
	write(textFile, vector)
	start_time = time.perf_counter()
	os.system("./" + testFile + " " + textFile + " Dummy")
	end_time = time.perf_counter()
	elapsedTime = (end_time - start_time)*10000
	mp[math.log(xi)] = math.log(elapsedTime)
os.system("rm " + textFile)
powerAp(mp,1)