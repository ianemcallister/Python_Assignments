# Define dependencies
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')

client = OpenAI(
    api_key = OPEN_AI_API_KEY
)

# Get user input for raw data
raw_data = input('Enter raw data: ')

# Preprocess the data (example: converting to lower case)
processed_data = raw_data.lower()

# Perform API call for data processing
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": processed_data
        }
    ],
    model='gpt-3.5-turbo',
)

# Get the generated output from the API response
generated_output = chat_completion.choices[0].message.content.strip()

# Print the generated output
print('Generated Output:')
print(generated_output)