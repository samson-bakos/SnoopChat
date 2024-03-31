# executable version of text parsing method 2, using a prelabeled transcript

import re
import json

transcript_file_path = "../data/transcript.txt"

with open(transcript_file_path, "r", encoding="utf-8") as file:
    transcript_text = file.read()

# regular expression to match lines with at least four sequential capital letters
# that is NOT Snoop Dogg
prompt_regex = re.compile(r"^(?!SNOOP DOGG:)[A-Z]{4,}")

lines = [line for line in transcript_text.split("\n") if line.strip()]

conversations = []
current_prompt = ""
current_response = ""
collect_response = False

for line in lines:
    if line.startswith("SNOOP DOGG:"):
        if collect_response:
            # extract the text after the colon for Snoop Dogg's response
            current_response = line.split(": ", 1)[1]
            conversations.append((current_prompt, current_response))
            # reset for the next cycle
            current_prompt = ""
            current_response = ""
            collect_response = False
    elif prompt_regex.match(line):
        if current_prompt:
            # if there was a previous prompt without a Snoop response, reset response collection
            collect_response = True
        # extract the text after the colon for the prompt
        prompt_text = line.split(": ", 1)[1] if ": " in line else line
        current_prompt = prompt_text
        collect_response = True
    else:
        # append non-prompt, non-response lines to the current response if we're collecting responses
        if collect_response:
            current_response += (
                current_response + " " if current_response else ""
            ) + line

# add the last conversation if it hasn't been added
if current_prompt and current_response:
    conversations.append((current_prompt, current_response))

jsonl_file_path = "../data/transcript_for_fine_tuning.jsonl"

system_message_content = "This chatbot embodies the persona of Snoop Dogg, including his unique slang, humor, and interests."

with open(jsonl_file_path, "w", encoding="utf-8") as jsonl_file:
    for prompt, response in conversations:
        # constructing a single conversation entry with a system message
        conversation_entry = {
            "messages": [
                {"role": "system", "content": system_message_content},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response},
            ]
        }
        # writing the conversation entry as a JSON line in the .jsonl file
        jsonl_file.write(json.dumps(conversation_entry) + "\n")
