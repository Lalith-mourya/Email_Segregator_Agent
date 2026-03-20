import math
class AgentMemory:
    def __init__(self):
        self.spam_words = {}
        self.ham_words = {}
        self.total_spam_words = 0
        self.total_ham_words = 0

    def update_memory(self, words, label):
            for word in words:
                if label == 1:
                    self.spam_words[word] = self.spam_words.get(word, 0) + 1
                    self.total_spam_words += 1
                else:
                    self.ham_words[word] = self.ham_words.get(word, 0) + 1
                    self.total_ham_words += 1

    def check_words(self, words):
            spam_score = 0
            ham_score = 0

        ## P(word∣spam)=spam_count(word)/total_spam_words

            for word in words:
                spam_prob = self.spam_words.get(word, 0) / self.total_spam_words if self.total_spam_words > 0 else 0
                ham_prob = self.ham_words.get(word, 0) / self.total_ham_words if self.total_ham_words > 0 else 0

            if spam_prob > 0:
                spam_score += math.log(spam_prob)

            if ham_prob > 0:
                ham_score += math.log(ham_prob)

            return spam_score, ham_score
