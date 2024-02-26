"""Description module for the models"""
import streamlit as st

class ModelDescriptions:
    @staticmethod
    def display_description(model_name):
        if model_name == "ModelA":
            st.write("Description for ModelA: Hello world")
        elif model_name == "ModelB":
            st.write("Description for ModelB: Hello world")

