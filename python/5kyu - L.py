# Link -> https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    anagram_list = []

    for anagram in words:
        if sorted(list(word)) == sorted(list(anagram)):
            anagram_list.append(anagram)

    return anagram_list
