def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    start = 0
    end = -1
    mid = len(word) // 2
    for _ in range(0, mid):
        if word[start] != word[end]:
            return False
        start += 1
        end += -1
    return True
