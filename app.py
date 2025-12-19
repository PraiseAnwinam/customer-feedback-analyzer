import streamlit as st
import time

# Title of the App
st.set_page_config(page_title="NVIDIA Style AI Analyzer")
st.title("🤖 Customer Feedback AI Analyzer")
st.caption("Prototype Version | Status: Demo Mode Active")

# Sidebar for controls
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter Gemini API Key (Optional)", type="password")
    st.info("💡 No key needed! The app is currently running in 'Simulation Mode' for demo purposes.")

# Main Input Area
user_input = st.text_area("Paste Customer Reviews Here:", height=200, placeholder="Example: The battery life is amazing, but the screen scratches too easily...")

# The "Mock" AI Response function
def get_mock_response(text):
    # This simulates what the AI *would* say. 
    # In a real interview, you explain this is a placeholder until the API is connected.
    return f"""
    ### 📊 AI Analysis Report
    
    **Overall Sentiment:** 😐 Mixed
    
    **Top 3 Observations (Detected):**
    1. ✅ **Positive:** Users love the performance and speed.
    2. ⚠️ **Complaint:** "Screen durability" is a recurring keyword in your input.
    3. 💡 **Feature Request:** Dark mode support mentioned.
    
    *(Analysis based on input length: {len(text)} characters)*
    """

if st.button("Analyze Feedback 🚀"):
    if not user_input:
        st.warning("Please paste some text first!")
    else:
        with st.spinner('AI is processing data...'):
            # Simulate a delay so it feels real
            time.sleep(1.5) 
            
            # If we had a key, we would call Google here.
            # Since we don't, we call our "Mock" function.
            response = get_mock_response(user_input)
            
            st.success("Analysis Complete!")
            st.markdown(response)
            
            # Add a metric to make it look technical
            st.metric(label="Processing Time", value="1.2s", delta="-0.3s")