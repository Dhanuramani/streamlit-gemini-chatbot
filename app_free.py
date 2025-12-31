import streamlit as st
import requests
import json

# Configure page
st.set_page_config(
    page_title="Free AI Chat App",
    page_icon="🤖",
    layout="wide"
)

def get_free_ai_response(prompt: str, model: str = "microsoft/DialoGPT-medium") -> str:
    """Get response from Hugging Face free API"""
    try:
        # Hugging Face Inference API (free tier)
        API_URL = f"https://api-inference.huggingface.co/models/{model}"
        
        headers = {
            "Content-Type": "application/json",
        }
        
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": 100,
                "temperature": 0.7,
                "do_sample": True
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', 'Sorry, I could not generate a response.')
            else:
                return "Sorry, I could not generate a response."
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"❌ **Error**: {str(e)}"

def main():
    st.title("🤖 Free AI Chat App")
    st.markdown("*Chat with AI - Completely Free! No API key required.*")
    
    # Sidebar for model selection
    with st.sidebar:
        st.header("⚙️ Settings")
        
        model_options = {
            "DialoGPT Medium (Conversational)": "microsoft/DialoGPT-medium",
            "DialoGPT Large (Better Quality)": "microsoft/DialoGPT-large",
            "BlenderBot (Facebook)": "facebook/blenderbot-400M-distill",
            "GPT-2 Medium": "gpt2-medium"
        }
        
        selected_model = st.selectbox(
            "Choose AI Model:",
            options=list(model_options.keys()),
            index=0,
            help="Different free AI models with various capabilities"
        )
        
        model_name = model_options[selected_model]
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown(f"**Current Model:** {selected_model}")
        st.markdown("🆓 **Completely Free!** Powered by Hugging Face")
        st.markdown("---")
        st.markdown("**Features:**")
        st.markdown("- 💬 Real-time AI conversations")
        st.markdown("- 🆓 No API key required")
        st.markdown("- 🌐 Multiple free AI models")
        st.markdown("- 📱 Mobile-friendly")
        st.markdown("- 🔄 Chat history")
        
        st.markdown("---")
        st.markdown("**Note:** Free models may be slower and have usage limits.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to talk about?"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking... (Free models may take a moment)"):
                response = get_free_ai_response(prompt, model_name)
                st.markdown(response)
        
        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Clear chat button
    if st.session_state.messages:
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()