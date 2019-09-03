theater = 50
movies = theater** 0.5
if  movies/1 ==0: 
    print (movies)

Anatomy = 1
Physiology = 1


Embryology = 1
structure = Embryology ** 0.5 
while ( structure + Anatomy + Physiology ) != 1000 or Physiology < 995:
       Embryology = (Anatomy  * Anatomy )+ (Physiology * Physiology)
       structure = Embryology **0.5
       if structure/1 == 0:
                while Anatomy < 995:
                          Anatomy += 1
                          if ( structure  )  +  Anatomy + Physiology == 1000:
                                   print (23456)
       Physiology += 1
print (structure , Anatomy ,  Physiology   )

print (357912)
