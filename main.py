import nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')


# Preprocessing function
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text
    words = word_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    cleaned_text = ' '.join([word for word in words if word not in stop_words and word not in string.punctuation])

    return cleaned_text


# Function to classify the message
def classify_message(text):
    # Simple rule-based classification (you can replace this with an ML model later)
    spam_keywords = ['free', 'win', 'prize', 'click', 'claim']
    ham_keywords = ['hello', 'meeting', 'how', 'are', 'you', 'thanks']

    # Preprocess the input text
    processed_text = preprocess_text(text)

    # Check for spam keywords
    if any(keyword in processed_text for keyword in spam_keywords):
        return "spam"
    elif any(keyword in processed_text for keyword in ham_keywords):
        return "ham"
    else:
        return "unknown"


# Main function
def main():
    print("Email Spam Classifier")
    print("Enter a message to classify (or type 'exit' to quit):")

    while True:
        # Take user input
        user_input = input("Enter message: ")

        if user_input.lower() == 'exit':
            print("Exiting program.")
            break

        # Classify the message
        result = classify_message(user_input)

        # Output the result
        print(f"Message is classified as: {result}")


if __name__ == "__main__":
    main()
