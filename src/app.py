"""Main app"""

import streamlit as st
from description import ModelDescriptions

def main():
    st.sidebar.title("Model Selection")
    model_option = st.sidebar.selectbox("Select Model", ["ModelA", "ModelB"])

    ModelDescriptions.display_description(model_option)

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

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

if __name__ == "__main__":
    main()
