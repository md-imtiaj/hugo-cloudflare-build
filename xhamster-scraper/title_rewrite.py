import random
import synonyms_list as sl

# Define the synonyms dictionary
synonyms = sl.synonyms

# Function to match the case of the original word
def match_case(word, template):
    if template.isupper():
        return word.upper()
    elif template.islower():
        return word.lower()
    elif template.istitle():
        return word.capitalize()
    else:
        return word

# Function to convert a sentence by replacing words with random synonyms
def convert_sentence(sentence, synonyms):
    words = sentence.split()
    new_words = []
    
    for word in words:
        # Extract the lowercased word for dictionary lookup
        word_lower = word.lower()
        
        # Check if the word exists in the synonyms dictionary
        if word_lower in synonyms:
            # Replace with a random synonym and match the original case
            new_word = random.choice(synonyms[word_lower])
            new_word = match_case(new_word, word)
            new_words.append(new_word)
        else:
            # If no synonym exists, keep the original word
            new_words.append(word)
    
    # Join the words back into a sentence
    return ' '.join(new_words)


# Example usage
#sentence = "Tattooed MILF Ryan Conner Gets Her Butthole Pounded Hard"
#new_sentence = convert_sentence(sentence, synonyms)
#print(new_sentence)
