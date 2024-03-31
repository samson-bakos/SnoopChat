from openai import OpenAI
import openai

api_key_path = "/Users/samsonbakos/keys/OpenAI/key.txt"

with open(api_key_path, "r") as file:
    api_key = file.read().strip()
file_path = "../data/transcript_for_fine_tuning.jsonl"

client = OpenAI(api_key=api_key)

# Upload the dataset file for fine-tuning
try:
    with open(file_path, "rb") as file:
        upload_response = client.files.create(file=file, purpose="fine-tune")
    file_id = upload_response.id
    print(f"File uploaded successfully with ID: {file_id}")
except Exception as e:
    print(f"Failed to upload file: {e}")
    exit()

# Create a fine-tuning job using the uploaded file ID
try:
    fine_tune_response = client.fine_tuning.jobs.create(
        training_file=file_id, model="gpt-3.5-turbo"
    )
    job_id = fine_tune_response.id
    print(f"Fine-tuning job created successfully with ID: {job_id}")
except Exception as e:
    print(f"Failed to create fine-tuning job: {e}")
