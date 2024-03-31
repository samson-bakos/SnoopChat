from openai import OpenAI


def checkstatus(path):

    with open(path, "r") as file:
        api_key = file.read().strip()
    file_path = "../data/transcript_for_fine_tuning.jsonl"

    client = OpenAI(api_key=api_key)

    return client.fine_tuning.jobs.retrieve("ftjob-aR3kGKN4vOj4DlCQm8MN8Vu2")


print(checkstatus(path="/Users/samsonbakos/keys/OpenAI/key.txt"))
