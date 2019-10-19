'''

i/p layer	hidden layer	o/p layer
#toes 	->	hid[0]	->		hurt?
	
win/loss ->	hid[1]	->		win?

#fans 	->	hid[2]	->		sad?

'''

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65,0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

ih_wgt = [
			[0.1, 0.2, -0.1],
			[-0.1, 0.1, 0.9],
			[0.1, 0.4, 0.1]
]

hp_wgt = [
			[0.3, 1.1, -0.3],
			[0.1, 0.2, 0.0],
			[0.0, 1.3, 0.1]
]

weights = [ih_wgt, hp_wgt]

def w_sum(a, b):
	assert (len(a) == len(b))
	output = 0

	for i in range(len(a)):
		output += (a[i] * b[i])

	return output

def vect_mat_mul(input, weights):
	assert(len(input) == len(weights))
	output = [0] * len(input)

	for i in range(len(input)):
		output[i] = w_sum(input, weights[i])

	return output

def neural_network(input, weights):
	hid = vect_mat_mul(input, weights[0])
	pred = vect_mat_mul(hid, weights[1])
	return pred

input = [toes[0],wlrec[0],nfans[0]]
pred = neural_network(input,weights)
print(pred)