import numpy as np

"""Working with Docker - The basics."""

print("Hello world from Docker!")

a = np.array([[1, 2, 3], [4, 5, 6]])

print(f"Shape of a: {a.shape}")

print(dir(np))

# 1. make a Dockerfile
# 2. Docker build
# 3. Docker run
