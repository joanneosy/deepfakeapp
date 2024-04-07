"""Main app"""

import streamlit as st
from description import ModelDescriptions
from PIL import Image
from results import Results

def main():
    st.sidebar.title("Model Selection")
    
    # Add placeholder to model selection dropdown
    model_option = st.sidebar.selectbox("Select Model", ["Please select a model", "MesoNet", "Convolutional Neural Network"])

    # Check if a model is selected
    if model_option != "Please select a model":
        uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        ModelDescriptions.display_description(model_option)

        if uploaded_file:
            st.success("Image uploaded successfully!")
            pil_image = Image.open(uploaded_file)
            run_model_button = st.button("Run Model")

            if run_model_button:
                with st.spinner("In progress..."):
                    results = Results.get_results(model_option, pil_image)

                if results == -1:
                    st.error("Something went wrong! Please try again.")
                elif model_option in ('MesoNet', 'Convolutional Neural Network'):
                    # {'Fake': 0, 'Real': 1}
                    st.success("Image classified!")
                    real_conf = round(results[0][0] * 100, 2)
                    fake_conf = round((1 - results[0][0]) * 100, 2)
                    st.write(f"Results: {results[0][0]}")
                    if results < 0.5:
                        st.write(f"Prediction: Fake")
                        st.write(f"Confidence: {fake_conf}%")
                    else:
                        st.write(f"Prediction: Real")
                        st.write(f"Real Certainty: {real_conf}%")

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
