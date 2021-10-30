def solution(n, arr1, arr2):
    answer = []


    for a,b in zip(arr1,arr2):
        bin_a = list(bin(a))[2:]
        bin_b = list(bin(b))[2:]
        bin_a = ["0"] * (n - len(bin_a)) + bin_a
        bin_b = ["0"] * (n - len(bin_b)) + bin_b

        tmp = ["#" if (a_i == "1") or (b_i == "1") else " " for a_i, b_i in zip(bin_a, bin_b)]
        answer.append("".join(tmp))

    # rjust 이용하기
    # for a,b in zip(arr1,arr2):
    #     bin_a = str(bin(a))[2:]
    #     bin_b = str(bin(b))[2:]
    #     bin_a = bin_a.rjust(n, "0")
    #     bin_b = bin_b.rjust(n, "0")

    #     tmp = ["#" if (a_i == "1") or (b_i == "1") else " " for a_i, b_i in zip(bin_a, bin_b)]
    #     answer.append("".join(tmp))

    return answer
print(solution(5, 	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))