import pytest


@ pytest.fixture(params=[(3, 5, 15), (3.5, 5.5, 19.25)], ids=["int", "float"])
def get_rectangle(request):
    print("\n Start DB")
    yield request.param
    print("\n Stop DB")


# @pytest.fixture()
# def start_api(start_db):
#     print("\n Start api")
#     yield
#     print("\n Stop api")
