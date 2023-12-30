

def knapsack_rec(current_item: int, W: int, profits: list, weights: list, memo: list[list[int]]) -> int:
    if memo[current_item][W] is not None:
        return memo[current_item][W]
        
    #final condition
    if current_item < 0 or W == 0:
        return 0
    
    #cant take this item
    if weights[current_item] > W:
        res1 =  knapsack_rec(current_item - 1, W, profits, weights, memo)
        memo[current_item][W] = res1
        return res1
    
    # can take
    res1 = profits[current_item] + knapsack_rec(current_item - 1, W - weights[current_item], profits, weights, memo)
    # or not take
    res2 = knapsack_rec(current_item - 1, W, profits, weights, memo)
        
    res3 = max(res1, res2)
    memo[current_item][W] = res3
    return res3
    
def knapsack(W: int, profits: list, weights: list) -> int:
    memo = [[None for j in range(W + 1)] for i in range(len(weights))]
    res = knapsack_rec(len(profits) - 1, W, profits, weights, memo)
     
     
    print(res)
    
    
profits = [50, 19, 31, 31, 3, 16, 14, 29, 36, 39, 30, 6, 21, 20, 30, 34, 44, 27, 46, 43]
weights = [33, 3, 33, 11, 16, 0, 48, 18, 47, 0, 42, 46, 27, 3, 27, 39, 20, 9, 15, 2]
W = 300; 

knapsack(W, profits, weights)




# from random import randint
# print([randint(0,50) for _ in range(20)])
# print([randint(0,50) for _ in range(20)])