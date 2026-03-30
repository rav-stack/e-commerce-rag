from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap = 50)

    for doc in documents:
        split_into_chunks = splitter.split_text(doc["content"])
        for chunk in split_into_chunks:
            chunks.append({"content": chunk, 
            "source": doc["source"]})
    return chunks



#  ✅ Test input
# documents = [
#     {
#         "content": """
# LangChain is a powerful framework for building applications powered by large language models (LLMs). 
# It enables developers to combine LLMs with external data sources, APIs, and workflows to create intelligent systems.

# One of the key features of LangChain is its support for Retrieval-Augmented Generation (RAG). 
# RAG allows models to retrieve relevant information from external knowledge bases before generating responses. 
# This improves accuracy and reduces hallucinations.

# In a typical RAG pipeline, documents are first split into smaller chunks. These chunks are then converted into embeddings 
# using models like OpenAI embeddings. The embeddings are stored in a vector database such as FAISS or Chroma.

# When a user asks a question, the system converts the query into an embedding and performs similarity search 
# to find the most relevant chunks. These retrieved chunks are then passed to the language model as context.

# Chunking is a critical step in this pipeline. If chunks are too large, they may exceed token limits. 
# If they are too small, important context may be lost. That is why chunk overlap is used to preserve meaning 
# across chunk boundaries.

# LangChain also supports agents, which can decide dynamically which tools to use based on user input. 
# This allows building more complex and interactive AI systems.

# Overall, LangChain simplifies the process of building production-ready AI applications by providing modular components 
# for chaining, memory, retrieval, and orchestration.
# """,
#         "source": "langchain_doc.txt"
#     }
# ]

# # ✅ Call function
# result = chunk_documents(documents)

# # ✅ Print output
# for i, chunk in enumerate(result):
#     print(f"\nChunk {i+1}:")
#     print(chunk) 