## Navis

Navis enables Artificial Intelligence Agents with Filecoin data on IPFS.

Filecoin has over 22 EiB of data storage capacity and the best way to leverage that data is through Artificial Intelligence models.

Navis provides a programming interface for OpenAI Artificial Intelligence models using Filecoin/IPFS data with support for other models as part of the roadmap.

### Navis Github repository

/navis
  ├── navis_gpt4o_file_search.py
  ├── requirements.txt
  ├── Dockerfile
  └── examples
      └── navis_agents_gpt4o.py
      └── navis_agents_vision.py
      └── navis_file_search.py

### Navis Agents using OpenAI gpt-4o model

ChatGPT
Vision
File Search

### Navis usage

Build Docker image

```bash
docker build -t navis .
```

### Run Navis Agents examples with OpenAI gpt-4o reading IPFS data in Docker container

```bash
# Runs navis_agents_gpt4o_file_search.py and prints result
# This example request a question to gpt-4o to ask about Filecoin whitepaper and then uses OpenAI File Search over Filecoin whitepaper PDF downloading it from IPFS.
docker run navis python3 navis_agents_gpt4o_file_search.py

# Example output
How does the Filecoin protocol ensure data reliability and integrity in a decentralized storage network, and what are the mechanisms for dealing with potential data loss or corruption?

The Filecoin protocol ensures data reliability and integrity through several mechanisms:

1. **Data Integrity and Retrievability**: 
   - Filecoin ensures data integrity by naming pieces after their cryptographic hash. Clients store these hashes to verify the data's integrity upon retrieval. No bounded adversary can convince clients to accept altered or falsified data at the end of a Get execution【4:0†source】【4:18†source】. 
   - Retrievability is achieved by specifying replication factors and erasure coding during the Put request. The system guarantees data can be recovered even if some storage providers fail【4:1†source】.

2. **Proof of Storage**:
   - **Proof-of-Replication (PoRep)**: This mechanism allows storage providers to prove that they are storing unique copies of the data on their physical storage. This proof prevents Sybil, outsourcing, and generation attacks. Storage Miners must generate and submit these proofs to the blockchain periodically【4:3†source】.
   - **Proof-of-Spacetime (PoSt)**: This protocol allows storage providers to prove that they have stored the data for a specified period. These proofs are frequently checked and verified by the network to ensure data continues to be stored as agreed【4:6†source】【4:17†source】.

3. **Fault Tolerance and Self-Healing**:
   - Filecoin is designed to tolerate both management faults (byzantine faults in the Manage protocol) and storage faults (loss or unavailability of data by Storage Miners). The system relies on decentralized verification and coordination, using methods like Byzantine Agreement to audit storage providers【4:0†source】.
   - The protocol also includes self-healing mechanisms. If storage proofs are missing or invalidated due to misbehavior, the network penalizes the faulty miners by slashing their collateral. The system attempts to repair faults by reallocating data when necessary, and in severe cases, refunds the client【4:7†source】【4:4†source】.

4. **Incentives and Penalties**:
   - Storage Miners are incentivized to maintain data integrity and availability by rewarding them with tokens for valid proofs of storage. Conversely, they are penalized for failing to provide the required proofs, ensuring their dominant strategy is to store and reliably serve the data【4:4†source】【4:1†source】.

These combined mechanisms ensure that Filecoin maintains a reliable and verifiable decentralized storage network, even in the face of potential faults and adversarial actions

# This example uses gpt-4o model 
docker run navis python3 navis_agents_gpt4o.py

# This example downloads a picture of a panda from IPFS to use OpenAI vision to get understanding of the picture contains.
docker run navis python3 examples/navis_agent_vision.py

# This example uses OpenAI File Search over Filecoin whitepaper PDF downloading it from IPFS.
docker run navis python3 examples/navis_agent_file_search.py
```

Running Navis Docker image executes navis_gpt4o_file_search.py which creates and executes two Navis Agents, a GPT4oAgent with instructions "What is a good question to ask about Filecoin decentralized storage whitepaper? Share a single example of just the question" and then takes answer to FileSearchAgent to search and summarize Filecoin whitepaper PDF stored in IPFS.

NOTE: You can replace OpenAI secret key in the examples to use your own OpenAI account.



### Navis Roadmap

OpenAI models
-Text to speech/speech to text models using IPFS text/audio

Open source models
-Llama 3
-InternLM 2.5
-Stable Diffusion 3

Model integrations
-Runway 3rd Gen video
-Luma image/text to video
Navis Agents boilerplate for Chainlit/LangChain applications for Retrieval Augmented Generation with IPFS data
