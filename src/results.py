"""Results module"""
from mesonet import *
from xgboost_model import *

class Results:
    @staticmethod
    def get_results(model_name, image):
        if model_name == 'MesoNet':
            meso = Meso4()
            meso.load('./weights/mesonet.weights.h5')
            prediction = meso.predict(Meso4.preprocess_image(image))[0]

        elif model_name == 'XGBoost':
            prediction = DeepFakeXGB.predict_image_label(DeepFakeXGB.preprocess_image(image))

        else:
            prediction = -1

        return prediction
