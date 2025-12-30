# Gemini Chat App

A simple Streamlit chat application powered by Google's Gemini AI models (2.5 Flash, 2.5 Pro, etc.).

🚀 **[Live Demo](https://streamlit-gemini-chatbot.streamlit.app)** (Replace with your actual URL after deployment)

## Features

- 🤖 **Multiple Gemini Models**: Choose from Gemini 2.5 Flash, 2.5 Pro, 2.0 Flash, and more
- 💬 **Clean Chat Interface**: Real-time conversation with message history
- 🔐 **Secure API Key Input**: Password-protected API key entry
- 🔧 **Built-in Troubleshooting**: Comprehensive error handling and diagnostics
- 📱 **Responsive Design**: Works on desktop and mobile
- 🚀 **One-Click Deployment**: Ready for Streamlit Community Cloud

## Deployment

### Streamlit Community Cloud
1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy from your forked repository
5. Set `app.py` as the main file

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

3. Run the app:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

5. Enter your API key in the sidebar and start chatting!

## Features

- Clean chat interface with message history
- Sidebar for API key configuration
- Error handling for API issues
- Clear chat history option
- Responsive design

## Getting Your API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Select "Create API key in new project"
5. Copy the generated key (starts with 'AIza')

## Troubleshooting

- **API Key Issues**: Use the built-in troubleshooting guide in the app
- **Model Not Found**: Try different models from the dropdown
- **Quota Exceeded**: Check your usage limits in Google AI Studio
- **Region Issues**: Some models may not be available in all regions

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini (2.5 Flash, 2.5 Pro, 2.0 Flash)
- **Language**: Python 3.8+
- **Deployment**: Streamlit Community Cloud

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).