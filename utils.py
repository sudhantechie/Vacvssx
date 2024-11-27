
def validate_score(s):
    if 0 <= s <= 10:
        return True
    raise ValueError("Score must be between 0 and 10.")
