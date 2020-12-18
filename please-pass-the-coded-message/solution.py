import itertools

def get_permutations(l):
    for n in range(1, len(l)+1):
        for permutation in itertools.permutations(l, n):
            value = 0
            for digit in permutation:
                value = value * 10 + digit
            yield value

def solution(l):
    return max(p for p in get_permutations(l) if p % 3 == 0)
    