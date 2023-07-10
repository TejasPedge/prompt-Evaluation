# Question 5 : Problem Statement: Basic Instagram-Like Application with Flask (Only Backend) 
# [Submit github link]

# You can Refer Flask Documentation: https://flask.palletsprojects.com/en/2.3.x/

# In this exercise, you will create a simple, Instagram-like web application using Flask. 
# This application will not involve any databases or user authentication; 
# instead, data will be stored in Python data structures (Use Dictionary).

# Your application should support the following operations:

# Post Creation: An endpoint should allow the creation of a new post with a 
# username and a caption. For simplicity, a "post" will be a dictionary with 
# username and caption keys. 

# Post Viewing: The application should have an 
# endpoint that lists all posts

# Post Deletion: The application should allow 
# the deletion of a post, given its unique ID.
# Use Python's data structures (like list and dictionary) to store the posts. 

# You can assume that the server will not be shut down, 
# so data persistence between runs is not necessary.

# Constraints:

# Handle the case when trying to delete a post that does not exist.
# Bonus:

# Implement a simple "like" feature that allows a post to receive likes. Each post should keep track of its likes. Create an endpoint to increase the likes of a post by 1. Implement a simple "comment" feature that allows a post to receive comments. Each post should store its comments. Create an endpoint to add a comment to a post.
# Remember to focus on the backend logic and don't worry about creating a frontend. The purpose of this task is to test your backend skills.
from flask import Flask, jsonify, request

app = Flask(__name__)

Dummy_Database = [
    {'id' : 1, 'userName' : 'john', 'caption' : 'feeling happy'}
];


@app.route('/listposts', methods = ['GET'])
def List_All_Posts() :
    return Dummy_Database




if '__name__' == '__main__':
    app.run(debug = True)






