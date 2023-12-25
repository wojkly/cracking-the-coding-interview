def parens_rec(result: list[str], opened: int, to_open: int):
    if opened == 0 and to_open == 0:
        print(''.join(result))
    else:
        if to_open > 0:
            result.append('(')
            parens_rec(result, opened + 1, to_open - 1)
            result.pop()
        if opened > 0:
            result.append(')')
            parens_rec(result, opened - 1, to_open)
            result.pop()


def parens(n: int):
    parens_rec([], 0, n)

parens(4)