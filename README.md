# Backend Developer Challenge
This challenge is designed to test your skills in Python, designing REST APIs, JSON manipulation, and basic problem-solving abilities.

In this challenge, you'll be tasked to implement a lightweight transaction management system with a set of REST APIs using Flask and Python. The focus is on developing clean, efficient code and meaningful commit messages.

Class Definition
A transaction has the following structure:

```
{
  "description": "String. A brief description of the transaction",
  "amount": "Float. The monetary amount of the transaction. ",
  "date": "String. The date of the transaction in 'YYYY-MM-DD' format"
}
```

You will be implementing CRUD operations for transactions. A template code is provided to you with a GET operation already implemented.

Provided Files
This repository contains:

main.py: This is the main driver code that runs the Flask application.
transactions.py: Contains the placeholder routes for transactions' CRUD operations.
transactions.json: A JSON file containing transactions data. You need to update this file as you implement the POST, PUT and DELETE operations.
Tasks
Complete the transactions REST API by implementing the following methods in transactions.py:

POST /api/transaction: Adds a new transaction to the transaction list.
PUT /api/transaction/<id>: Updates an existing transaction with the given id.
DELETE /api/transaction/<id>: Deletes an existing transaction with the given id.
Update transactions.json whenever a POST, PUT or DELETE method is called.

Running Code
To start the Flask server, run the following command:

```$ python main.py```

Then, you can use a HTTP client (like Postman, curl, etc.) to test your APIs at http://localhost:5000.

Submission Instructions
1. Fork this repository.
2. Complete tasks.
3. Push your changes to your fork.
4. Submit your fork's link along with a brief summary of what you have done.
Please make sure to write meaningful comments and commit messages throughout your coding process.

Evaluation Criteria
Your submission will be evaluated based on the following criteria:

1. Code structure and style: Your code should be well-structured and easy to follow.
2. Completeness: All tasks should be completed.
3. Correctness: Your code should correctly implement the given tasks.

Good luck!# challenge_backend
