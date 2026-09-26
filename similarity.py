from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the pretrained NLP model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(text1, text2):

    # Convert both texts into numerical embeddings
    embeddings = model.encode(
        [text1, text2],
        convert_to_numpy=True
    )

    # Calculate cosine similarity
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    # Convert to percentage
    percentage = similarity * 100

    return percentage
