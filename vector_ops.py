# Vector Analysis Toolkit
# This module provides functions for vector operations

def add_vectors(v1, v2):
    """Add two vectors of the same length."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    return [a + b for a, b in zip(v1, v2)]

def subtract_vectors(v1, v2):
    """Subtract v2 from v1."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    return [a - b for a, b in zip(v1, v2)]

def scalar_multiply(v, scalar):
    """Multiply a vector by a scalar."""
    return [scalar * x for x in v]

def dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    return sum(a * b for a, b in zip(v1, v2))

def cross_product(v1, v2):
    """Calculate the cross product of two 3D vectors."""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product is only defined for 3D vectors")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

def magnitude(v):
    """Calculate the magnitude (length) of a vector."""
    return (sum(x * x for x in v)) ** 0.5

# Example usage (for testing)
if __name__ == "__main__":
    # Test the functions
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    
    print("Addition:", add_vectors(v1, v2))  # [5, 7, 9]
    print("Subtraction:", subtract_vectors(v1, v2))  # [-3, -3, -3]
    print("Scalar Multiply:", scalar_multiply(v1, 2))  # [2, 4, 6]
    print("Dot Product:", dot_product(v1, v2))  # 32
    print("Cross Product:", cross_product(v1, v2))  # [-3, 6, -3]
    print("Magnitude of v1:", magnitude(v1))  # ~3.74