"""Main app"""

import streamlit as st
from description import ModelDescriptions

def main():
    st.sidebar.title("Model Selection")
    
    # Add placeholder to model selection dropdown
    model_option = st.sidebar.selectbox("Select Model", ["Please select a model", "ModelA", "ModelB"])

    # Check if a model is selected
    if model_option != "Please select a model":
        uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        ModelDescriptions.display_description(model_option)

        if uploaded_file:
            st.success("Image uploaded successfully!")
            run_model_button = st.button("Run Model")

            if run_model_button:
                st.text("Running Model...")
                with st.spinner("In progress..."):
                    # Simulate model running for 10 seconds
                    import time
                    time.sleep(10)
                st.success("Model finished running!")

                show_results_button = st.button("Show Results")

                if show_results_button:
                    st.success("Image classified!")

    else:
        # Landing page with animation about deepfake
        st.title("Welcome to Deepfake Detection Solution")
        
        st.write("This is a Streamlit app for deepfake image detection using deep learning models.")

        with open("static/deepfake_animation.css", "r") as f:
            css_content = f.read()
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

        with open("static/deepfake_animation.html", "r") as f:
            html_content = f.read()
            st.markdown(html_content, unsafe_allow_html=True)

        # Add the powered by DeepSense license
        st.markdown("<p style='text-align:center; color:#888;'>Powered by DeepSense</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
