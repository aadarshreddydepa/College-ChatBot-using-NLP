import json
import nltk
from nltk.tokenize import word_tokenize

# Load knowledge base
with open("college_data.json", "r") as file:
    knowledge_base = json.load(file)

def get_response(user_input):
    user_tokens = word_tokenize(user_input.lower())
    best_match = None
    max_overlap = 0

    for category, data in knowledge_base.items():
        for question in data["questions"]:
            question_tokens = word_tokenize(question.lower())
            overlap = len(set(user_tokens).intersection(set(question_tokens)))
            if overlap > max_overlap:
                max_overlap = overlap
                best_match = category

    if best_match and max_overlap > 0:
        return knowledge_base[best_match]["answer"]
    else:
        return "Sorry, I didn't understand that. Please ask a different question."
