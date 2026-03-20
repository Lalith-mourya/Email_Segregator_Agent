from agent import SpamModelBasedAgent

agent = SpamModelBasedAgent("models/spam_model.pkl")

subject = input("Enter email subject: ")

prediction, source = agent.predict(subject)

if prediction == 1:
    print(f"Prediction: SPAM (via {source})")
else:
    print(f"Prediction: HAM (via {source})")
