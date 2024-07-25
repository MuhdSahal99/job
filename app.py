import streamlit as st
from pages import candidate_page, employer_page
import nltk

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def main():
    st.sidebar.title("Job Matcher")
    page = st.sidebar.radio("Select Page", ["Candidate", "Employer"])

    if page == "Candidate":
        candidate_page.show()
    elif page == "Employer":
        employer_page.show()

if __name__ == "__main__":
    main()
