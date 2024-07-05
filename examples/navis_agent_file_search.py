from openai import OpenAI
import wget

print("Running: navis_agent_file_search.py")

client = OpenAI(api_key="sk-proj-ZWynagibKLNXGbiCwwr7T3BlbkFJXi5ko0HC4dej0fIdE4Zg")

assistant = client.beta.assistants.create(
    name="Blockchain Researcher Assistant",
    instructions="You are an expert blockchain researcher. Use you knowledge base to answer questions about blockchain whitepapers.",
    model="gpt-4o",
    tools=[{"type": "file_search"}],
)

vector_store = client.beta.vector_stores.create(name="Filecoin Whitepaper")

# Download Filecoin whitepaper from ipfs gateway
url = 'https://bafybeibsogvuzxkqkcnpnjz4tagaandsct6qvhav5qhhnaz7zed2u25qda.ipfs.w3s.link/ipfs/bafybeibsogvuzxkqkcnpnjz4tagaandsct6qvhav5qhhnaz7zed2u25qda/filecoin.pdf'
filename = wget.download(url)
print("\n Downloaded: " + filename)

# Upload the user provided file downloaded from IPFS to OpenAI
message_file = client.files.create(
    file=open(filename, "rb"), purpose="assistants"
)

# Create a thread and attach the file to the message
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "Explain how Filecoin creates an algorithmic market for storage, and how storage and retrieval markets are used.",
            "attachments": [
                {"file_id": message_file.id, "tools": [
                    {"type": "file_search"}]}
            ],
        }
    ]
)

print(thread.tool_resources.file_search)

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id, assistant_id=assistant.id
)

messages = list(client.beta.threads.messages.list(
    thread_id=thread.id, run_id=run.id))

message_content = messages[0].content[0].text.value
print(message_content)
