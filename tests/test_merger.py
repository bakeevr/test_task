from src.utils.merger import merge_data


def test_merger_data():
    data1 = {"key1": 1}
    data2 = {"key2": 2}

    result = merge_data(data1, data2)

    assert result == {"key1": 1, "key2": 2}


def test_merger_empty():
    data1 = {}

    result = merge_data(data1)

    assert result == {}
