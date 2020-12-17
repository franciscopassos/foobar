def convert_char(c):
    if ord('a') <= ord(c) <= ord('z'):
        return chr(ord('z') - ord(c) + ord('a'))
    return c

def solution(x):
    return ''.join(convert_char(c) for c in x)