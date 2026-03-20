import pickle
from preprocessing import preprocess_text
from memory import AgentMemory

class SpamModelBasedAgent:

    def __init__(self, model_path):
        with open(model_path, 'rb') as f:
            self.model, self.vectorizer = pickle.load(f)

        self.memory = AgentMemory()

    def rule_based_decision(self, words):
        spam_score, ham_score = self.memory.check_words(words)

        if spam_score > ham_score:
            return 1
        elif ham_score > spam_score:
            return 0
        else:
            return None


    def ml_decision(self, text):
        vector = self.vectorizer.transform([text])

        prediction = self.model.predict(vector)[0]
        probabilities = self.model.predict_proba(vector)[0]

        confidence = probabilities[prediction] * 100

        return prediction, confidence



    def predict(self, subject):

        words = preprocess_text(subject)

    #  Rule-based attempt
        rule_result = self.rule_based_decision(words)

        if rule_result is not None:
            return rule_result, "Rule-Based Memory"

    # ML 
        processed_text = " ".join(words)
        ml_result, confidence = self.ml_decision(processed_text)

    # Update memory
        self.memory.update_memory(words, ml_result)

        return ml_result, f"ML Model ({confidence:.2f}% confidence)"

