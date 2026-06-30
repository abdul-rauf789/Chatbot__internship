\# Day 5 Notes



\## Observation Questions — Task 1 (Conversation Memory)



\*\*Copy the exact rewritten question for Turn 2. Did it correctly resolve 'it' to 'NexusChat'?\*\*

\[Paste the exact "(rewritten for search as: ...)" line from your terminal output here]



\*\*What would happen on Turn 2 without query rewriting?\*\*

\[After temporarily returning `question` unchanged from rewrite\_query() and re-testing, note whether retrieval quality dropped — it should, since "What formats does it support?" alone has no anchor for what "it" refers to.]



\*\*Why rewrite the question for retrieval but pass the ORIGINAL question to generation?\*\*

The rewritten standalone question is optimized for search accuracy (it needs to be self-contained to embed well), but the original question is what the user actually typed — passing it to generation keeps the response natural and directly responsive to their actual wording, while the conversation history fills in any context Gemini needs to understand pronouns like "it" or "that."



\## Task 1 Checkpoint — Memory Test Results



Turn 1: "What is NexusChat?" — \[note result]

Turn 2: "What formats does it support?" — \[note rewritten query + answer]

Turn 3: "How much does the Professional plan cost?" — \[note result]

Turn 4: "Does that include support?" — \[note whether "that" correctly resolved to Professional plan]



\## Task 2 — Polish \& Package



\- safe\_generate\_with\_memory() added to prevent crashes on API failures ✅

\- Empty retrieval handling added (graceful message instead of crash) ✅

\- Configuration centralized at top of file (CHUNK\_SIZE, CHUNK\_OVERLAP, TOP\_K\_RESULTS, HISTORY\_TURNS, COLLECTION\_NAME) ✅

\- README.md written with setup instructions and project structure ✅

\- requirements.txt lists all packages used this week ✅

\- Fresh terminal run-through: \[note results — did it run cleanly start to finish, including a bad question and clean quit?]



\## Week 1 — What I Learned



This week I built every layer of a RAG system from scratch: document ingestion across multiple file formats, three different chunking strategies, embeddings and vector search with ChromaDB, grounded generation with citation requirements, and finally conversation memory with query rewriting. The biggest takeaway was seeing how each layer depends on the one before it — bad chunking hurts retrieval, and bad retrieval hurts generation, no matter how good the prompt is. I also learned how quickly tooling changes in this space, since the SDK I started with was deprecated mid-build and I had to migrate to the new google-genai client.

