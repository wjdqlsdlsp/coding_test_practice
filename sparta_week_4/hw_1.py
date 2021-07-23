import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 15, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    heap = []

    for day in range(1, k+1):
        if day in dates:
            heapq.heappush(heap, supplies[dates.index(day)] * -1)

        if stock == 0:
            tmp = (heapq.heappop(heap) * -1)
            stock += tmp
            answer += 1

        stock -=1

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))