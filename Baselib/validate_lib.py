import json

from jsonschema import ValidationError, validate


class ValidateLib:

    def __init__(self, logger):
        self.logger = logger
        self.logger.info("Init ValidateLib")

    def assert_data(self, actual: any, expect: any):
        default_error_msg = "[FAIL],\nactual: {actual}\nexpected: {expect}"
        if actual != expect:
            self.logger.error(default_error_msg.format(
                actual=actual, expect=expect))
            assert False
        self.logger.info("[PASS]")
        assert True

    def validate_ohlc_value(self, data_list: list):
        pass_flag = True
        for data in data_list:
            price_list = ["open", "high", "low", "close", "volume",
                          "adj_high", "adj_low", "adj_close", "adj_open",
                          "adj_volume"]
            date_symbol = f"{data['date'].split('T')[0], data['symbol']}"
            error_price = list(filter(lambda x: data[x] <= 0, price_list))
            if error_price:
                self.logger.error(
                    f"{date_symbol}, data:{error_price} shouldn't less  than or equal to 0")
                pass_flag = False
            if float(data["high"]) < float(data["low"]):
                self.logger.error(f'{date_symbol},high price:{data["high"]} should large or\
                                  equal to low price:{data["low"]}')
                pass_flag = False
            if float(data["adj_high"]) < float(data["adj_low"]):
                self.logger.error(
                    f'{date_symbol},adj_high price:{data["adj_high"]} should large or\
                        equal to adj_low price:{data["adj_low"]}')
                pass_flag = False

            if pass_flag:
                assert True
                self.logger.info("[PASS], validate_ohlc_value")
            else:
                assert False

    def validate_json(self, validated_jsonschema: json, standard_jsonschema: json):
        try:
            validate(instance=validated_jsonschema, schema=standard_jsonschema)
            self.logger.info("[PASS], validate JsonSchema")
            assert True
        except ValidationError as e:
            self.logger.error(f"[FAIL], validate JsonSchema:{e.message}")
            assert False


if __name__ == "__main__":
    from Baselib.logger_manager import setup_logger
    from MarketstackAPITest_Proj.api_jsonschema import historical_data_schema
    from MarketstackAPITest_Proj.config import log_config
    logger = setup_logger(log_config, loggername="historical_logger")
    test_pass_historical_data = {
        "pagination": {"limit": 100, "offset": 0, "count": 5, "total": 5},
        "data": [
            {
                "open": 73.14,
                "high": 73.29,
                "low": 72.345,
                "close": 72.89,
                "volume": 578910.0,
                "adj_high": 73.29,
                "adj_low": 72.345,
                "adj_close": 72.89,
                "adj_open": 73.14,
                "adj_volume": 578910.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-07T00:00:00+0000",
            },
            {
                "open": 73.01,
                "high": 73.4,
                "low": 72.39,
                "close": 73.07,
                "volume": 608441.0,
                "adj_high": 73.4,
                "adj_low": 72.39,
                "adj_close": 73.07,
                "adj_open": 73.01,
                "adj_volume": 608441.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-06T00:00:00+0000",
            },
            {
                "open": 73.0,
                "high": 73.28,
                "low": 72.53,
                "close": 72.87,
                "volume": 735270.0,
                "adj_high": 73.28,
                "adj_low": 72.53,
                "adj_close": 72.87,
                "adj_open": 73.0,
                "adj_volume": 735270.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-05T00:00:00+0000",
            },
            {
                "open": 72.32,
                "high": 72.56,
                "low": 71.71,
                "close": 72.43,
                "volume": 463126.0,
                "adj_high": 72.56,
                "adj_low": 71.71,
                "adj_close": 72.43,
                "adj_open": 72.32,
                "adj_volume": 463126.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-04T00:00:00+0000",
            },
            {
                "open": 72.02,
                "high": 73.37,
                "low": 71.46,
                "close": 72.88,
                "volume": 659105.0,
                "adj_high": 73.37,
                "adj_low": 71.46,
                "adj_close": 72.88,
                "adj_open": 72.02,
                "adj_volume": 659105.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-03T00:00:00+0000",
            },
        ],
    }
    test_fail_historical_data = {
        "pagination": {"limit": 100, "offset": 0, "count": 5, "total": 5},
        "data": [
            {
                "open": 73.14,
                "high": "dfdf",
                "low": 72.345,
                "close": 72.89,
                "volume": 578910.0,
                "adj_high": 73.29,
                "adj_low": 72.345,
                "adj_close": 72.89,
                "adj_open": 73.14,
                "adj_volume": 578910.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-07T00:00:00+0000",
            },
            {
                "open": 73.01,
                "high": 73.4,
                "low": 72.39,
                "close": 73.07,
                "volume": 608441.0,
                "adj_high": 73.4,
                "adj_low": 72.39,
                "adj_close": 73.07,
                "adj_open": 73.01,
                "adj_volume": 608441.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-06T00:00:00+0000",
            },
            {
                "open": 73.0,
                "high": 73.28,
                "low": 72.53,
                "close": 72.87,
                "volume": 735270.0,
                "adj_high": 73.28,
                "adj_low": 72.53,
                "adj_close": 72.87,
                "adj_open": 73.0,
                "adj_volume": 735270.0,
                "split_factor": 1.0,
                "dividend": 0.0,
                "symbol": "ADC",
                "exchange": "XNYS",
                "date": "2025-02-05T00:00:00+0000",
            },
        ],
    }
    val_lib = ValidateLib(logger)
    print(val_lib.validate_json(test_pass_historical_data, historical_data_schema))
    # print(val_lib.validate_json(test_fail_historical_data, historical_data_schema))
