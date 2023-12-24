def magic_index_1(data):
    #data is sorted and distint, dind i where A[i] = i

    def magic_bin_search(start, last, data):
        if start > last:
            return None

        middle = (start + last) // 2
        middle_v = data[middle]

        #end condition
        if middle_v == middle:
            return middle
        if start == last:
            return None

        if middle < middle_v:
            possible_result = magic_bin_search(start, middle - 1, data)

            # only if not distinct values
            # if possible_result is None:
            #     possible_result = magic_bin_search(middle_v, last)
        else:
            possible_result = magic_bin_search(start, middle_v - 1, data)
            if possible_result is None:
                possible_result = magic_bin_search(middle + 1, last, data)

        return possible_result

    result = magic_bin_search(0, len(data) - 1, data)
    print(data)
    print('data[', result, '] =', result)
    print('='*100)

data = [i for i in range(17)]
print(magic_index_1(data))

data = [-3,-2,-1,0,2,4,6,10,11,12]
print(magic_index_1(data))

data = [i-2 for i in range(17)]
print(magic_index_1(data))

data = [i+2 for i in range(17)]
print(magic_index_1(data))

data = [i-2 for i in range(17)]
data.extend([16,18,19])
print(magic_index_1(data))

data = [i+2 for i in range(17)]
data.insert(0, 0)
print(magic_index_1(data))


