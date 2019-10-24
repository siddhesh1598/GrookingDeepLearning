def neural_network(input, weights):
	out = 0

	for i in range(len(input)):
		out += (input[i] * weights[i])

	return out

wlrec = [0.9, 1.0, 1.0, 0.9]

hurt = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

input = wlrec[0]
true = [hurt[0], win[0], sad[0]]

pred = neural_network(input,weight)

error = [0, 0, 0]
delta = [0, 0, 0]

for i in range(len(true)):
	error[i] = (pred[i] - true[i]) ** 2
	delta = pred[i] - true[i]

weight_deltas = ele_mul(input,weights)
alpha = 0.1

for i in range(len(weights)):
	weights[i] -= (weight_deltas[i] * alpha)