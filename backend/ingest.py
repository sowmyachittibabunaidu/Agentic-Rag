import requests
from bs4 import BeautifulSoup
from vectorstore import add_document


def split_text(text, chunk_size=500):
    """
    Split large text into smaller chunks.
    """
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def extract_text(url):
    """
    Extract text from a webpage.
    """

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    # Remove extra spaces
    text = " ".join(text.split())

    return text


def ingest_url(url):
    """
    Download webpage and store it in ChromaDB.
    """

    try:
        text = extract_text(url)

        chunks = split_text(text)

        for i, chunk in enumerate(chunks):
            add_document(
                chunk,
                f"{url}_chunk_{i}"
            )

        print(f"{len(chunks)} chunks added.")

    except Exception as e:
        print("Error:", e)
