from transformers import pipeline

# Load the AI model
sentiment_analyzer = pipeline("sentiment-analysis")

print("=== AI Sentiment Analyzer ===")
print("Type 'exit' to quit.\n")

while True:
    text = input("Enter a sentence: ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    result = sentiment_analyzer(text)[0]

    print("\nResult:")
    print(f"Sentiment : {result['label']}")
    print(f"Confidence: {result['score']:.2%}")

    if result["label"] == "POSITIVE":
        print("😊 Positive")
    else:
        print("😞 Negative")

    print("-" * 40)