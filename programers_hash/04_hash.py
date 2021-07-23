genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    genre_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dict.keys():
            genre_dict[genres[i]] = plays[i]
        else:
            genre_dict[genres[i]] += plays[i]
    genre_dict = sorted(genre_dict.items(), key=lambda item: item[1], reverse=True)

    dict_pr ={}
    for i in range(len(genres)):
        if genres[i] not in dict_pr.keys():
            dict_pr[genres[i]] = [(i,plays[i])]
        else:
            dict_pr[genres[i]].append((i,plays[i]))
    
    answer = []
    for genre, play in genre_dict:
        tmp = sorted(dict_pr[genre], key = lambda x : x[1], reverse=True)
        for i in range(min(2, len(tmp))):
            answer.append(tmp[i][0])

    return answer

print(solution(genres,plays))