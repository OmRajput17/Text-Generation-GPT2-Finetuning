from src.generate_gpt2 import generate_text

if __name__ == "__main__":
    prompt = "As the carriage rolled through the rain, Elizabeth looked at Darcy and said that"
    output = generate_text(prompt)
    print("\n Generated Text:\n")
    print(output)
