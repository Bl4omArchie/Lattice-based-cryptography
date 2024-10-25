import math

#scalar multiplication: vector1 * int1 = vector2
def scalar_multiplication(vect_a: list, b: int):
    res = []
    for element in vect_a:
        res.append(element * b)
    return res


#vector addition: vector1 + vector2 = vector3
def vector_addition(vect_a: list, vect_b: list):
    res = []
    for i in range(len(vect_a)):
        res.append((vect_a[i] + vect_b[i]))
    return res


#vector substraction: vector1 - vector2 = vector3
def vector_substraction(vect_a: list, vect_b: list):
    res = []
    for i in range(len(vect_a)):
        res.append((vect_a[i] - vect_b[i]))
    return res


#dot product: vector * vector = scalar
def dot_product(vect_a: list, vect_b: list):
    assert(len(vect_a) == len(vect_b)), "Error: vector a and b should have equal len"
    
    res = 0
    for i in range(len(vect_a)):
        res += (vect_a[i] * vect_b[i])
    return res


#return the magnitude of a vector
def compute_magnitude(vect_a: list):
    return math.sqrt(dot_product(vect_a, vect_a))


# Grand Schmidt algorithm : from the given list of vectors, it return an orthogonal basis
def gran_schmidt_orthogonal_basis(vectors: list):
    u = []
    phi = [[]]
    u.append(vectors[0])

    for i in range(1, len(vectors)-1):
        for j in range(i-1):
            phi[i][j] = dot_product(vectors[i], u[j]) / compute_magnitude(u)
        
        u[i] = sum(scalar_substraction(vectors[i], scalar_multiplication(phi[i][j], u[j])) for j in range(i-1))
    return u


if __name__ == "__main__":
    a = [2,6,3]
    b = [1,4,2]
    c = [7,7,2]
    s = 5

    assert(vector_addition(a, b) == [3, 10, 5]), "Error : vector addition"
    assert(vector_substraction(a, b) == [1, 2, 1]), "Error : vector substraction"
    assert(scalar_multiplication(a, s) == [10, 30, 15]), "Error : scalar multiplication"
    assert(dot_product(a, b) == 32), "Error : dot product"
    print ("Test completed !")