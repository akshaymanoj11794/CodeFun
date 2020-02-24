#from Crypto.Cipher import DES
from bitstring import BitStream, BitArray
from des import DesKey
plaincipher= []
secondDict={}
possibleKeys=[[]]
firstDict={}

def DESBlackbox(): # Code that generates the plaintext, ciphertext for our attack the inner workings of this code would be hidden in a real scenario, we will treat this as blackbox
	firstK= DesKey(BitArray(formatKey(BitArray(hex="aaaaaaaa0001b1").bin)).tobytes())
	secondK=DesKey(BitArray(formatKey(BitArray(hex="aaaaaaaa001a1a").bin)).tobytes())
	p1="0123456789ABCDEF"
	p2="A01B23C45D67E89F"
	c1 = secondK.encrypt(firstK.encrypt(p1))
	c2 = secondK.encrypt(firstK.encrypt(p2))
	plaincipher.append((p1,c1))
	plaincipher.append((p2,c2))

def formatKey(key): #Convert the 56 bit key into 64 bit key that will be used by DES
	x=7
	keySplits = [key[i: i+x] for i in range(0,len(key),x)]
	s ='0b'
	for k in keySplits:
		s=s+k+"0"
		#print(s)

	return s

def generateKeys(knownbits):#Generate all the combinations 56 bit key by bruteforcing the last 24 bits
	i = 0
	while(i < 2**24):
		b = BitArray(int=i , length=24)
		#print(b)
		yield knownbits+b
		i+=1
def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))
		
def mitm():
	k1=firstDict.keys()
	k2=secondDict.keys()
	possibleVals = intersection(k1,k2)
	for k in possibleVals:
		key1 = firstDict[k]
		key2 = secondDict[k]
		if(verify(key1,key2)):
			exit()

def verify(k1,k2):
	p,c=plaincipher[1]
	print("Verify Keys using second plaintext Ciphertext pair")
	print("Plaintext 2 = "+p)
	print("Ciphertext 2 ="+c)
	key1 = DesKey(BitArray(formatKey(k1.bin)).tobytes())
	key2 = DesKey(BitArray(formatKey(k2.bin)).tobytes())
	c1 = key2.encrypt(key1.encrypt(p));
	if(c1==c):
		print("Verified key pair using second plaintext ciphertext pair :")
		print(k1+"\n")
		print(k2+"\n")
		return True
	else :
		return False


			
def main():
	DESBlackbox() #generate plaintext ciphertext pairs for some keys
	knownk1="aaaaaaaa" #known 32 bits of keys
	knownkBits= BitArray(hex=knownk1)
	print(knownkBits)
	p,c = plaincipher[0]
	print("Plaintext 1 = "+p)
	print("Ciphertext 1 ="+c)
	for k in generateKeys(knownkBits):
		k1 = formatKey(k.bin)
		key=DesKey(BitArray(k1).tobytes())
		firstDict[key.encrypt(p)]=k
		secondDict[key.decrypt(c)]=k
		mitm()
	mitm()

if __name__ == '__main__':
 	main() 