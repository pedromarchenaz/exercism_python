def find_anagrams(word, candidates):

    def anagram(word_1, word_2):
        w_1 = word_1.lower()
        w_2 = word_2.lower()
        return sorted(w_1) == sorted(w_2) and w_1 != w_2

    return [i for i in candidates
            if anagram(word, i)]
