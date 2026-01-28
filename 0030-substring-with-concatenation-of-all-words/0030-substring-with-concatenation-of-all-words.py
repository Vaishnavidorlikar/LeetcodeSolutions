from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_length):
            left = i
            count = 0
            current_count = defaultdict(int)

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j:j+word_length]

                if word in word_count:
                    current_count[word] += 1
                    count += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left+word_length]
                        current_count[left_word] -= 1
                        left += word_length
                        count -= 1

                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left+word_length]
                        current_count[left_word] -= 1
                        left += word_length
                        count -= 1
                else:
                    current_count.clear()
                    count = 0
                    left = j + word_length

        return result
