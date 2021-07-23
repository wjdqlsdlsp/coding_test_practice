def make_charts(genres, plays):
    chart_dict = {}
    chart_dict_index = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre not in chart_dict:
            chart_dict[genre] = play
            chart_dict_index[genre] = [[i,play]]
        else:
            chart_dict[genre] += play
            chart_dict_index[genre].append([i,play])

    chart_dict = sorted(chart_dict.items(), key = lambda item: item[1], reverse=True)
    result = []
    for i in range(len(chart_dict)):
        tmp = chart_dict_index[chart_dict[i][0]]
        tmp = sorted(tmp, key = lambda x : x[1], reverse=True)
        for j in range(min(len(tmp),2)):
            result.append(tmp[j][0])
    return result
# 1
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(make_charts(genres, plays))
# 정답 = [4, 1, 3, 0]


# 2
genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]
print(make_charts(genres, plays))
# 정답 = [0, 6, 5, 2, 4, 1]