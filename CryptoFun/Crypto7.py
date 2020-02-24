'''
Algorithm:
    1. pick a random puzzle from the lit of puzzles(below implementation picks first one)
    2. generate list of possible keys by bruteforcing the last 16 bits (we already know that the first 14 bytes are 0s)
    3. brute force the random puzzle to find the valid key(validate that cippher upon decrypting returns string like "Puzzle is" in hex)
    4. Use the Valid key to solve all puzzles and find the puzzle where x = "740AC607E4F3A32193DA750FACF38D87"
    5. exit when the correct value of x is found

Output:
Key Value=000000000000000000000000000027e4

x=740ac607e4f3a32193da750facf38d87
k=1bb168fcfaca89d2855ed80e96639e9a
Cipher=82CC81F9392D37F79AB70AC889C9103528F9502F5EEDE77F923E9071FD2130374D8ECD62511F054044611171CC68C0F9235BD612FE421E121FB19F

Decryption= 50757a7a6c6520697320740ac607e4f3a32193da750facf38d873a1bb168fcfaca89d2855ed80e96639e9a
Key is000000000000000000000000000027e4


'''




import crypto
import sys
from Crypto.Util import Counter
from Crypto.Cipher import AES
from bitstring import BitStream, BitArray
keyList=[]
finalKey=[]
def generateKeys(knownbits):#Generate all the combinations 128 bit key by bruteforcing the last 16 bits
    i = 0
    while(i < 2**16-1):
        b = BitArray(uint=i , length=16)
        #print(b)
        yield (knownbits+b).hex
        i+=1
def createKeyHash():
    knownbits = BitArray(int=0 , length=112)
    for s in generateKeys(knownbits):
        keyList.append(s)
def main():
    createKeyHash()
    with open("puzzles.txt",'r') as file1:
        for i,cipher in enumerate(file1):
            #str_key = "0123456789abcdef"
            IV = cipher[:32]
            #key_final=""
            ctr = Counter.new(128, initial_value=int(IV, 16))
            for k in keyList:
                cipher1 = AES.new(bytearray.fromhex(k), AES.MODE_CTR, counter=ctr)
                ciphertext = BitArray(hex=cipher[32:]).tobytes()
                a = bytearray(cipher1.decrypt(ciphertext))
                a = ''.join('{:02x}'.format(x) for x in a)
                puzzle = a[:20]
                x = a[20:52]
                colon= a[52:54]
                key= a[54:]
                if(puzzle== "50757a7a6c6520697320"):
                    print("Key Value=" + k)
                    finalKey.append(k);
                    break
            if(keyList[0]):
                break
        key_f= finalKey[0]
        for count, cipher in enumerate(file1):
            IV = cipher[:32]
            ctr = Counter.new(128, initial_value=int(IV, 16))
            cipher1 = AES.new(bytearray.fromhex(key_f), AES.MODE_CTR, counter=ctr)
            ciphertext = BitArray(hex=cipher[32:]).tobytes()
            a = bytearray(cipher1.decrypt(ciphertext))
            a = ''.join('{:02x}'.format(x) for x in a)            
            puzzle_is = a[:20]
            x = a[20:52]
            colon = a[52:54]
            
            k = a[54:]
            if x == "740AC607E4F3A32193DA750FACF38D87".lower():
                print("\nx=" + x+ "\nk=" + k+"\nCipher=" + cipher+"\nDecryption=" + a+
                      "\nKey is" + key_f)
                exit()
if __name__ == '__main__':
    main()