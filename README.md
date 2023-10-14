# retailys-flask-project

This Flask application provides functionalities to process and display data from an XML file, either standalone or within a ZIP archive. The app supports three primary routes: counting products, displaying product names, and listing spare parts associated with products.

## Features

- Count the total number of products from the XML.
- List product names.
- Display products along with their associated spare parts.

## Setup and Installation

### Local Setup

1. **Clone the repository**:

- `git clone https://github.com/Gwynbleidd21/retailys-flask-project.git`

- `cd flask-docker-app`

2. **Set up a virtual environment** (optional but recommended):

- `python -m venv venv`

- `source venv/bin/activate # On Windows, use venv\Scripts\activate`

3. **Install dependencies**:

- `pip install -r requirements.txt`

4. **Run the application**:

- `python app.py`


### Docker Setup

1. **Build the Docker image**:
- `docker build -t retailys-flask-project .`

2. **Run the application using Docker**:
- `docker run -p 5000:5000 your_flask_app_name`


## API Endpoints

- `GET /`: Home route displaying available tasks.
- `GET /count_products`: Display the total number of products.
- `GET /product_names`: List the names of the products.
- `GET /spare_parts`: Display the products and their associated spare parts.
