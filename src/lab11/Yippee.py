import random
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set device to use GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Generate an encouraging message
def generate_encouragement():
    prompt = "I believe you can make it to the destination city"
    encoded_prompt = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
    encoded_prompt = encoded_prompt.to(device)

    # Generate text using the model
    output_sequences = model.generate(
        input_ids=encoded_prompt,
        max_length=50,
        temperature=1.0,
        top_k=0,
        top_p=0.9,
        do_sample=True,
        num_return_sequences=1,
    )

    # Decode the generated text
    generated_sequence = output_sequences[0].tolist()
    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)
    return text.strip()

print(generate_encouragement())