import streamlit as st
import google.generativeai as genai
from typing import List, Dict
import os

# Configure page
st.set_page_config(
    page_title="Gemini Chat App",
    page_icon="🤖",
    layout="wide"
)

def configure_gemini(api_key: str, model_name: str = "gemini-2.5-flash") -> tuple[bool, str]:
    """Configure Gemini API with the provided key"""
    try:
        # Validate API key format
        if not api_key or len(api_key.strip()) < 10:
            return False, "API key appears to be too short or empty"
        
        # Remove any whitespace
        api_key = api_key.strip()
        
        # Check if it looks like a valid Google API key
        if not api_key.startswith('AIza'):
            return False, "API key should start with 'AIza'. Make sure you're using a Gemini API key."
        
        if len(api_key) < 35:
            return False, f"API key seems too short ({len(api_key)} chars). Should be ~39 characters."
        
        genai.configure(api_key=api_key)
        
        # Test the connection with a simple prompt
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        
        if response and response.text:
            return True, f"Connection successful with {model_name}!"
        else:
            return False, "Got empty response from API"
        
    except Exception as e:
        error_msg = str(e)
        
        # More specific error handling
        if "API_KEY_INVALID" in error_msg:
            return False, "Invalid API key format. Please double-check your key from Google AI Studio."
        elif "PERMISSION_DENIED" in error_msg:
            return False, "Permission denied. Enable the Generative AI API in Google Cloud Console."
        elif "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower():
            return False, "API quota exceeded. Check your usage limits in Google AI Studio."
        elif "NOT_FOUND" in error_msg:
            return False, f"Model {model_name} not found. Try switching to Gemini Pro or check if available in your region."
        elif "UNAUTHENTICATED" in error_msg:
            return False, "Authentication failed. Your API key might be expired or invalid."
        else:
            return False, f"Error: {error_msg}"

def get_gemini_response(prompt: str, api_key: str, model_name: str = "gemini-2.5-flash") -> str:
    """Get response from Gemini API"""
    try:
        genai.configure(api_key=api_key.strip())
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = str(e).lower()
        if "api_key" in error_msg or "invalid" in error_msg:
            return "❌ **API Key Error**: Your API key appears to be invalid. Please check it in the sidebar."
        elif "quota" in error_msg or "limit" in error_msg:
            return "❌ **Quota Exceeded**: You've reached your API usage limit. Please check your Google AI Studio dashboard."
        elif "permission" in error_msg:
            return "❌ **Permission Error**: Your API key doesn't have permission to use this model."
        else:
            return f"❌ **Error**: {str(e)}"

