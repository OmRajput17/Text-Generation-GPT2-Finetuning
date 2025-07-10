# ✅ src/train_gpt2.py
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from src.utils.data_loader import load_gutenberg_text

def train():
    dataset = load_gutenberg_text()
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token

    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=128)

    tokenized_dataset = dataset.map(tokenize, batched=True)
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    model.resize_token_embeddings(len(tokenizer))

    training_args = TrainingArguments(
        output_dir="models/gpt2-pride-model",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        logging_dir="logs",
        save_strategy="epoch"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        tokenizer=tokenizer
    )
    trainer.train()
    model.save_pretrained("models/gpt2-pride-model")
    tokenizer.save_pretrained("models/gpt2-pride-model")

if __name__ == "__main__":
    train()