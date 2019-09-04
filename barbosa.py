# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
Philosophy  = 1
Absolutely = 2
structuring = (Philosophy *Philosophy )+ (Absolutely* Absolutely )
while (Philosophy  + Absolutely +  ( structuring ** 0.5 )) != 1000 :
          if Philosophy <  50 : 
                Philosophy += 1
                Absolutely = Philosophy +1 
                print (Absolutely, Philosophy)
          while Absolutely <  50 :
                    Absolutely += 1
                    structure = (Philosophy *Philosophy )+ ( Absolutely * Absolutely)
                    structure = structure ** 0.5
                    print (structure)
                    if structure % 1 == 0:
                           if structure + Philosophy + Absolutely == 1000: 
                                  print (23456789)
          #Absolutely = Philosophy +1 
print (Absolutely ,Philosophy )
print (987654321,  structure )
