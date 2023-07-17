# Document Buddy

This repository contains code for a web application that allows users to chat with multiple PDF documents. The application leverages Streamlit, a Python library for building interactive web apps, to provide a user-friendly interface.

## Installation

To use this application, follow these steps:

1. Clone the repository: `git clone https://github.com/pranathlcp/document-buddy.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Make sure you have the necessary environment variables configured. You can use `.env` file and `dotenv` library for that.
4. Run the application: `streamlit run app.py`

## Usage

Once the application is running, you can interact with it through your web browser. The main functionality of the application is to enable users to upload PDF documents and ask questions related to the content of those documents.

The process for using the application is as follows:

1. Upload PDF documents by using the file uploader in the sidebar.
2. Click on the "Process" button to extract text from the uploaded PDF documents and initialize the conversation chain.
3. Enter your questions in the text input field and press Enter to receive responses from the conversation chain.
4. The chat history will be displayed in the main panel, with bot responses shown in a chatbot-like template and user messages shown in a user-like template.

Please note that the application requires at least one PDF document to be uploaded before it can process questions.

## Customization

You can modify the code in `app.py` to customize the behavior of the application. For example, you can change the templates for bot and user messages, adjust the text chunk size, modify the embeddings used, or customize the styling of the web interface.

Feel free to explore and adapt the code according to your specific requirements.

## Upcoming Enhancements

- Adding a separate page for managing uploaded files, and persisting them
- Adding validation to prevent the user from giving inputs if documents are not available
