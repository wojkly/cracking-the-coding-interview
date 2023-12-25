def permutations_with_dups_rec(permutation: list, charset: set):
    if len(permutation) == len(charset):
        print(permutation)
    else:
        for char in charset:
            permutation.append(char)
            permutations_with_dups_rec(permutation, charset)
            permutation.pop()

def permutations_with_dups(s: str):
    permutations_with_dups_rec([], set(s))

permutations_with_dups('123')