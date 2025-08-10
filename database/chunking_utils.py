from typing import List, Dict
import re

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 200) -> List[str]:
    words = re.findall(r'\w+', text)
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        start += (chunk_size - overlap)
    return chunks
