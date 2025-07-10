# ✅ src/utils/data_loader.py
import nltk
import requests
from datasets import Dataset
nltk.download('punkt')

def load_gutenberg_text():
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    raw = requests.get(url).text
    start = raw.lower().find("chapter 1")
    end = raw.lower().find("*** end of the project gutenberg")
    text = raw[start:end]
    sentences = nltk.sent_tokenize(text)
    chunks = [' '.join(sentences[i:i+5]) for i in range(0, len(sentences), 5)]
    return Dataset.from_dict({"text": chunks})