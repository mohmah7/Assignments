# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
Philosophy  = 0
Absolutely = 1
structuring = (Philosophy *Philosophy )+ (Absolutely* Absolutely )
while (Philosophy  + Absolutely +  ( structuring ** 0.5 )) != 1000 :
          if Philosophy <  999 : 
                Philosophy += 1
                Absolutely = Philosophy +1 
                print (Absolutely, Philosophy)
          while Absolutely <  999 :
                    Absolutely += 1
                    structuring = (Philosophy *Philosophy )+ ( Absolutely * Absolutely)
                    structuring = structuring** 0.5
                    print (structuring )
                    if structuring % 1 == 0:
                           if structuring + Philosophy + Absolutely == 1000: 
                                  print (23456789)
          #Absolutely = Philosophy +1 
print (Absolutely ,Philosophy )
print (987654321,  structuring )
