import openai
from openai import OpenAI
import wget

print("Running: navis_agents_gpt4o_file_search.py")

class GPT4oAgent:
    def __init__(self, api_key, model="gpt-4o"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def analyze_text(self, system_message, user_prompt, max_tokens=300):
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content


class FileSearchAgent:
    def __init__(self, api_key, assistant_name, assistant_instructions, assistant_model, assistant_tools, vector_store_name, file_path):  # user_content
        openai.api_key = api_key
        self.client = openai
        self.assistant_id = None
        self.thread_id = None
        self.assistant_name = assistant_name
        self.assistant_instructions = assistant_instructions
        self.assistant_model = assistant_model
        self.assistant_tools = assistant_tools
        self.vector_store_name = vector_store_name
        self.file_path = file_path

        self.assistant = self.create_assistant()
        self.vector_store = self.create_vector_store()
        self.message_file = self.upload_file()

    def create_assistant(self):
        assistant = self.client.beta.assistants.create(
            name=self.assistant_name,
            instructions=self.assistant_instructions,
            model=self.assistant_model,
            tools=self.assistant_tools
        )
        self.assistant_id = assistant.id
        return assistant

    def create_vector_store(self):
        return self.client.beta.vector_stores.create(name=self.vector_store_name)

    def upload_file(self):
        return self.client.files.create(
            file=open(self.file_path, "rb"), purpose="assistants"
        )

    def execute_task(self, request):
        thread = self.client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": request,
                    "attachments": [
                        {"file_id": self.message_file.id,
                            "tools": self.assistant_tools}
                    ],
                }
            ]
        )
        self.thread_id = thread.id
        run = self.client.beta.threads.runs.create_and_poll(
            # get thread.id and assistant.id
            thread_id=self.thread_id, assistant_id=self.assistant_id
        )
        messages = list(self.client.beta.threads.messages.list(
            thread_id=self.thread_id, run_id=run.id))
        return messages[0].content[0].text


api_key = "sk-proj-ZWynagibKLNXGbiCwwr7T3BlbkFJXi5ko0HC4dej0fIdE4Zg"

system_message = "You are a blockchain researcher, skilled in explaining complex blockchain distributed systems concepts."
user_prompt = "What is a good question to ask about Filecoin decentralized storage whitepaper? Share a single example of just the question"
gpt4o_agent = GPT4oAgent(api_key=api_key, model="gpt-4o")
filecoin_question = gpt4o_agent.analyze_text(
    system_message=system_message, user_prompt=user_prompt)
print(filecoin_question)

# download filecoin whitepaper from ipfs gateway
url = 'https://bafybeibsogvuzxkqkcnpnjz4tagaandsct6qvhav5qhhnaz7zed2u25qda.ipfs.w3s.link/ipfs/bafybeibsogvuzxkqkcnpnjz4tagaandsct6qvhav5qhhnaz7zed2u25qda/filecoin.pdf'
filename = wget.download(url)
print("Downloaded from IPFS: " + filename)

instructions = "You are an expert blockchain researcher. Use your knowledge base to answer questions about blockchain whitepapers."

blockchain_file_search_agent = FileSearchAgent(
    api_key=api_key,
    assistant_name="Blockchain Researcher Assistant",
    assistant_instructions=instructions,
    assistant_model="gpt-4o",
    assistant_tools=[{"type": "file_search"}],
    vector_store_name="Filecoin Whitepaper",
    file_path=filename
)

filecoin_whitepaper_summary = blockchain_file_search_agent.execute_task(
    filecoin_question)

print(filecoin_whitepaper_summary.value)
