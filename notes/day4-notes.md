\# Day 4 Notes



\## Observation Questions — Task 1 (Generation)



\*\*Did Gemini follow the 'I could not find it' instruction for Q2, or did it hallucinate? Copy the response.\*\*

\[Paste your actual Q2 output here once you run generator.py]



\*\*Does Q1's SOURCES section correctly name sample.pdf? What would go wrong without the source label?\*\*

\[Fill in after running — if working correctly, it should cite sample.pdf. Without source labels in the prompt, the model would have no way to tell the user which document an answer came from, breaking the "citation" property that makes RAG trustworthy.]



\*\*Why test generation with fake chunks before connecting ChromaDB?\*\*

It isolates the generation logic from the retrieval logic, so if something breaks you immediately know whether the problem is in how the prompt/answer is built or in how chunks are being retrieved — testing both systems at once makes bugs much harder to track down.



\## Task 2 — Complete RAG Pipeline



Ran day4/rag\_chatbot.py with all 5 test questions:

1\. "What is NexusChat?" — \[note whether it cited sample.pdf correctly]

2\. "What are the rules about sharing data with AI services?" — \[note whether it drew from sample.docx]

3\. "How does RAG work?" — \[note the result]

4\. "What is the refund policy?" — \[note whether it correctly refused instead of hallucinating]

5\. "Tell me everything you know about NexusChat" — \[note whether it stayed grounded]



\## Experiments



\*\*Experiment A — removed grounding instruction\*\*

\[After deleting rules 1–2 in build\_prompt() and re-asking Q4, note whether Gemini hallucinated a refund policy. Restore the rules afterward.]



\*\*Experiment B — top\_k value\*\*

top\_k=1: \[note answer completeness]

top\_k=6: \[note whether it improved or got repetitive]

Best value found: \[your conclusion]



\*\*Experiment C — added sample2.txt\*\*

After adding the pricing document and asking "What does the Professional plan cost?", the chatbot correctly retrieved and cited sample2.txt, answering 200 USD/month with priority support included.



\## Reflection Questions



\*\*Experiment A result — did removing grounding cause hallucination?\*\*

\[Paste the exact Q4 answer Gemini gave without the grounding instruction]



\*\*Experiment B result — best top\_k value and why?\*\*

\[Your reasoning — e.g. top\_k=3 balanced enough context without redundant/repetitive chunks]



\*\*Experiment C result — did it correctly cite sample2.txt?\*\*

Yes — this shows how easy it is to expand a RAG system's knowledge: just add a new file to the document list and the entire pipeline (chunk → embed → index → retrieve) handles it automatically, no other code changes needed.



\*\*One thing this chatbot still can't do that production would need?\*\*

It has no persistent memory between separate runs (in-memory ChromaDB resets every time), no UI, and would need to handle far more documents efficiently than this small demo set.



\*\*Which layer is hardest to get right in production, and why?\*\*

Retrieval quality is arguably the hardest — generation just reflects whatever context it's given, so if retrieval pulls the wrong chunks, no amount of good prompting fixes a fundamentally wrong answer.

