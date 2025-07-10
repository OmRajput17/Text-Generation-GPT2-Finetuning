# GPT-2 Fine-Tuned Text Generator

This project fine-tunes GPT-2 on *Pride and Prejudice* to generate original literary-style text in the tone of Jane Austen.

## Project Structure
```
textgen_gpt2/
├── src/
│   ├── train_gpt2.py          # Fine-tuning script
│   ├── generate_gpt2.py       # Text generation script
│   └── utils/data_loader.py   # Data fetch & chunking
├── models/gpt2-pride-model/   # Saved model & tokenizer
├── main.py                    # Run this to generate
├── requirements.txt
└── README.md
```

## How to Use
```bash
# Install dependencies
pip install -r requirements.txt

# Train (if not already trained)
python src/train_gpt2.py

# Generate
python main.py
```

## Sample Prompt
```
"As the carriage rolled through the rain, Elizabeth looked at Darcy and said"
```

## 📜 Sample Output
> Elizabeth looked at Darcy and said, “I do believe, sir, that you intend to leave without telling me the truth.”
