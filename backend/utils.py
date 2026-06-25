import re
import uuid


def clean_text(text):
    """
    Remove extra spaces, tabs and new lines.
    """

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_text(text, chunk_size=500, overlap=50):
    """
    Split text into overlapping chunks.
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def generate_id():
    """
    Generate unique document id.
    """

    return str(uuid.uuid4())


def validate_url(url):
    """
    Check whether the URL is valid.
    """

    pattern = re.compile(
        r"^(http|https)://"
        r"([A-Za-z0-9.-]+)"
        r"(\.[A-Za-z]{2,})"
        r"(/.*)?$"
    )

    return bool(pattern.match(url))


def remove_empty_chunks(chunks):
    """
    Remove empty chunks.
    """

    cleaned = []

    for chunk in chunks:

        chunk = chunk.strip()

        if len(chunk) > 0:
            cleaned.append(chunk)

    return cleaned


def print_banner():
    """
    Startup banner.
    """

    print("=" * 50)
    print("Agentic RAG Chatbot Started")
    print("=" * 50)
