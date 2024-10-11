import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = 'gpt2-medium' # Use a smaller model varient
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Generate response using GPT-2
def generate_response(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors='pt').to(device)
    output = model.generate(input_ids, max_length=60, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Chat Loop
while True:
    user_input = input('Enter your message: ')
    if user_input.lower() == 'exit':
        break
    
    response = generate_response(user_input)
    print('ChatGPT:', response)