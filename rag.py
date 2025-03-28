# algoroot/rag.py

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

function_metadata = [
    {"name": "get_system_info", "description": "Returns operating system, platform, and CPU count. Use for system details."},
    {"name": "open_url", "description": "Opens or launches a web page in the default browser. Provide the URL. Use for opening websites, URLs, etc."},
    {"name": "create_file", "description": "Creates a new file with optional content. Specify filename and content."},
    {"name": "get_process_list", "description": "Lists all running processes with their IDs and names."},
    {"name": "shutdown_system", "description": "Initiates system shutdown. Use with caution."},
    {"name": "get_current_directory", "description": "Returns the current working directory path."},
]

embedding_model = SentenceTransformer("all-mpnet-base-v2")
embeddings = embedding_model.encode([metadata["description"] for metadata in function_metadata])
embeddings = np.array(embeddings).astype("float32")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def retrieve_function(query: str) -> str:
    query_embedding = embedding_model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, 1)
    if indices[0][0] < len(function_metadata):
        return function_metadata[indices[0][0]]["name"]
    else:
        return None