def main():
    st.title("🤖 Gemini Chat App")
    
    # Sidebar for API key
    with st.sidebar:
        st.header("Configuration")
        
        # Initialize API key in session state
        if "api_key" not in st.session_state:
            st.session_state.api_key = ""
        
        # API key input with session persistence
        api_key_input = st.text_input(
            "Enter your Gemini API Key:",
            value=st.session_state.api_key,
            type="password",
            help="Get your API key from Google AI Studio",
            placeholder="AIza...",
            key="api_key_input"
        )
        
        # Update session state when key changes
        if api_key_input != st.session_state.api_key:
            st.session_state.api_key = api_key_input
        
        api_key = st.session_state.api_key
        
        # Clear API key button
        if api_key and st.button("🗑️ Clear API Key"):
            st.session_state.api_key = ""
            st.rerun()
        
        if api_key:
            if st.button("Test Connection"):
                with st.spinner("Testing API key..."):
                    is_valid, message = configure_gemini(api_key, st.session_state.model_name)
                    if is_valid:
                        st.success(f"✅ {message}")
                        st.session_state.api_key_valid = True
                    else:
                        st.error(f"❌ {message}")
                        st.session_state.api_key_valid = False
        
        # Show API key status
        if api_key:
            key_length = len(api_key.strip())
            if key_length < 30:
                st.warning(f"⚠️ API key seems short ({key_length} chars)")
            elif api_key.strip().startswith('AIza'):
                st.success("✓ API key format looks correct")
                st.info("🔒 API key saved for this session")
            else:
                st.warning("⚠️ API key should start with 'AIza'")
            
            # Show first/last few characters for verification
            if len(api_key.strip()) > 10:
                masked_key = api_key.strip()[:6] + "..." + api_key.strip()[-4:]
                st.info(f"Key preview: {masked_key}")
        else:
            st.info("👆 Enter your API key above to get started")
        
        # Troubleshooting section
        with st.expander("🔧 Troubleshooting"):
            st.markdown("""
            **Step-by-Step API Key Setup:**
            
            1. **Go to Google AI Studio**: [makersuite.google.com](https://makersuite.google.com/app/apikey)
            2. **Sign in** with your Google account
            3. **Click "Create API Key"**
            4. **Select "Create API key in new project"** (recommended)
            5. **Copy the entire key** (starts with 'AIza', ~39 characters)
            6. **Paste it here** and click "Test Connection"
            
            **Common Issues:**
            - ❌ **Wrong API**: Don't use Google Cloud, Maps, or YouTube API keys
            - ❌ **Incomplete copy**: Make sure you copied the full key
            - ❌ **Spaces**: The app removes spaces automatically
            - ❌ **Expired key**: Create a new one if yours is old
            - ❌ **Region**: Gemini might not be available in your region
            
            **Still not working?**
            - Try creating a **new API key**
            - Check if Gemini is **available in your country**
            - Make sure you're signed into the **correct Google account**
            """)
        
        
        st.markdown("---")
        st.markdown("### Quick Links")
        st.markdown("🔑 [Get API Key](https://makersuite.google.com/app/apikey)")
        st.markdown("🏠 [Google AI Studio](https://makersuite.google.com/)")
        st.markdown("📚 [Gemini API Docs](https://ai.google.dev/docs)")
        
        # Model selection
        st.markdown("---")
        st.markdown("### Model Selection")
        
        model_options = {
            "Gemini 2.5 Flash (Latest)": "gemini-2.5-flash",
            "Gemini 2.5 Pro (Latest)": "gemini-2.5-pro",
            "Gemini 2.0 Flash": "gemini-2.0-flash",
            "Gemini Flash (Auto-Latest)": "gemini-flash-latest",
            "Gemini Pro (Auto-Latest)": "gemini-pro-latest",
            "Gemini 2.0 Flash Experimental": "gemini-2.0-flash-exp"
        }
        
        selected_model = st.selectbox(
            "Choose Model:",
            options=list(model_options.keys()),
            index=0,
            help="Try different models if one doesn't work. Gemini 2.5 Flash is recommended."
        )
        
        st.session_state.model_name = model_options[selected_model]
        
        # List available models button
        if st.session_state.api_key and st.button("🔍 List Available Models"):
            with st.spinner("Fetching available models..."):
                try:
                    genai.configure(api_key=st.session_state.api_key.strip())
                    models = genai.list_models()
                    st.markdown("**Available Models:**")
                    for model in models:
                        if 'generateContent' in model.supported_generation_methods:
                            st.text(f"✅ {model.name}")
                except Exception as e:
                    st.error(f"Error listing models: {str(e)}")
        
        st.markdown("### About")
        st.markdown(f"Using: **{selected_model}**")
        st.markdown(f"Model ID: `{st.session_state.model_name}`")
        
        
        # Show API key status
        if api_key:
            key_length = len(api_key.strip())
            if key_length < 30:
                st.warning(f"⚠️ API key seems short ({key_length} chars)")
            elif api_key.strip().startswith('AIza'):
                st.info("✓ API key format looks correct")
            else:
                st.warning("⚠️ API key should start with 'AIza'")
    
    
    # Initialize chat history and API key validation state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "api_key_valid" not in st.session_state:
        st.session_state.api_key_valid = False
    if "model_name" not in st.session_state:
        st.session_state.model_name = "gemini-2.5-flash"
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        if not st.session_state.api_key:
            st.error("Please enter your Gemini API key in the sidebar first.")
            return
        
        if not st.session_state.api_key.strip():
            st.error("API key cannot be empty. Please enter a valid key.")
            return
            
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(prompt, st.session_state.api_key, st.session_state.model_name)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Clear chat button
    if st.session_state.messages:
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()