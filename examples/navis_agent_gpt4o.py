from openai import OpenAI

print("Running: navis_agent_gpt4o.py")

class NavisAgent:
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

api_key = "sk-proj-ZWynagibKLNXGbiCwwr7T3BlbkFJXi5ko0HC4dej0fIdE4Zg"
agent = NavisAgent(api_key=api_key, model="gpt-4o")

system_message = "You are a blockchain researcher, skilled in explaining complex blockchain distributed systems concepts."
user_prompt = "What is a good question to ask about Filecoin decentralized storage whitepaper? Share a single example of just the question"
result = agent.analyze_text(system_message=system_message, user_prompt=user_prompt)
print(result)