# Streamlit Deepfake Image Detection App

This is a simple Streamlit web application for deepfake image detection using different machine models. Users can select a model, upload an image, run the model, and view the classification results.

## Prerequisites

Before running the application, make sure you have Python installed. It is recommended to use a virtual environment to manage dependencies. If you don't have Streamlit installed, you can install it by running:

```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/li00-lab/deepfake_app.git
```

2. Navigate to the project directory:

```bash
cd deepfake_app
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

Once you've set up the environment, you can run the Streamlit app with the following command:

```bash
streamlit run src/app.py
```

This will start the development server, and you can access the app in your web browser at `http://localhost:8501`.

## Usage

1. Select a model from the sidebar.
2. Upload an image (JPEG, PNG).
3. Click the "Run Model" button to simulate model running.
4. Click the "Show Results" button to view the classification results.

## Contributing
If you'd like to contribute to the project, please open an issue or create a pull request. We welcome your suggestions and improvements.

# License
This project is licensed under the MIT License - see the `LICENSE` file for details.
