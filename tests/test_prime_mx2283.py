from prime_mx2283 import is_prime

# +
import pytest

def test_is_prime():
    # Test prime numbers
    assert is_prime(2) == True, "2 should be prime"
    assert is_prime(7) == True, "7 should be prime"
    assert is_prime(11) == True, "11 should be prime"
    
    # Test non-prime numbers
    assert is_prime(1) == False, "1 is not prime"
    assert is_prime(8) == False, "8 should not be prime"
    assert is_prime(9) == False, "9 should not be prime"
    
    # Test with zero and negative number
    assert is_prime(0) == False, "0 is not prime"
    assert is_prime(-7) == False, "-7 should not be prime, only positive integers can be prime"
# -

# !pytest test_prime_mx2283.py


