def elementwise_multiplication(vec_a, vec_b):
	result = []
	for i in range(len(vec_a)):
		result.append(vec_a[i] * vec_b[i])

	return result


def elementwise_addition(vec_a, vec_b):
	result = []
	for i in range(len(vec_a)):
		result.append(vec_a[i] + vec_b[i])

	return result


def vector_sum(vec_a):
	return sum(vec_a)


def vector_average(vec_a):
	return (sum(vec_a)/len(vec_a))


def dot_product(vec_a, vec_b):
	vec_c = elementwise_multiplication(vec_a, vec_b)
	ans = vector_sum(vec_c)
	return ans