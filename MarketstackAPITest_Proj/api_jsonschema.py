

historical_data_schema = {
    "type": "object",
    "properties": {
        "pagination": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer"},
                "offset": {"type": "integer"},
                "count": {"type": "integer"},
                "total": {"type": "integer"}
            },
            "required": ["limit", "offset", "count", "total"]
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "open": {"type": "number"},
                    "high": {"type": "number"},
                    "low": {"type": "number"},
                    "close": {"type": "number"},
                    "volume": {"type": "number"},
                    "adj_high": {"type": "number"},
                    "adj_low": {"type": "number"},
                    "adj_close": {"type": "number"},
                    "adj_open": {"type": "number"},
                    "adj_volume": {"type": "number"},
                    "split_factor": {"type": "number"},
                    "dividend": {"type": "number"},
                    "symbol": {"type": "string"},
                    "exchange": {"type": "string"},
                    "date": {"type": "string"}
                },
                "required": [
                    "open", "high", "low", "close", "volume",
                    "adj_high", "adj_low", "adj_close", "adj_open", "adj_volume",
                    "split_factor", "dividend", "symbol", "exchange", "date"
                ]
            }
        }
    },
    "required": ["pagination", "data"]
}