# Marketstack API Test Cases

## Overview
This document outlines the test cases for validating the Marketstack historical data API.

**Python Version** >= **3.12.2**

**How to use:**
```
pip install -r requirement.txt    #install related package
export PYTHONPATH=/path/to/your_project
pytest --html=report.html MarketstackAPITest_Proj/Testcases/test_historical_api.py   #run testcase
```
**Log**: MarketstackAPITest_Proj/**%Y-%m-%d_%H%M_%S**_historical_data.log  
  
ex: MarketstackAPITest_Proj/2025-02-10_1804_10_historical_data.log

**Html Report** : MarketstackAPITest_Proj/report.html

## Test Cases

| #  | Test Case Description | Expected Result |
|----|------------------------|----------------|
| 1  | Test with a fake API key to verify Marketstack historical data API response HTTP status code and data.(Negative test) | HTTP status code: `401` |
| 2  | Test Marketstack historical data API response HTTP status code with a valid API key.(Positive test) | HTTP status code: `200` |
| 3  | Test whether the response data format from Marketstack historical data API matches the expected JSON format.(Response json Schema test) | Expected JSON format |
| 4  | Test Marketstack historical data API OHLC values: 1. Ensure all values are greater than 0. 2. Ensure `High (H)` value is greater than or equal to `Low (L)` value.(Business logic test) | 1. Values > 0  2. `H` >= `L` |

## Notes
- Ensure to use a valid API key for test cases 2, 3, and 4.
- The response JSON format should match the documented API response structure.
- If any test fails, review the API request parameters and validate against Marketstack documentation.

