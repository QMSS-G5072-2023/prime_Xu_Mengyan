# +
import math

def is_prime(n):
    """
    Determine if a number is prime.

    This function checks if a given number is prime. A number is considered prime if it 
    is greater than 1 and has no divisors other than 1 and itself.

    Parameters:
    - n (int): The number to check.

    Returns:
    - bool: True if n is prime, False otherwise.

    Example:
    >>> is_prime(5)
    True

    >>> is_prime(4)
    False
    """
    
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# -




