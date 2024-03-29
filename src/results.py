"""Results module"""
import streamlit as st
from mesonet import *

class Results:
    @staticmethod
    def display_description():
        st.write("Description for ModelB: Hello world")

    def get_results(model_name, image):
        if model_name == 'MesoNet':
            meso = Meso4()
            meso.load('./weights/mesonet.weights.h5')
            prediction = meso.predict(Meso4.preprocess_image(image))

        elif model_name == 'CNN':
            prediction = -1
        else:
            prediction = -1

        return prediction
