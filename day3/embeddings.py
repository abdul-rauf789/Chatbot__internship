import os
import math
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

EMBED_MODEL = 'gemini-embedding-001'


def embed_text(text):
    result = client.models.embed_content(
        model=EMBED_MODEL,
        contents=text,
    )
    return result.embeddings[0].values


def embed_query(text):
    # Same model/call as embed_text; the new SDK does not require
    # a separate task_type call like the old one did.
    result = client.models.embed_content(
        model=EMBED_MODEL,
        contents=text,
    )
    return result.embeddings[0].values


if __name__ == '__main__':
    sentence = 'Retrieval-Augmented Generation improves LLM accuracy.'
    vector = embed_text(sentence)

    print(f'Text: {sentence}')
    print(f'Vector dimensions: {len(vector)}')
    print(f'First 10 values:   {[round(v, 5) for v in vector[:10]]}')
    print(f'Min value: {min(vector):.5f}   Max value: {max(vector):.5f}')
    print()

    def cosine_similarity(v1, v2):
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        return dot / (norm1 * norm2)

    texts = [
        'The cat sat on the mat.',
        'A feline rested on a rug.',
        'Machine learning models process data.',
        'Deep neural networks learn representations.',
        'The weather in London is often rainy.',
    ]

    print('Cosine similarity to: "The cat sat on the mat."')
    print('-' * 50)
    base_vec = embed_text(texts[0])
    for t in texts:
        vec = embed_text(t)
        sim = cosine_similarity(base_vec, vec)
        print(f'  {sim:.4f}  |  {t}')