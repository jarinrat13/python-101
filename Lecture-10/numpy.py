<<<<<<< HEAD
import numpy as np

random_matrix = np.random.randint(1, 11, size=(3, 3))
print("Random 3x3 Matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nSum od all elements: {matrix_sum}")

transposed_matrix = np.transpose(random_matrix)
=======
import numpy as np

random_matrix = np.random.randint(1, 11, size=(3, 3))
print("Random 3x3 Matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nSum od all elements: {matrix_sum}")

transposed_matrix = np.transpose(random_matrix)
>>>>>>> 36e2367c506c94705546caf13817ba0e32d9cbfa
print("\nTransposed Martix:\n", transposed_matrix)