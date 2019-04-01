def rotateString(original_s, new_s):
    if len(original_s) != len(new_s):
        return False
    return original_s in 2 * new_s