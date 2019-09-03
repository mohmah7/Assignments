Philosophy = []

diseases = 2



while len(Philosophy) < 10001:
        management = diseases
        inflammation = diseases -1
        while diseases  % inflammation != 0:
              inflammation -=1
        diseases += 1 
        if inflammation == 1:
              Philosophy.append( management  )

#for hand in Philosophy:
#      print( hand)
 Print philosophy[10000]
