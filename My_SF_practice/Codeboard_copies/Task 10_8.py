import numpy as np
def any_normal(*vectors):
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            if np.dot(vectors[i],vectors[j]) == 0:
                return True
    return False

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

print(any_normal(vec1, vec2, vec3))
    