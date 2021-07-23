import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

def get_min_city_chicken_distance(n, m, city_map):
    house_position = []
    chicken_position = []
    for i in range(len(city_map)):
        for j in range(len(city_map[0])):
            if city_map[i][j] == 1:
                house_position.append([i+1,j+1])
            if city_map[i][j] == 2:
                chicken_position.append([i+1,j+1])

    min_distance = sys.maxsize
    chicken_position_selection = list(itertools.combinations(chicken_position,m))
    for case in range(len(chicken_position_selection)):
        distance = [sys.maxsize] * len(house_position)
        for house_num in range(len(house_position)):
            for chicken_num in range(len(chicken_position_selection[case])):
                x = house_position[house_num][0] - chicken_position_selection[case][chicken_num][0]
                y = house_position[house_num][1] - chicken_position_selection[case][chicken_num][1]
                distance_value = abs(x) + abs(y)
                if distance_value < distance[house_num]:
                    distance[house_num] = distance_value
        if min_distance > sum(distance):
            min_distance = sum(distance)
    return min_distance

city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))