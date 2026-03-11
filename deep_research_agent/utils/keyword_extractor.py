from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, top_k=10):

    vectorizer = TfidfVectorizer(stop_words="english", max_features=top_k)
    X = vectorizer.fit_transform([text])

    keywords = vectorizer.get_feature_names_out()

    return list(keywords)