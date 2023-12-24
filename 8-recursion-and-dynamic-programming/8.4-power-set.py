def print_all_subsets_rec(subset: list, data: set):
    if not data:
        print(subset)
        return

    new_value = data.pop()

    #subset without element
    print_all_subsets_rec(subset, data)

    #subset with element
    subset.append(new_value)
    print_all_subsets_rec(subset, data)
    subset.pop()
    data.add(new_value)


def print_all_subsets(data: list):
    print('all subsets of:', data)
    print_all_subsets_rec([], set(data))
    print('='*200)

data = []
print_all_subsets(data)
data = [1]
print_all_subsets(data)
data = [1,2,3,4]
print_all_subsets(data)