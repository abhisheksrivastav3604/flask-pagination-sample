from query.queries import alldata

def test_limit():
    # checking from limit
    startPoint = 0
    limit = 10;
    response = alldata('','',startPoint,limit)
    assert len(response) == limit
    pass


