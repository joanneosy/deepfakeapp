import xgboost as xgb
import numpy as np
import joblib

class DeepFakeXGB():
    # Load the XGBoost model
    def __init__(self):
        self.model = DeepFakeXGB()

    # Function to preprocess an image
    def preprocess_image(image):
        # Resize the image to match the size used during training
        image = image.resize((40, 40))
        # Flatten the image to match the input format
        image = np.array(image)
        flattened_image = image.flatten()
        pca = joblib.load('weights/pca.pkl')
        img_data_pca = pca.transform(flattened_image.reshape(1, -1))

        # return np.array([flattened_image])
        return img_data_pca

    # Function to predict label for an image
    def predict_image_label(image):
        # Preprocess the image
        # preprocessed_image = preprocess_image(image)
        # Create a DMatrix for the preprocessed image
        dtest = xgb.DMatrix(image)
        # Make predictions
        bst = xgb.Booster()
        bst.load_model('weights/xgboost.model')
        prediction = bst.predict(dtest)

        # predicted_label = 1 if prediction > 0.5 else 0
        return prediction

