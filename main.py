import csv
from textblob import TextBlob

# This is actual Python code!
def analyze_sentiment(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    if score > 0.1:
        return "Positive", "🟢"
    elif score < -0.1:
        return "Negative", "🔴"
    else:
        return "Neutral", "🟡"

print("--- CX Sentiment Report ---")
try:
    with open('feedback.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            status, emoji = analyze_sentiment(row['Feedback'])
            print(f"{emoji} [{status}] {row['Customer']}: {row['Feedback']}")
except FileNotFoundError:
    print("Error: feedback.csv not found!")