import datetime

import pytest

from Baselib.logger_manager import setup_logger
from Baselib.validate_lib import ValidateLib
from MarketstackAPITest_Proj.api_jsonschema import historical_data_schema
from MarketstackAPITest_Proj.api_lib import APILib
from MarketstackAPITest_Proj.config import log_config


class TestHistoricalAPI:
    now = datetime.datetime.now()
    logger = setup_logger(log_config, loggername="historical_logger")

    @classmethod
    def setup_class(cls):
        cls.logger.info("Initial Test")
        cls.valib = ValidateLib(cls.logger)
        cls.apilib = APILib(access_key="01df658e2b07051a3de1b54c4553c494")

    @classmethod
    def teardown_class(cls):
        cls.logger.info("End Test")

    def setup_method(self, method):
        self.logger.info(f"----starting {method.__name__} execution----")

    def teardown_method(self, method):
        self.logger.info(f"----end {method.__name__} execution----")

    def test_get_historical_data_with_fake_accesskey(self):
        resp = self.apilib.get_stock_historical_data(
            symbols="AAPL", date_from="2025-02-03", date_to="2025-03-07")
        expected_json = {
            "error": {
                "code": "invalid_access_key",
                "message": "You have not supplied a valid API Access Key."}}
        self.valib.assert_data(resp.status_code, 401)
        self.valib.assert_data(resp.json(), expected_json)

    @pytest.mark.parametrize(
        "symbols, date_from, date_to",
        [("AAPL,ADC", "2025-02-01", "2025-02-10")])
    def test_get_stock_historical_data(self, symbols: str, date_from: str, date_to: str):
        resp = self.apilib.get_stock_historical_data(
            symbols, date_from, date_to)
        self.valib.assert_data(resp.status_code, 200)

    @pytest.mark.parametrize(
        "symbols, date_from, date_to",
        [("AAPL", "2025-02-01", "2025-03-10"), ("AAPL,ADC", "2025-02-01", "2025-02-10")])
    def test_historical_dataformat(self, symbols: str, date_from: str, date_to: str):
        resp = self.apilib.get_stock_historical_data(
            symbols, date_from, date_to)
        self.valib.validate_json(resp.json(), historical_data_schema)

    @pytest.mark.parametrize(
        "symbols, date_from, date_to",
        [("AAPL", "2025-02-06", "2025-02-11")])
    def test_historical_ohlc_value_should_be_large_than_zero(self, symbols: str,
                                                             date_from: str, date_to: str):
        resp = self.apilib.get_stock_historical_data(
            symbols, date_from, date_to)
        self.logger.info(resp.url)
        self.valib.validate_ohlc_value(resp.json()["data"])
