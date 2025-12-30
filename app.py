import streamlit as st
import google.generativeai as genai

# Configure page
st.set_page_config(
    page_title="Gemini Chat App",
    page_icon="🤖",
    layout="wide"
)

# REPLACE THIS WITH YOUR ACTUAL API KEY
GEMINI_API_KEY = "AIzaSyYOUR_ACTUAL_API_KEY_HERE"  # ← Put your real API key here

# Configure Gemini
try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    st.error("⚠️ Please replace 'YOUR_API_KEY_HERE' with your actual Gemini API key in the code!")
    st.stop()

def get_gemini_response(prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    """Get response from Gemini API"""
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ **Error**: {str(e)}"

def main():
    st.title("🤖 Gemini Chat App")
    st.markdown("*Chat with Google's Gemini AI - No API key required!*")
    
    # Sidebar for model selection
    with st.sidebar:
        st.header("⚙️ Settings")
        
        model_options = {
            "Gemini 2.5 Flash (Recommended)": "gemini-2.5-flash",
            "Gemini 2.5 Pro": "gemini-2.5-pro",
            "Gemini 2.0 Flash": "gemini-2.0-flash"
        }
        
        selected_model = st.selectbox(
            "Choose AI Model:",
            options=list(model_options.keys()),
            index=0
        )
        
        model_name = model_options[selected_model]
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown(f"**Current Model:** {selected_model}")
        st.markdown("🚀 **Ready to chat!** Just type below.")
        st.markdown("---")
        st.markdown("**Features:**")
        st.markdown("- 💬 Real-time AI conversations")
        st.markdown("- 🧠 Multiple Gemini models")
        st.markdown("- 📱 Mobile-friendly")
        st.markdown("- 🔄 Chat history")
    
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
                response = get_gemini_response(prompt, model_name)
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