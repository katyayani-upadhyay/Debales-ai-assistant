from graph import build_graph

app = build_graph()

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    result = app.invoke({"query": query})
    print("Bot:", result["response"])
