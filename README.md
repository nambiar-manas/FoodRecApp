# Like It or Not

## Introduction

Welcome to the Like It or Not GitHub repository! This repository hosts the source code for a web application designed to provide recipe recommendations based on ingredient similarity. 

Problem: Through surveys and research, it's clear that a significant challenge for restaurant staff, particularly waiters and hostesses, is customers taking an extended time to place their orders. This delay disrupts the smooth flow of service, causing waiters to struggle with uneven attention allocation between tables. Additionally, it results in the formation of long queues, adding to the workload of hostesses. Ultimately, these delays hinder the efficient turnover of tables, impacting both customer satisfaction and the restaurant's overall performance.

Solution: A custom app that reduces the need for customers to bombard their waiter with numerous questions about the menu. Here's how it works: we gather menu data from the restaurant of the information they want to feature(ingredients, features, etc...) Once we gather this data from the restaurant, we utilize it to create a tailored set of recommendations. Customers access these recommendations via a QR code, which leads them to a simple webpage presenting four featured dishes. Based on the customer's selection, the page then displays a subset of additional recommendations comprising dishes similar to the chosen one. This seamless integration of technology aims to streamline the dining experience, empowering customers with information and enhancing their satisfaction while alleviating the burden on waitstaff.

## Repository Structure

In this repository, we showcase an illustrative example of a sample website using Italian dishes from the [Spoonacular API](https://spoonacular.com/food-api). In a real-world scenario, we would seamlessly integrate with the restaurant's operations, gathering ingredient data and images directly from their offerings. By providing this personalized touch, our platform enhances the dining experience by offering comprehensive insights into each dish, empowering customers to make informed choices. 


- **`static/`**: Contains CSS files responsible for styling the website's appearance.
- **`templates/`**: Holds HTML files for the home page and recipe display.
- **`dockerfile`**: Sets up a Docker environment for running the Flask web application along with its dependencies.
- **`FoodRecommendationNotebook.ipynb`**: Jupyter notebook used to pull data from an API, perform agglomerative clustering, and generate recipe recommendations.
- **`app.py`**: Script for setting up the Flask web application, handling recipe recommendations, and serving specific recipe details.
- **`dfRecommendation`**: DataFrame containing the recommendations utilized by the website.
- **`requirements.txt`**: Lists the dependencies required to run the application.

## Dependencies

To run the Like It or Not web application, ensure you have the following dependencies installed:

- Flask==2.1.0
- gunicorn==20.1.0
- Werkzeug==2.3.7
- numpy==1.22.1
- pandas
- requests

