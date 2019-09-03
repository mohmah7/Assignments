Philosophy = []

diseases = 2



while len(Philosophy) < 10005:
        management = diseases
        inflammation = diseases -1
        while diseases  % inflammation != 0:
              inflammation -=1
        diseases += 1 
        if inflammation == 1:
              Philosophy.append( management  )

#for hand in Philosophy:
#      print( hand)
print (Philosophy[10000])
