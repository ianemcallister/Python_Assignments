import re

# Read the input from the 'source.txt' file
with open('source.txt', 'r') as file:
    input_string = file.read()

# List of words to ignore
ignore_words = ["Skill", "Resume", "Job Description"]

# Split the input string into lines
lines = input_string.splitlines()

# Initialize a list to hold the keywords
keywords = []

# Iterate over the lines
for line in lines:
    # Remove leading/trailing whitespace
    line = line.strip()
    
    # If the line is a number or in the ignore list, skip it
    if line.isdigit() or line in ignore_words:
        continue
    
    # Add the valid line to the keywords list
    if line:  # Check to avoid adding empty lines
        keywords.append(line)

# Output the list of keywords
print(keywords)
