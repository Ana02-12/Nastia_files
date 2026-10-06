def lengthOfLastWord(s: str) -> int:
    end = len(s) - 1

    while s[end] == " ":
        end -= 1

    start = end
    #для обработки строк содержащих
    #только одно слово l может стать -1
    while start >= 0 and s[start] != " ":
        start -= 1

    return end - start
