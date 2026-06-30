\# Day 2 Notes



\## Observation Questions — Task 1 (Ingestion)



\*\*Is the raw PDF text perfectly clean? What extra whitespace/characters do you notice?\*\*

Not perfectly clean — PDF text extraction can include extra line breaks or spacing artifacts depending on how the original PDF laid out text, since PDFs store text by position rather than by paragraph structure.



\*\*Why might leaving blank paragraphs in cause problems for a RAG system?\*\*

Blank paragraphs add no useful information but still take up space in a chunk, diluting the meaningful content and potentially pushing real content out of the chunk size limit.



\*\*What would you need to add to handle an HTML webpage? Name the library.\*\*

You'd need an HTML parser like BeautifulSoup (`bs4`) to strip out tags and extract just the visible text content.



\## Comparison Table — Task 2 (Chunking)



| Strategy   | Chunks Produced | Avg Length (chars) | First Chunk Reads Naturally? |

|------------|------------------|----------------------|-------------------------------|

| Fixed-Size | 2                | 195                  | Partially                     |

| Sentence   | 2                | 169                  | Yes                            |

| Recursive  | 2                | 169                  | Yes                            |



\## Experiments



\*\*overlap=0 in chunk\_fixed():\*\* \[run it and note: do chunk 1 and chunk 2 share any words now? Fill in after testing]



\*\*sentences\_per\_chunk=1 in chunk\_sentences():\*\* \[run it and note: how many chunks now, are they too short?]



\*\*size=100 in chunk\_recursive():\*\* \[run it and note: does chunk count go up or down, why?]



\## Reflection Questions



\*\*Which strategy cut a sentence in half in its first chunk? Why is that a problem?\*\*

Fixed-Size cut a sentence in half ("The system" trails off mid-thought). This is a problem for retrieval because a half-sentence loses meaning — if that chunk gets retrieved, the LLM only sees a fragment and can't form a complete or accurate answer from it.



\*\*If someone asked 'What formats does NexusChat support?' — which chunk from which strategy would you want the retriever to find?\*\*

The Sentence or Recursive chunk, since both preserve the full sentence "It supports PDF, DOCX, and TXT file formats." intact, unlike Fixed-Size which risks cutting it off mid-way.



\*\*Why does overlap exist? What would go wrong with zero overlap if a key fact sits at the boundary?\*\*

Overlap exists so that ideas spanning a chunk boundary aren't lost entirely in either chunk. With zero overlap, if a key fact straddles the cutoff point, it could be split between two chunks, and neither one alone would contain the complete fact for the retriever to find.



\## Day 2 → Full Pipeline Reflection



\*\*Q1: What would you change about how the Day 1 demo chunked its documents, and why?\*\*

\[Answer once you've seen the demo notebook — note: this file wasn't available in our repo]



\*\*Q2: Trace the path from raw DOCX file to Gemini generating an answer, naming each function.\*\*

load\_document() reads the DOCX → chunk\_recursive() splits it into chunks → (Day 3) embed\_text() converts each chunk to a vector and stores it in ChromaDB → (Day 3) embed\_query() embeds the user's question → ChromaDB finds the closest matching chunks → (Day 4) those chunks get passed to Gemini along with the question to generate the final answer.

