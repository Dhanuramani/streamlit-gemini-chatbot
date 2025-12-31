import streamlit as st
import requests
import json

# Configure page
st.set_page_config(
    page_title="Local AI Chat App",
    page_icon="🤖",
    layout="wide"
)

def get_ollama_response(prompt: str, model: str = "llama2") -> str:
    """Get response from local Ollama API"""
    try:
        url = "http://localhost:11434/api/generate"
        
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result.get('response', 'No response generated.')
        else:
            return "❌ Ollama server not running. Please start Ollama first."
            
    except requests.exceptions.ConnectionError:
        return "❌ **Ollama Not Running**: Please install and start Ollama server."
    except Exception as e:
        return f"❌ **Error**: {str(e)}"

def main():
    st.title("🤖 Local AI Chat App")
    st.markdown("*Chat with AI running locally - No internet required!*")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        model_options = {
            "Llama 2 (7B)": "llama2",
            "Llama 2 (13B)": "llama2:13b",
            "Code Llama": "codellama",
            "Mistral": "mistral",
            "Neural Chat": "neural-chat"
        }
        
        selected_model = st.selectbox(
            "Choose Local Model:",
            options=list(model_options.keys()),
            index=0
        )
        
        model_name = model_options[selected_model]
        
        st.markdown("---")
        st.markdown("### Setup Instructions")
        st.markdown("1. Install Ollama: [ollama.ai](https://ollama.ai)")
        st.markdown("2. Run: `ollama pull llama2`")
        st.markdown("3. Start: `ollama serve`")
        st.markdown("4. Chat here!")
        
        st.markdown("---")
        st.markdown("**Benefits:**")
        st.markdown("- 🔒 Completely private")
        st.markdown("- 🆓 No API costs")
        st.markdown("- ⚡ Fast responses")
        st.markdown("- 🌐 Works offline")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ollama_response(prompt, model_name)
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