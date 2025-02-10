# Marketstack API Test Cases

## Overview
This document outlines the test cases for validating the Marketstack historical data API.

## Test Cases

| #  | Test Case Description | Expected Result |
|----|------------------------|----------------|
| 1  | Test with a fake API key to verify Marketstack historical data API response HTTP status code and data. | HTTP status code: `401` |
| 2  | Test Marketstack historical data API response HTTP status code with a valid API key. | HTTP status code: `200` |
| 3  | Test whether the response data format from Marketstack historical data API matches the expected JSON format. | Expected JSON format |
| 4  | Test Marketstack historical data API OHLC values: 1. Ensure all values are greater than 0. 2. Ensure `High (H)` value is greater than or equal to `Low (L)` value. | 1. Values > 0  2. `H` >= `L` |

## Notes
- Ensure to use a valid API key for test cases 2, 3, and 4.
- The response JSON format should match the documented API response structure.
- If any test fails, review the API request parameters and validate against Marketstack documentation.

