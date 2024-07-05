FROM python:3.9-slim

WORKDIR /app

RUN apt-get update

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the Navis Agents for OpenAI gpt-4o and File Search
# CMD ["python", "navis_agents_gpt4o_file_search.py"]

CMD ["bash"]