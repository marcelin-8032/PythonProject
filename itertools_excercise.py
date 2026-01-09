import itertools


def loop_twice_over_generator(gen):
   
    gen1, gen2 = itertools.tee(gen, 2)
    
    for x in gen1:
        print(x)
        
    for x in gen2:
        print(x)