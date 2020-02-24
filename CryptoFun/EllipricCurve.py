class Elliptical:
	p=0 
	a=0 
	b=0
	def __init__(self,p,a,b):
		if(self.check(p,a,b)):
			self.p=p
			self.a=a
			self.b=b 
		else:
			print("Invalid values of a,b,p")
			return None

	def check(self,p,a,b):
		x1= 4*a**3 + 27*b**2
		if(x1%p!=0):
			return True
		else:
			return False

	def EllipticPoint(self,x,y):
		#y^2 =x^3+ax+b mod p 
		x1 = (x**3)%self.p
		x2 = (x*self.a)%self.p
		x3 = (x1+x2+self.b)%self.p
		if((y**2)%self.p == x3):
			print("point exists")
			return True
		else:
			print("point doesn't exist")
			return False
	def AddPoints(self,x1,y1,x2,y2):
		print(x1,y1,"+",x2,y2)
		x=abs(x2-x1)
		y=abs(y2-y1)
		p=self.p
		xmod = modInverse(x,self.p)
		s= (y*xmod)%p
		x3= (s**2-x1-x2)%p
		y3= (s*(x1-x3)-y1)%p
		return (x3,y3)
	def selfAddPoint(self,x1,y1):
		x=3*x1**2+self.a
		y=2*y1
		x2=x1
		y2=y1
		p=self.p
		ymod = modInverse(y,self.p)
		s= (x*ymod)%p
		x3= (s**2-x1-x2)%p
		y3= (s*(x1-x3)-y1)%p
		return (x3,y3)
	def multiplyPoint(self,i,x,y):
		print(i,x,y)
		if(i==0):
			return x,y
		if(i%2==0):
			x1,y1=self.selfAddPoint(x,y)
			x2,y2=self.multiplyPoint(i-2,x1,y1)
			return x2,y2
		if(i%2!=0):
			x1,y1=self.multiplyPoint(i-1,x,y)
			x2,y2=self.AddPoints(x1,y1,x,y)
			return x2,y2
	# def findInverse(self,x1,y1):
		

def modInverse(a, m) : 
    g = gcd(a, m)  
    if (g != 1) : 
        print("Inverse doesn't exist") 
        return None
    else :
    	return power(a, m - 2, m)
def power(x, y, m) : 
    if (y == 0) : 
        return 1 
    p = power(x, y // 2, m) % m 
    p = (p*p)%m 
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m) 
  
def gcd(a, b) : 
    if (a == 0) : 
        return b 
    # print(a,b)       
    return gcd(b % a, a) 

#4a^3 +27b^2 != 0 modp
def main():
	curve=Elliptical(11,1,6)
	if(curve.EllipticPoint(2,7)):
		x,y=curve.multiplyPoint(2,5,9)
		# # x,y=curve.AddPoints(5,1,6,3)
		print(x,y)
		#print(y)
if __name__ == '__main__':
	main()