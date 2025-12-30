import google.generativeai as genai

# Test your API key
api_key = input("Enter your API key: ")

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Say hello")
    print("✅ SUCCESS! API key works!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ ERROR: {e}")