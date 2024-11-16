from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend-backend communication

# Home route for the root URL
@app.route('/')
def home():
    return "Welcome to the Room Decor App!"

# Upload route to handle POST requests
@app.route('/upload', methods=['POST'])
def upload():
    # Get files and theme from the request
    images = request.files.getlist('room-images')
    theme = request.form.get('theme')

    # For now, we won't process the images
    # We'll return dummy recommendations based on the theme
    recommendations = get_dummy_recommendations(theme)

    return jsonify({'recommendations': recommendations})

# Function to provide hardcoded dummy recommendations
def get_dummy_recommendations(theme):
    # Hardcoded dummy products
    products = {
        'modern': [
            {
                'name': 'Modern Sofa',
                'image_url': 'https://example.com/modern-sofa.jpg',
                'product_url': 'https://example.com/modern-sofa'
            },
            {
                'name': 'Glass Coffee Table',
                'image_url': 'https://example.com/glass-table.jpg',
                'product_url': 'https://example.com/glass-table'
            }
        ],
        'rustic': [
            {
                'name': 'Rustic Wooden Chair',
                'image_url': 'https://example.com/rustic-chair.jpg',
                'product_url': 'https://example.com/rustic-chair'
            },
            {
                'name': 'Vintage Lamp',
                'image_url': 'https://example.com/vintage-lamp.jpg',
                'product_url': 'https://example.com/vintage-lamp'
            }
        ],
        'scandinavian': [
            {
                'name': 'Scandinavian Bookshelf',
                'image_url': 'https://example.com/scandinavian-bookshelf.jpg',
                'product_url': 'https://example.com/scandinavian-bookshelf'
            },
            {
                'name': 'Minimalist Dining Table',
                'image_url': 'https://example.com/minimalist-table.jpg',
                'product_url': 'https://example.com/minimalist-table'
            }
        ],
        'bohemian': [
            {
                'name': 'Bohemian Rug',
                'image_url': 'https://example.com/bohemian-rug.jpg',
                'product_url': 'https://example.com/bohemian-rug'
            },
            {
                'name': 'Macrame Wall Hanging',
                'image_url': 'https://example.com/macrame.jpg',
                'product_url': 'https://example.com/macrame'
            }
        ]
    }

    return products.get(theme, [])

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
