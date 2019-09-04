green = 0
carpenter = 1
lemons = (green *green) + ( carpenter* carpenter )
lemon = lemons ** 0.5
while carpenter  <999 or green < 999:
         if carpenter  == 998:
                #carpenter = green + 1
                green  += 1
                carpenter = green + 1 
         carpenter  +=1
         lemons = ((green *green) + ( carpenter* carpenter ))
         lemon = lemons ** 0.5
         #print(lemon)
         if lemon % 1 == 0:
                watermelon = lemon + green +  carpenter 
                if watermelon  == 1000: 
                      print (lemon, green, carpenter )

#if watermelon  == 1000: 
#      print (lemon, green, carpenter )
