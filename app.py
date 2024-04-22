from flask import Flask, request, render_template, redirect
import pickle
import requests
from urllib.parse import unquote

API_KEY = '2232105aa3b848bcb7436221719dc8e0'
# Create the Flask app
app = Flask(__name__)


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


# Define the home page
@app.route('/', methods=['GET'])
def home():

    return render_template('home.html', recipes=first_dishes)

# Define the recommendation page


@app.route('/cluster/<int:cluster_id>/<int:dish_id>')
def cluster(cluster_id, dish_id):
    selected_dish = next(
        (dish for dish in data if dish['id'] == dish_id), None)

    cluster_dishes = [
        cluster for cluster in data if cluster['cluster'] == cluster_id]

    return render_template('recipes.html', selected_dish=selected_dish, cluster_dishes=cluster_dishes[:5])


@app.route('/index', methods=['GET', 'POST'])
def index():
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


@app.route('/recipe/<int:recipe_id>')
def view_specfic_recipe(recipe_id):
    query = request.args.get('query', '')
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
        'includeNutrition': True
    }

    # response = requests.get(url, params=params)
    response = data[recipe_id]

    if response.status_code == 200:
        recipe = response.json()
        return render_template('recipe.html', recipe=recipe, query=query)

    return "Recipe not found", 404


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
