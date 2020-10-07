# rest_endpoint
Python programme to create a REST endpoint that returns the sum of a list of numbers.

* [Motivation](#motivation)
* [Assumptions](#assumptions)
* [Input Output Details](#input-output-details)
* [Example](#example)
* [Installation](#installation)
* [Tests](#tests)
* [Instructions](#instructions)
* [Improvements](#improvements)

## Motivation
Creating a REST endpoint for http calls returning the sum of a given list of numbers e.g. [1,2,3] => 1+2+3 = 6

## Assumptions
* the endpoint accepts POST requests with the payload in the body
* no authentication/ token is required

## Input Output Details
**Input**\
{"numbers": [num1, num2, num3, ..., n]}

**Output**\
{"total": total sum}

## Example
{"numbers": [1, 2, 3]}

{"total": 6}

## Installation
* this program requires Python 3.7
* further libraries to be installed are listed in "requirements.txt" and "requirements_test.txt"

## Tests
all tests are run using unit test framework

## Instructions
1. either go to "server.py" and run "app.run(host='localhost', debug=True)" (under if "__name__ == '__main__") 
or open a terminal, go into rest_endpoint folder and type: **python server.py** to start the server

2. download Postman -> create a POST request with the link http://localhost:5000/total (or http://127.0.0.1:5000/total),   
headers: Content-Type: application/json, and raw body, e.g. {"numbers": [1, 2, 3, 4]}

3. alternatively, call the send_http_request method within the client.py module, 
an example is shown at the bottom of the client.py file

## Improvements
* use form data instead of JSON data so the user can input the list of numbers directly on the website
