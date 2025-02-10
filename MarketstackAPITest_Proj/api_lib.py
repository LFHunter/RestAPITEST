import requests


class APILib:
    def __init__(self, logger, access_key: str):
        self.logger = logger
        self.logger.info(f"Init APILib with access key:{access_key}")
        self.url = f"http://api.marketstack.com/v1/eod?access_key={access_key}"

    def get_stock_historical_data(self, symbols: str, date_from: str,
                                  date_to: str) -> requests.Response:
        """
        Get Marketstack Historical Data
        (https://marketstack.com/documentation)
        """
        url = f"{self.url}&symbols={symbols}&date_from={date_from}&date_to={date_to}"
        self.logger.info(f"GET url :{url}")
        headers = {}
        response = requests.request("GET", url, headers=headers)
        return response
