from googlesearch import search
from newspaper import Article
from newspaper.article import ArticleException 
import streamlit as st
import nltk

nltk.download('punkt')
st.title("Pro Bono Advice")

def article_content(url):
    article = Article(url)
    
    try:
        article.download()
        article.parse()
        article.nlp()
        st.write(article.summary)
    except ArticleException as e:
        print("Error while processing article:", e)

def search_and_extract(query):
    search_results = search(query)
    for i, result in enumerate(search_results, start=1):
        if result in visited_links:
            continue
        visited_links.add(result)
        st.subheader(result)
        article_content(result)

if __name__ == "__main__":
    visited_links = set()
    search_queries = ['pro bono advice for charities', 'managing pro bono charity cleverly']
    for search_query in search_queries:
        st.header(search_query.upper(), divider = "rainbow")
        search_and_extract(search_query)
