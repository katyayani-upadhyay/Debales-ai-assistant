from dotenv import load_dotenv
import os

load_dotenv()

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_rag():
    with open("data/debales_docs.txt", "r", encoding="utf-8") as f:
        text = f.read()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_text(text)

    db = Chroma.from_texts(docs, HuggingFaceEmbeddings())
    return db
