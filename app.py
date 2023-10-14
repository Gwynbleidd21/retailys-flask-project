from flask import Flask, render_template
from utils import load_xml_data
import os

app = Flask(__name__)

product_names, spare_parts_dict = load_xml_data('astra_export_xml.zip')


@app.route('/')
def home():
    """Home page route."""
    return render_template('home.html')


@app.route('/count_products')
def count_products():
    """Route to display the number of products."""
    return f"Total number of products: {len(product_names)}"


@app.route('/product_names')
def product_names_list():
    """Route to list the names of the products (limiting to first 100)."""
    return "<br>".join(product_names)


@app.route('/spare_parts')
def spare_parts_list():
    """Route to display the products and their associated spare parts (limiting to first 20)."""
    parts_list = [
        "<br>".join([f"<b>{product}</b>: {', '.join(parts)}"] + parts)
        for product, parts in list(spare_parts_dict.items())
    ]
    return "<br><br>".join(parts_list)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

