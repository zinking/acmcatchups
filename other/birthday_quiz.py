
import itertools
import math

def isValidCombination( house,place,food,drink,pet,cig):
    if not( house.index("red") > house.index("blue") and house.index("red") < house.index("white")) : return False
    if not( house.index("yellow") == place.index("hk") and place.index("hk") > 0 ) : return False
    if not ( abs(food.index("pizza") - drink.index("water")) == 1 ) : return  False
    if not ( place.index("bj") == drink.index("maotai") and abs(place.index("bj")-place.index("sh")) == 1 ) : return False;
    #if not ( cig.index("hilton") > pet.index("horse") ) : return False;
    if not ( drink.index("beer") == food.index("chicken") ) : return False;
    if not ( house.index("green") == pet.index("dog")) : return False;
    if not ( abs(food.index("noodle") - pet.index("snake")) == 1 ) : return  False

    tj = place.index("tj")
    nb1 = tj+1
    if nb1 < 5 and not ( abs(food.index("beef"),nb1) == 1 and abs(place.index("cd"),nb1) == 1 ) : return False;
    nb2 = tj-1
    if nb2 > 0 and not ( abs(food.index("beef"),nb2) == 1 and abs(place.index("cd"),nb2) == 1 ) : return False;

    return True
    
    

if __name__ == '__main__':
    house= ["red","blue","white","yellow","green"]
    place = ["hk","cd","bj","sh", "tj"]
    food = ["beef","noodle","chicken","pizza","whatever"]
    drink = ["beer", "maotai", "water", "w1", "w2"]
    pet  = ["dog", "horse", "snake", "p1", "p2"]
    cig  = ["hilton", "c1","c2","c3","c4"]
    cig  = []

    for h in itertools.permutations( house ):
	for p in itertools.permutations(place):
	    for f in itertools.permutations(food):
		for d in itertools.permutations(drink):
		    for pe in itertools.permutations(pet):
			for c in itertools.permutations(cig):
			    if isValidCombination(h,p,f,d,pe,c):
				print h
				print p
				print f
				print d
				print pe
				print c
				print '*'*32



    
