"""
Write 2 (or more) test cases for any of the above API options and implement an automation test for each test case using Python, the
test case should have the following:
Clear steps for the test
Expected result
How the expected result will be validated (make sure the answer is what we expected)
Implementation in Python.
(recommendation) Use Pytest parametrize to reduce code but maintain high coverage.
4 scroll down 2 times
5 Select one streamer
6 on the streamer page wait until all is load and take a screenshot
Correct version (WAP) Incorrect website
NOTE:
It is advice to provide several test cases, a mixture of positive and negative scenarios.
Think in framework design and modularity
Delivery:
1. A GitHub Repository ( different than the WAP test)
2. README should include the test case written for the test in a table form
3. Description of what validation is been used and why the candidate used this type of validation
"""

import requests


class APILib:
    def __init__(self, access_key="01df658e2b07051a3de1b54c4553c494"):
        """http://api.marketstack.com/v1/eod?\
                   access_key=01df658e2b07051a3de1b54c4553c494\
                   &symbols=AAPL,AAPL\
                   &date_from=2025-02-03\
                   &date_to=2025-03-07"""
        self.url = f"http://api.marketstack.com/v1/eod?access_key={access_key}"

    def get_stock_historical_data(self, symbols: str, date_from: str, date_to: str):
        url = f"{self.url}&symbols={symbols}&date_from={date_from}&date_to={date_to}"
        headers = {}
        response = requests.request("GET", url, headers=headers)
        return response
