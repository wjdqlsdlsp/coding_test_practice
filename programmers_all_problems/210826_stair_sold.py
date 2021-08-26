def solution(enroll, referral, seller, amount):
    money = {}
    for name in enroll:
        money[name] = 0
    en_re = {}
    for en, re in zip(enroll,referral):
        en_re[en] = re

    for index, sell in enumerate(seller):
        price = amount[index] * 100
        next_name = sell
        while next_name != '-' and price !=0:
            my_money = price - price // 10
            money[next_name] += my_money
            price = price //10
            next_name = en_re[next_name]

    return list(money.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))