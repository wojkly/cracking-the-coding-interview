def permutations_without_dups_rec(permutation: list, charset: set):
    if not charset:
        print(permutation)
    else:
        for char in charset.copy():
            charset.remove(char)
            permutation.append(char)
            permutations_without_dups_rec(permutation, charset)
            permutation.pop()
            charset.add(char)

def permutations_without_dups(s: str):
    permutations_without_dups_rec([], set(s))

permutations_without_dups('123')