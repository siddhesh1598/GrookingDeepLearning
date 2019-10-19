'''
instead of predicting just
whether the team won or lost,
now we're also predicting whether
they are happy/sad AND the percentage
of the team that is hurt. We are
making this prediction using only
the current win/loss record
'''

weights = [0.3, 0.2, 0.9]

def ele_mul(input, weights):
	output = [0, 0, 0]
	assert (len(output) == len(weights))

	for i in range(len(weights)):
		output[i] = input * weights[i]

	return output


def neural_network(input, weights):
	pred = ele_mul(input,weights)
	return pred

wlrec = [0.65, 0.8, 0.8, 0.9]
input = wlrec[0]
pred = neural_network(input,weights)
print(pred)