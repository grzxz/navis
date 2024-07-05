from openai import OpenAI

print("Running: navis_agent_vision.py")

client = OpenAI(api_key="sk-proj-ZWynagibKLNXGbiCwwr7T3BlbkFJXi5ko0HC4dej0fIdE4Zg")

# Navis Agent for OpenAI Vision
class Agent:
    def __init__(self, model="gpt-4o"):
        self.client = OpenAI(api_key="sk-proj-ZWynagibKLNXGbiCwwr7T3BlbkFJXi5ko0HC4dej0fIdE4Zg")
        self.model = model

    def analyze_image(self, ipfs_image_cid, prompt="What’s in this image?", max_tokens=300):
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": "https://" + ipfs_image_cid + ".ipfs.w3s.link/"}
                    },
                ],
            }
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content

navis_agent = Agent()
image_ipfs_cid = "bafkreigw3ka6gd3i3zh2cwygrwmmx3zjt2blypi7mgqsr2rvee7nwfeyyq"
navis_agent_result = navis_agent.analyze_image(image_ipfs_cid)
print(navis_agent_result)
