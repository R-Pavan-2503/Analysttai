import nltk
import random
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.sentiment import SentimentIntensityAnalyzer

# Package download

"""
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')
"""

#  responses
responses = {
    "greetings": ["Hello! I am an humours chatbot ", "Hi there!  I am an humours chatbot ", "Hey! I am an humours chatbot"],
    "farewell": ["Goodbye!", "Bye!", "See you later!", "Take care!"],
    "age": ["I'm just a chatbot, I don't have an age.", "Age is just a number for me!" , "I just born now !!!"],
    "weather": ["I'm not sure about the weather. You can check online . Just a joke !! ."],
    "thank_you": ["You're welcome!", "Anytime!", "Glad I could help!"],
    "name": ["I don't have a name. You can call me JARVIS as of in the movie IronMan !!!.", "I'm Alien, nice to meet you!"],
    "location": ["I'm present in Mars , wanna come over ? ", "I am located inside your computer system !!!"],
    "appreciation" : [" Thank you !!!" , " It was a nice joke right ? "],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "Sorry, I didn't get that."],

}

#  patterns
patterns = [
    (r"hi|hello|hey", "greetings"),
    (r"bye|goodbye", "farewell"),
    (r"how old are you", "age"),
    (r"what is the weather ?", "weather"),
    (r"thank you", "thank_you"),
    (r"what(?:.*)name(?:.*)", "name"),
    (r"where are you from|where are you located", "location"),
    (r"haha|good joke", "appreciation")
]

# Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def chatbot():
    print("Hi, I'm Chatbot! How can I assist you today?")


    def respond(message):
        tokens = word_tokenize(message)
        tagged_tokens = pos_tag(tokens)

        # NER
        named_entities = ne_chunk(tagged_tokens)

        # Sentiment Analysis
        sentiment_score = sia.polarity_scores(message)
        sentiment = "neutral"
        if sentiment_score['compound'] > 0.2:
            sentiment = "positive"
        elif sentiment_score['compound'] < -0.2:
            sentiment = "negative"

        for pattern, response_key in patterns:
            if nltk.re.search(pattern, message):
                if response_key == "default":
                    return random.choice(responses[response_key])
                elif response_key == "location":
                    return random.choice(responses[response_key])
                elif response_key == "greetings":
                    if sentiment == "positive":
                        return random.choice(["Hello! Glad to see you're in a good mood!", "Hi there! Feeling positive today?"])
                    elif sentiment == "negative":
                        return random.choice(["Hello! Is everything alright?", "Hi there! Anything bothering you?"])
                    else:
                        return random.choice(responses[response_key])
                else:
                    return random.choice(responses[response_key])

        return random.choice(responses["default"])


    chat = Chat([], reflections)
    chat.respond = respond
    chat.converse()

# Run
if __name__ == "__main__":
    chatbot()