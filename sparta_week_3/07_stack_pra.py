top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    result = []
    while len(heights) > 0:
        top_h = top_heights.pop()
        index = 0
        for j in range(len(heights)):
            if top_h < heights[j]:
                index = j+1
        result.append(index)
    return result.reverse()

print(get_receiver_top_orders(top_heights))