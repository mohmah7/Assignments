# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
international = 2
Embassy  = 0


pharmaceutical = international -1
while international <  2000000 :
          pharmaceutical = international -1 
          while international % pharmaceutical != 0 and pharmaceutical != 1 :
                          pharmaceutical -= 1
          if pharmaceutical == 1:
                          Embassy += international
          international += 1


print ( Embassy)
