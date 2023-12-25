def print_hanoi(stacks):
    max_h = max([len(stacks[0]), len(stacks[1]), len(stacks[2])])
    for i in range(max_h -1 , -1, -1):
        v1, v2, v3 = ' ',' ',' '
        if i < len(stacks[0]):
            v1 = stacks[0][i]
        if i < len(stacks[1]):
            v2 = stacks[1][i]
        if i < len(stacks[2]):
            v3 = stacks[2][i]
        print('[',v1,']',end=' ')
        print('[',v2,']',end=' ')
        print('[',v3,']')
    print('='*50)

def move_disk(src, dest, disk, stacks):
    if stacks[src][-1] == disk:
        stacks[src].pop()
        stacks[dest].append(disk)
        print_hanoi(stacks)
    else:
        #pick somehow the dest
        all_dests = [0,1,2]
        all_dests.remove(src)
        all_dests.remove(dest)
        other_dest = all_dests[0]

        move_disk(src, other_dest, disk - 1, stacks)
        move_disk(src, dest, disk, stacks)
        move_disk(other_dest, dest, disk - 1, stacks)

def run_hanoi(n):
    stacks = [[i for i in range(n , 0, -1)],[],[]]

    print_hanoi(stacks)
    move_disk(0,2,n, stacks)

run_hanoi(4)