import random
def generate_poetry(markov_chain, length=10):
    start_key = random.choice(list(markov_chain.keys()))
    generated_words = list(start_key)

    for _ in range(length):
        key = tuple(generated_words[-2:])
        if key in markov_chain:
            next_word = random.choice(markov_chain[key])
            generated_words.append(next_word)
        else:
            break

    return " ".join(generated_words)
