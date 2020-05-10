# Import the libraries
import numpy as np

# Create a numpy array to represent the data
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

# Load the csv data
recipes = np.genfromtxt('recipes.csv', delimiter=',')

print(recipes)

# Select all the elements from the third column representing the # of eggs each recipe needs
eggs = recipes[:, 2]

# Use a logical statement to igure out which recipes require 1 egg
one_egg = recipes[(eggs == 1)]

# Create a variable with the data from the 3rd row representing cookies recipes
cookies = recipes[2, :]

# Get the # of ingredients for a double batch of cupcakes
double_batch = cupcakes * 2

# Create a new variable called grocery list to store the needed ingredients for 1 batch of cookies and 2 batches of cupcakes
grocery_list = cookies + double_batch

print(grocery_list)
