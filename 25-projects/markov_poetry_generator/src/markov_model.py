import random

def build_markov_chain(words, order=2):
    markov_chain = {}

    for i in range(len(words) - order):
        key = tuple(words[i:i+order])
        next_word = words[i+order]

        if key not in markov_chain:
            markov_chain[key] = []
        
        markov_chain[key].append(next_word)

    return markov_chain
