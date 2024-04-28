from flask import Flask, request, render_template, redirect
import pickle
import requests
from urllib.parse import unquote
from jinja2 import Environment

API_KEY = ''
# Create the Flask app
app = Flask(__name__)

# Define a custom filter function for the 'min' operation


def min_filter(a, b):
    return min(a, b)


# Add the custom filter to the Jinja2 environment
app.jinja_env.filters['min'] = min_filter


# Configure the pickle data source
with open('./dfRecommendation', 'rb') as f:
    data = pickle.load(f)

# Convert the data to a list of dictionaries
data = data.reset_index()
data = data.to_dict(orient='records')

# Get first dish of each cluster
first_dishes = {}
for dish in data:
    cluster = dish['cluster']
    if cluster not in first_dishes:
        first_dishes[cluster] = dish


# Define the home page is the landing page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Define the menu page


@app.route('/menu', methods=['GET'])
def menu():
    return render_template('menu.html', recipes=data)


# Define the cuisine page
@app.route('/cuisine', methods=['GET'])
def home():

    return render_template('home.html', recipes=first_dishes)


# Define the recommendation page
@app.route('/cluster/<int:cluster_id>/<int:dish_id>')
def cluster(cluster_id, dish_id):
    selected_dish = next(
        (dish for dish in data if dish['id'] == dish_id), None)

    cluster_dishes = [
        cluster for cluster in data if cluster['cluster'] == cluster_id]

    items_per_slide = 4
    total_items = len(cluster_dishes)
    num_items = -(-total_items // items_per_slide)

    return render_template('recipes.html',
                           num_items=num_items,
                           selected_dish=selected_dish,
                           cluster_dishes=cluster_dishes,
                           items_per_slide=items_per_slide,
                           total_items=total_items)


# Define check out page
@app.route('/checkout')
def checkout():

    return render_template('checkout.html')


@app.route('/getrecipe', methods=['GET', 'POST'])
def get_recipe():
    if request.method == 'POST':
        # query = request.form['query']
        query = request.form.get('query', '')

        if query:
            # recipes = search_recipes(query)
            recipes = data.to_dict(orient='records')

        return render_template('service.html', recipes=recipes, query=query)

    # If GET request or no query/ form submission
    query = request.args.get('query', '')
    decode_query = unquote(query)

    # recipes = search_recipes(decode_query)
    recipes = data.to_dict(orient='records')

    return render_template('service.html', recipes=recipes, query=decode_query)


def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch/'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'addRecipeInformation': True,
        'instructionsRequired': True,
        'fillIngredients': True
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        results = response.json()
        return results['results']

    return []


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
