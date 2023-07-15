import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader


def get_pdf_text(pdf_docs):
    text = ""
    for pdf_doc in pdf_docs:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def main():
    load_dotenv()
    st.set_page_config(page_title='Chat with Documents', page_icon=':books:')
    st.header("Chat with Documents :books:")
    st.text_input("Ask anything about your documents")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload Your PDF Documents", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get PDF Text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                # Get the text chunks


                # Create the vector store with embeddings


if __name__ == '__main__':
    main()
