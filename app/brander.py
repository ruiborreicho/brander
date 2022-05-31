import os
import openai
import argparse
import re
from typing import List

def main():
    print("Running Brander")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User Input: {user_input}")
    branding_results = generate_branding_snippet(user_input)
    keywords_results = generate_keywords(user_input)

    print(branding_results)
    print(keywords_results)

def generate_branding_snippet(prompt: str) -> str:
    #Load the API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")

    enriched_prompt=f"Generate upbeat branding snippet for {prompt}: "

    response = openai.Completion.create(engine="text-davinci-001", prompt=enriched_prompt, max_tokens=32)

    #Extract output text
    branding_text: str = response["choices"][0]["text"].strip()

    #Strip whitespace
    branding_text = branding_text.strip()

    #Add ... to truncated statements
    last_char = branding_text[-1]

    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    return branding_text

def generate_keywords(prompt: str) -> List[str]:
    #Load the API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")

    enriched_prompt=f"Generate related branding keywords for {prompt}: "

    response = openai.Completion.create(engine="text-davinci-001", prompt=enriched_prompt, max_tokens=32)

    #Extract output text
    keywords_text: str = response["choices"][0]["text"].strip()

    #Strip whitespace
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-", keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    return keywords_array

if __name__ == "__main__":
    main()