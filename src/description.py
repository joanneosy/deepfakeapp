"""Description module for the models"""
import streamlit as st

class ModelDescriptions:
    @staticmethod
    def display_description(model_name):
        if model_name == "MesoNet":
            st.markdown(
                """
                <ul style="list-style-type: none; padding-left: 0;">
                    <li><b style="color: orange; font-size: 30px;">Mesonet:</b></li>
                    <li><b style="color: orange;">Deep Learning System:</b> Built to spot deepfake images and videos.</li>
                    <li><b style="color: orange;">Multi-scale Convolutional Neural Network:</b> Employs advanced neural network architecture.</li>
                    <li><b style="color: orange;">Detects Manipulated Media:</b> Identifies anomalies indicating manipulated media.</li>
                    <li><b style="color: orange;">Combat Misleading Content:</b> Enhances the ability to combat the spread of misleading content online.</li>
                </ul>
                """,
                unsafe_allow_html=True
            )
        elif model_name == "Convolutional Neural Network":
            st.markdown("<p><b>Description for ModelB:</b> Hello world</p>", unsafe_allow_html=True)

