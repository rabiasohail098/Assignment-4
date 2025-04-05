import os
from src.text_preprocessing import preprocess_text
from src.markov_model import build_markov_chain
from src.poetry_generator import generate_poetry

# Poetry Dataset Load Karna
data_folder = "data"
poetry_files = ["ghalib_poetry.txt", "iqbal_poetry.txt"]
text_data = ""

for file in poetry_files:
    with open(os.path.join(data_folder, file), "r", encoding="utf-8") as f:
        text_data += f.read() + "\n"

# Process poetry
words = preprocess_text(text_data)
markov_chain = build_markov_chain(words, order=2)

# AI Poetry Generate Karo
new_poetry = generate_poetry(markov_chain, length=15)
print("✨ AI-Generated Poetry ✨\n", new_poetry)
print("\n\n")