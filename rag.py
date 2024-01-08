import openai
response = openai.Embedding.create(
    input="canine companions say",
    engine="text-similarity-davinci-001")
