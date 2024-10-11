# Define dependencies
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')

# Set up OpenAI API credentials
openai.api_key = OPEN_AI_API_KEY

# Get user input for raw data
raw_data = input('Enter raw data: ')

# Generate the response using ChatGPT model
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # System message to set the assistant's behavior
        {"role": "user", "content": raw_data}  # User input as the chat message
    ],
    max_tokens=50,  # Limit the response length
    temperature=0.7,  # Adjust the creativity/randomness of the response
    n=1  # Number of completions to generate
)

# Get the generated output from the API response
generated_output = response.choices[0].text.strip()

# Print the generated output
print('Generated Output:')
print(generated_output)
