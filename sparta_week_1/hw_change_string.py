input = "011110"
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    i = 0
    #make all zero
    zero_count = 0
    one_count = 0

    while i < len(string):
        if string[i] =='1':
            zero_count +=1
            for j in range(i,len(string)):
                if string[j]=='1':
                    i = j
                else:
                    break
        i +=1
    i = 0
    #make all one
    while i < len(string):
        if string[i] =='0':
            one_count +=1
            for j in range(i,len(string)):
                if string[j]=='0':
                    i = j
                else:
                    break
        i +=1
    return min(zero_count,one_count)
result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)