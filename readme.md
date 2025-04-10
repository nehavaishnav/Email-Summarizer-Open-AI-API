# Email Summarizer with OpenAI API

This project integrates with the Gmail API and OpenAI's GPT to automatically summarize emails from your Gmail inbox. It fetches emails using the Gmail API, processes them to extract relevant content, and then utilizes OpenAI's language model to generate concise summaries.

## Features

- **Email Retrieval**: Connects to your Gmail account to fetch emails.
- **Content Summarization**: Uses OpenAI's GPT model to generate summaries of email content.
- **Configurable Parameters**: Adjust settings such as the number of emails to summarize and specific labels or folders to target.

## Prerequisites

Before setting up the project, ensure you have the following:

- **Python 3.7 or higher**: The project is built using Python.
- **Gmail API Credentials**: Access to the Gmail API requires setting up a project in the Google Cloud Console and obtaining OAuth 2.0 credentials.
- **OpenAI API Key**: Access to OpenAI's GPT model requires an API key from OpenAI.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nehavaishnav/Email-Summarizer-Open-AI-API.git
   ```


2. **Navigate to the Project Directory**:

   ```bash
   cd Email-Summarizer-Open-AI-API
   ```


3. **Install Required Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```


4. **Configure Gmail API**:

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Enable the Gmail API for the project.
   - Create OAuth 2.0 credentials.
   - Download the `credentials.json` file and place it in the `credentials` directory of the project.

5. **Set Up Environment Variables**:

   - Rename the `.env.example` file to `.env`.
   - Open the `.env` file and add your OpenAI API key:

     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

6. **Run the Application**:

   ```bash
   python main.py
   ```


   The application will authenticate with your Gmail account, fetch emails, and generate summaries using OpenAI's GPT model.

## Usage

Upon running the application, it will prompt you to authenticate with your Gmail account. After authentication, it will fetch the latest emails, generate summaries, and display them in the console. You can configure the number of emails to fetch and summarize by modifying the `main.py` file.

## Security Considerations

- **Sensitive Information**: Ensure that your `credentials.json` and `.env` files are not exposed publicly. Add them to your `.gitignore` file to prevent accidental commits.
- **API Usage**: Be mindful of the usage limits of both the Gmail API and OpenAI API to avoid exceeding quotas.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

*Note: This README is based on the project structure and features inferred from the provided information. For detailed implementation and customization, refer to the source code in the repository.* 