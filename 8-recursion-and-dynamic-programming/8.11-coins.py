def count_ways(coins: list[int], sum: int) -> int:
    ways = [0 for i in range(sum + 1)]
    ways[0] = 1
    
    for i in range(sum):
        for coin in coins:
            if i + coin <= sum:
                ways[i + coin] += ways[i]
                
    print(ways)
    
    return ways[sum]


coins = [25,10,5,1]

print(count_ways(coins, 100))