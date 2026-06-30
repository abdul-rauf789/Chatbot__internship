\# Day 1 Glossary



\## Terms



\*\*Embedding\*\* — A list of numbers that represents the meaning of a piece of text, so similar meanings end up as similar numbers.



\*\*Vector Store\*\* — A database built to store these number-lists (vectors) and quickly find which ones are most similar to a given query.



\*\*Chunking\*\* — Breaking a long document into smaller pieces so each piece is small enough to search and feed into an LLM individually.



\*\*Context Window\*\* — The maximum amount of text an LLM can read and consider at one time when generating a response.



\*\*Hallucination\*\* — When an LLM confidently states something that sounds correct but is actually false or made up, often because it isn't grounded in real source data.



\## Questions



\*\*Q1: Why can't we just paste an entire document into the LLM prompt instead of chunking and retrieving?\*\*

Because documents can be much longer than the model's context window, and even when they do fit, stuffing in everything wastes space and buries the relevant part among irrelevant text, making the model's answer less accurate.



\*\*Q2: What would go wrong if the retrieval step returns the wrong chunks?\*\*

The LLM would generate an answer based on irrelevant context, producing a confidently wrong or hallucinated response, since it can only reason over what it was given.

