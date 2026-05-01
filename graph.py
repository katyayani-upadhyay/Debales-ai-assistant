from langgraph.graph import StateGraph
from rag import load_rag
from tools import search_tool

rag_db = load_rag()

def format_response(text):
    if not text:
        return "No relevant information found."

    sentences = text.split(". ")
    important = sentences[:3]

    bullets = "\n".join([f"• {s.strip()}" for s in important if s])

    return bullets if bullets else text[:200]

def decide(state):
    query = state["query"].lower()
    if "debales" in query:
        return "rag"
    else:
        return "search"

def rag_node(state):
    docs = rag_db.similarity_search(state["query"])
    if not docs:
        return {"response": "I couldn't find reliable info."}
    clean_text = format_response(docs[0].page_content)

    return {
    "response": f"📌 From Debales AI data:\n\n{clean_text}"
    }

def search_node(state):
    result = search_tool(state["query"])
    clean_text = format_response(result)

    return {
    "response": f"🌐 From external sources:\n\n{clean_text}"
    }

def build_graph():
    graph = StateGraph(dict)

    # nodes
    graph.add_node("rag", rag_node)
    graph.add_node("search", search_node)

    # conditional routing
    graph.add_conditional_edges(
        "__start__",   # 👈 IMPORTANT FIX
        decide,
        {
            "rag": "rag",
            "search": "search"
        }
    )

    return graph.compile()