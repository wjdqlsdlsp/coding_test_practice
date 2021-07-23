def solution(phone_book):
    phone_book.sort()
    for prev, next in zip(phone_book,phone_book[1:]):
        if next.startswith(prev):
            return False
    return True

print(solution(["119", "97674223", "1195524421","34223423","35353"]))