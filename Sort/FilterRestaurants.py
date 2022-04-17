# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
# Time complexity | Space complexity

def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    finals = []
    for res in restaurants:
        if veganFriendly:
            if res[2] and res[3] <= maxPrice and res[4] <= maxDistance:
                finals.append(res)
        else:
            if res[3] <= maxPrice and res[4] <= maxDistance:
                finals.append(res)

    finals.sort(key=lambda x: [-x[1], -x[0]])
    return [res[0] for res in finals]


print(filterRestaurants(restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [
      4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], veganFriendly=1, maxPrice=50, maxDistance=10))

# Expected output: [3,1,5] 

