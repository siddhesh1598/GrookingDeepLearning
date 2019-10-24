def neural_network(input, weights):
	out = 0

	for i in range(len(input)):
		out += (input[i] * weights[i])

	return out

def ele_mul(scalar, vector):
	out = [0, 0, 0]

	for i in range(len(out)):
		out[i] = scalar * vector[i]

	return out

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.9, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

win_or_lose_binary = [1, 1, 0, 1]
true = win_or_lose_binary[0]

weights = [0.1, 0.2, -.1]
alpha = 0.01
input = [toes[0],wlrec[0],nfans[0]]

for iter in range(3):

	pred = neural_network(input,weights)

	error = (pred - true) ** 2
	delta = pred - true

	weight_deltas = ele_mul(delta,weights)
	weight_deltas[0] = 0

	print("Iteration: " , str(iter+1))
	print("Pred: " , str(pred))
	print("Error: " , str(error))
	print("Delta: " , str(delta))
	print("Weights: " , str(weights))
	print("Weight_Deltas: ")
	print(str(weight_deltas))
	print()

	for i in range(len(weights)):
		weights[i] -= alpha * weight_deltas[i]

