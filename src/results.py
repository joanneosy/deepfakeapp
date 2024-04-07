"""Results module"""
from mesonet import *
from cnn import *

class Results:
    @staticmethod
    def get_results(model_name, image):
        if model_name == 'MesoNet':
            meso = Meso4()
            meso.load('./weights/mesonet.weights.h5')
            prediction = meso.predict(Meso4.preprocess_image(image))

        elif model_name == 'Convolutional Neural Network':
            detector = DeepFakeDetector()
            detector.load_model_weights(filepath='./weights/cnn.weights.h5')
            preprocessed_image = DeepFakeDetector.preprocess_image(image)
            prediction = detector.model.predict(preprocessed_image)

        else:
            prediction = -1

        return prediction
