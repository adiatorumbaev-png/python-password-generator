import sys
sys.path.insert(0, "src")
from main import generate_password, check_strength, generate_many, filter_by_strength
 
 
def test_length():
    assert len(generate_password(10)) == 10
 
 
def test_strength():
    assert check_strength("abc") == "weak"
    assert check_strength("Abcdef1!") == "strong"


def test_generate_many():
    passwords = generate_many(5, 8)
    assert len(passwords) == 5
    assert all(len(p) == 8 for p in passwords)


def test_filter_by_strength():
    assert filter_by_strength(["abc", "Abcdef1!"], "strong") == ["Abcdef1!"]
