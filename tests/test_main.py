import sys
sys.path.insert(0, "src")
from main import generate_password, check_strength
 
 
def test_length():
    assert len(generate_password(10)) == 10
 
 
def test_strength():
    assert check_strength("abc") == "weak"
    assert check_strength("Abcdef1!") == "strong"
