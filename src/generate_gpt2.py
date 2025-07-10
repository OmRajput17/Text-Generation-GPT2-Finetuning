# ✅ src/generate_gpt2.py
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

def generate_text(prompt):
    tokenizer = AutoTokenizer.from_pretrained("models/gpt2-pride-model")
    model = AutoModelForCausalLM.from_pretrained("models/gpt2-pride-model")
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    result = generator(prompt, max_new_tokens=100, temperature=1.0, top_k=50, top_p=0.95)
    return result[0]['generated_text']