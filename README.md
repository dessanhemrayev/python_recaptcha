# Flask Google reCAPTCHA Integration

This is a simple Flask application that demonstrates how to integrate Google reCAPTCHA to protect your forms from spam and abuse.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Prerequisites

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dessanhemrayev/python_recaptcha.git
    cd python_recaptcha
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Go to the [Google reCAPTCHA admin console](https://www.google.com/recaptcha/admin/) and register your site to get the Site Key and Secret Key.

2. Replace the placeholders in `app.py` with your actual reCAPTCHA keys:
    ```python
    RECAPTCHA_SITE_KEY = 'your-site-key'
    RECAPTCHA_SECRET_KEY = 'your-secret-key'
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. You should see the reCAPTCHA widget. When you submit the form, the server will verify the reCAPTCHA response and respond accordingly.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Google reCAPTCHA](https://www.google.com/recaptcha/)

---

Feel free to modify and extend this project to fit your needs. If you encounter any issues or have suggestions, please open an issue on the GitHub repository.
