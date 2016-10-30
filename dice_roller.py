#!/usr/bin/python

import sys
import numpy as np

def dice_roller(num_dice, sample_size):
	return  np.random.multinomial(num_dice, [1/6.]*6, size=sample_size)
	

#----------------------------------------

num_dice = int(sys.argv[1])
sample_size = int(sys.argv[3])
sums = int(sys.argv[2])

weights = np.array(range(1,7))
rolls =  dice_roller(num_dice, sample_size)

counter = 0
final_sample = []
log_sample = []
for roll in rolls:
	#print roll, np.dot(roll, weights)
	if np.dot(roll, weights) == sums:	
		counter += 1	
		final_sample.append(np.power(weights, roll).prod(dtype='float'))

final_sample = np.array(final_sample)

print "sample ratio:\t", counter, counter / float(sample_size)
print "mean:\t", np.mean(final_sample) 
print "SD:\t", np.std(final_sample) 

