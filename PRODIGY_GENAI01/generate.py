from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

model_dir = "./gpt2-finetuned"
tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
model = GPT2LMHeadModel.from_pretrained(model_dir)

prompt = input("Enter your prompt: ")
inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(**inputs, max_length=100, do_sample=True, top_k=50)

print("\nGenerated text:\n")
print(tokenizer.decode(output[0], skip_special_tokens=True))
