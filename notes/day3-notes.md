\# Day 3 Notes



\## Observation Questions — Task 1 (Embeddings)



\*\*What is the dimension count of the Gemini embedding vector? What does each number represent?\*\*

The vector has thousands of dimensions (depends on the model's default output size). Each number represents a coordinate in a multi-dimensional "meaning space" — together they encode the semantic content of the text, not any single interpretable feature on its own.



\*\*Did any cosine similarity result surprise you? Which two texts are more similar than you expected?\*\*

The cat/feline sentence pair scored very high (\~0.8+) despite sharing zero words, which shows the model is matching meaning, not vocabulary. That was the most surprising result.



\*\*Why use task\_type='RETRIEVAL\_QUERY' for the user's question instead of 'RETRIEVAL\_DOCUMENT'?\*\*

Note: the new google-genai SDK we're using doesn't expose separate task\_type embedding calls the way the old SDK did, so embed\_text() and embed\_query() currently use the same underlying call. Conceptually, the distinction still matters: documents and queries are phrased differently (statements vs questions), so a model that's aware of which role the text is playing can position the vectors more accurately for retrieval matching.



\*\*If two chunks have a cosine similarity of 0.95, what does that tell you about their content?\*\*

They are nearly identical in meaning — likely paraphrases of each other or covering the same specific fact, even if the wording differs.



\## Task 2 — Vector Store \& Semantic Search



\*\*Experiment A — top\_k=5 on the off-topic query\*\*

Even with more results requested, the off-topic "weather in Paris" query still only returned chunks from the unrelated sample documents, all with noticeably higher distance scores than on-topic queries. This shows that increasing top\_k doesn't fix bad retrieval — it just returns more irrelevant results, so result count isn't a substitute for filtering by distance/relevance.



\*\*Experiment B — paraphrased query ("Tell me about the NexusChat product")\*\*

The system still correctly retrieved the NexusChat-related chunk from sample.pdf, even though this exact phrasing wasn't in any document. This confirms semantic search works on meaning, not exact text matching.



\*\*Experiment C — distance threshold\*\*

On-topic queries returned distances around 0.49–0.67. The off-topic "weather in Paris" query returned distances above 1.0 (1.05–1.06). Based on this gap, a distance threshold of roughly 0.8–0.9 looks like a reasonable cutoff for "not relevant enough to include."



\## Reflection Questions



\*\*What happens to search quality when you query something outside the documents?\*\*

The system still returns its closest matches (it has no choice — it always returns top\_k results), but the distance scores are much higher, signaling low confidence. This shows why having a good, relevant document set matters — bad documents mean even the "best" results are not actually useful.



\*\*Why use the same embedding model for indexing and querying?\*\*

Different models position text differently in vector space, so a query embedded with one model and chunks embedded with another would not be comparable — their "coordinates" wouldn't line up, breaking similarity search entirely.



\*\*What would you need to make the ChromaDB collection persist?\*\*

Replace chromadb.Client() (in-memory) with chromadb.PersistentClient(path="...") so the collection is saved to disk and reloaded on the next run instead of being rebuilt from scratch every time.



\*\*What's the only remaining piece before a complete RAG chatbot?\*\*

The generation step — taking the retrieved chunks and the user's question and actually having an LLM produce a final, grounded answer.



\## Pipeline Diagram



```

RAW FILE (.txt / .pdf / .docx)

&#x20;       |

&#x20;       v

&#x20; \[Day 2] load\_document()  -->  raw text string

&#x20;       |

&#x20;       v

&#x20; \[Day 2] chunk\_recursive()  -->  list of chunk strings

&#x20;       |

&#x20;       v

&#x20; \[Day 3] embed\_text()  -->  embedding vectors

&#x20;       |

&#x20;       v

&#x20; \[Day 3] collection.add()  -->  stored in ChromaDB

&#x20;       ... (index phase complete)

USER QUESTION  -->  embed\_query()  -->  query vector

&#x20;       |

&#x20;       v

&#x20; collection.query()  -->  top-K most similar chunks

&#x20;       |

&#x20;       v

&#x20; \[Day 4]  Feed chunks + question to Gemini  -->  Final Answer

```

