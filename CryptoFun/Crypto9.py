import math
def solve(g, h, p):
	N = long(math.sqrt(p-1))
	print "N=",N	
	t = {}
	# Baby step.
	for i in range(N):
		t[pow(g, i, p)]=i
	print "Baby step",t
	c = pow(g, N * (p-2), p)
	for j in range(N):
		y = (h * pow(c, j, p)) % p
		if y in t: 
	 		return j * N + t[y]
	return None
def main():
	g = 2
	h = 128
	p = 257
	print (solve(g,h,p))
if __name__ == '__main__':
	main()