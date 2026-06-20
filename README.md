# Persona-Aware Support Agent

## 1. Project Overview

The Persona-Aware Support Agent is an AI-powered customer support system that adapts its responses based on the user's persona. The system combines persona detection, Retrieval-Augmented Generation (RAG), response generation using Gemini, and escalation logic to provide personalized support experiences.

The agent can:

* Detect user personas automatically
* Retrieve relevant support documentation
* Generate persona-specific responses
* Escalate sensitive cases to human agents
* Display confidence scores
* Collect user feedback through a Streamlit interface

---

## 2. Tech Stack

### Programming Language

* Python 3.13

### LLM

* Google Gemini 2.5 Flash
* google-genai 2.8.0

### RAG Components

* LangChain
* ChromaDB 1.5.9
* Sentence Transformers 5.6.0
* HuggingFace Embeddings

### Frontend

* Streamlit 1.30.0

### Additional Libraries

* python-dotenv 1.2.2
* pandas
* numpy

---

## 3. Architecture Diagram

User Query
↓
Persona Detection
↓
RAG Retrieval
↓
Response Generation
↓
Escalation Check
↓
Human Handoff (if required)
↓
Final Response

### Workflow

1. User submits a support query.
2. Persona classifier identifies the user type.
3. RAG retrieves relevant support documents.
4. Gemini generates a personalized response.
5. Escalation logic checks for sensitive cases.
6. System either:

   * Returns AI response
   * Escalates to human support

---

## 4. Persona Detection Strategy

### Classification Method

The system uses rule-based persona classification.

### Supported Personas

#### Technical Expert

Keywords:

* API
* database
* integration
* authentication
* server
* endpoint

#### Business Executive

Keywords:

* billing
* revenue
* invoice
* payment
* subscription

#### Frustrated User

Keywords:

* broken
* not working
* terrible
* frustrated
* issue
* problem

### Prompt Design

The detected persona is injected into the Gemini prompt so that response tone and detail level match the user.

Examples:

Technical Expert:

* Detailed explanations
* Technical terminology
* Step-by-step debugging

Business Executive:

* Professional tone
* Business impact focus
* Concise summaries

Frustrated User:

* Empathetic tone
* Reassurance
* Clear resolution steps

---

## 5. RAG Pipeline Design

### Chunking Strategy

RecursiveCharacterTextSplitter

Parameters:

* Chunk Size: 400
* Chunk Overlap: 40

### Embedding Model

sentence-transformers/all-MiniLM-L6-v2

Reason:

* Lightweight
* Fast
* Strong semantic retrieval performance

### Vector Database

ChromaDB

Reason:

* Easy integration with LangChain
* Persistent local storage
* Fast similarity search

### Retrieval Strategy

1. Load support documents
2. Generate embeddings
3. Store embeddings in ChromaDB
4. Perform similarity search
5. Return Top-K relevant chunks

Default:

* Top K = 3

---

## 6. Escalation Logic

### Escalation Triggers

The system escalates when messages contain:

* hacked
* fraud
* lawsuit
* legal
* complaint
* chargeback
* account locked
* refund not received
* human agent
* manager

### Human Handoff

When escalation is triggered:

ESCALATION REQUIRED

The user is directed to human support.

### Confidence Threshold

Confidence score is calculated from retrieval similarity scores.

Higher retrieval relevance results in higher confidence percentages displayed in the UI.

---

## 7. Setup Instructions

### Step 1

Clone repository

git clone <repository-url>

### Step 2

Navigate to project folder

cd persona-aware-support-agent

### Step 3

Create .env file

GEMINI_API_KEY=AQ.Ab.......

### Step 4

Run Streamlit Application

python -m streamlit run streamlit_app.py

---

## 8. Environment Variables

Required:

GEMINI_API_KEY

Example:

GEMINI_API_KEY= AQ.Ab......

---

## 9. Example Queries

### Example 1

Input:
Where is the guide to clear cookies? It's been an hour and nothing is loading.

Expected Persona:
Frustrated User

### Example 2

Input:
What are the header parameter requirements for your bearer token authentication?

Expected Persona:
Technical Expert

### Example 3

Input:
Our operational uptime is decreasing. We need a timeline of when billing disputes are resolved.

Expected Persona:
Business Executive

### Example 4

Input:
I'm experiencing an issue with your database integration that's causing internal errors.

Expected Persona:
Technical Expert

### Example 5

Input:
My billing statement has unexpected duplicate charges. I demand an immediate refund.

Expected Behavior:
Escalation to Human Support

---

## 10. Bonus Features Implemented

### Confidence Score

Displays retrieval confidence percentage.

### Feedback Collection

Users can submit:

*  Helpful
*  Not Helpful

through the Streamlit interface.

---

## 11. Known Limitations

### Current Limitations

* Rule-based persona detection
* Limited support document corpus
* Single-turn conversations
* No sentiment analysis
* No analytics dashboard

### Future Improvements

* Machine learning based persona classification
* Multi-turn conversation memory
* Sentiment analysis
* LangGraph workflows
* Agentic multi-agent architecture
* Analytics dashboard
* Human approval workflows
* Advanced feedback analytics

---

## 12. Repository Structure

persona-aware-support-agent/

├── data/

├── src/

│ ├── classifier.py

│ ├── rag_pipeline.py

│ ├── generator.py

│ └── escalator.py

├── streamlit_app.py

├── app.py

├── requirements.txt

├── README.md

└── .env

# Author

Snehitha Ponnada
