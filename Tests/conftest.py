import pytest


# @ pytest.fixture(params=[(3, 5, 15), (3.5, 5.5, 19.25)], ids=["int", "float"])
# def get_rectangle(request):
#     print("\n Start DB")
#     yield request.param
#     print("\n Stop DB")

#
# @pytest.fixture()
# def get_triangle():
#     print("\n Start db")
#     yield 3, 4, 5, 0.3, 3.5999999999999996, 12
#     print("\n Stop db")

@pytest.fixture(params=[(3, 4, 5, 0.3, 3.5999999999999996, 12), (3.5, 4.5, 5.5, 0.4, 6.300000000000001, 13.5)],
                ids=["int", "float"])
def get_triangle(request):
    # print("\n Start DB")
    yield request.param
    # print("\n Stop DB")

# @pytest.fixture()
# def start_api(start_db):
#     print("\n Start api")
#     yield
#     print("\n Stop api")
