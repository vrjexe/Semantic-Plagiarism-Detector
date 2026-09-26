from similarity import calculate_similarity


text1 = "Artificial intelligence is transforming the education sector."

text2 = "AI is changing the way education is delivered."


score = calculate_similarity(text1, text2)


print(f"Semantic Similarity: {score:.2f}%")