def zeros_matrix(a, b):

	out = []

	for i in range(a):
		x = [0] * b
		out.append(x)

	return out


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


def outer_product(a, b):
	out = zeros_matrix(len(a), len(b))

	for i in range(len(a)):
		for j in range(len(b)):
			out[i][j] = a[i] * b[j]

	return out


def neural_network(input, weights):
	pred = vect_mat_mul(input, weights)
	return pred


weights = [
			[0.1, 0.1, -0.3],
			[0.1, 0.2, 0.0],
			[0.0, 1.3, 0.1]
]

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

hurt = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

alpha = 0.01

input = [toes[0], wlrec[0], nfans[0]]
true = [hurt[0], win[0], sad[0]]

for iter in range(3):

	pred = neural_network(input, weights)

	error = [0, 0, 0]
	delta = [0, 0, 0]

	for i in range(len(true)):
		error[i] = (pred[i] - true[i]) ** 2
		delta[i] = pred[i] - true[i]

	weight_deltas = outer_product(input, delta)

	print("Iteration: " , str(iter+1))
	print("Pred: " , str(pred))
	print("Error: " , str(error))
	print("Delta: " , str(delta))
	print("Weights: " , str(weights))
	print("Weight_Deltas: ")
	print(str(weight_deltas))
	print()

	for i in range(len(weights)):
		for j in range(len(weights[0])):
			weights[i][j] -= alpha * weight_deltas[i][j]