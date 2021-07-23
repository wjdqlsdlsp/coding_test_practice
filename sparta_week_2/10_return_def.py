input = "dabcbad"


def is_palindrome(string):
    if len(string) < 2:
        print(True)
        return
    if string[0] == string[-1]:
        is_palindrome(string[1:-1])

    else:
        print(False)
        return

is_palindrome(input)