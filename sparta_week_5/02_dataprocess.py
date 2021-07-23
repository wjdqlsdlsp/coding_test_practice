# aabbaccc -> 2a2ba3c

input = "abcabcabcabcdededededede"
# input = 'aaabac'


def string_compression(string):
    n = len(string)
    str_length = []
    for split_size in range(1, n//2+1):
        compressed =""
        split_list = [string[i:i+split_size] for i in range(0, n,split_size)]

        count = 1
        for i in range(1,len(split_list)):
            prev, cur = split_list[i-1], split_list[i]
            if prev == cur:
                count +=1
            else:
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += (str(count) + prev)
        else:
            compressed += cur
        str_length.append(len(compressed))
    return min(str_length)


print(string_compression(input))  # 14 가 출력되어야 합니다!

# print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
# print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
# print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))