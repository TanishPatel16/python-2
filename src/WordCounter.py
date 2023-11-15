class WordCounter:

    def __init__(self, sentence):
        self.sentence = sentence
        self.word_count = 0
        self.shortest_word_len = 0
        self.longest_word_len = 0

    def count_words(self):
         words = self.sentence.split(" ")
         words.sort(key = lambda p : len(p))
         self.word_count = len(words)
         self.shortest_word_len = len(words[0])
         self.longest_word_len = len(words[-1])

    def get_word_count(self):
        return self.word_count

    def get_shortest_word(self):
        return self.shortest_word_len
    def get_longest_word(self):
        return self.longest_word_len

