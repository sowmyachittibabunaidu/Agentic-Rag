from vectorstore import search_documents

def needs_retrieval(query):
    """
    Decide whether the query needs retrieval.
    This is a simple rule-based agent.
    """

    keywords = [
        "what",
        "who",
        "when",
        "where",
        "why",
        "how",
        "tell me",
        "explain",
        "summarize"
    ]

    query = query.lower()

    for word in keywords:
        if word in query:
            return True

    return False


def agent_response(query):
    """
    Main Agent Function
    """

    if needs_retrieval(query):

        docs = search_documents(query)

        if len(docs) == 0:
            return "No relevant information found."

        answer = "Relevant Information:\n\n"

        for doc in docs:
            answer += "- " + doc + "\n"

        return answer

    else:
        return "This question does not require document retrieval."
