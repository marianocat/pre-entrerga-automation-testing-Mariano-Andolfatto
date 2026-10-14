import pytest


@pytest.fixture
def order():
    print("\nCreando la lista de orden...")
    return []


@pytest.fixture
def append_first(order):
    print("\nAgregando el primer elemento a la lista de orden...")
    order.append(1)


@pytest.fixture
def append_second(order, append_first):
    print("\nAgregando el segundo elemento a la lista de orden...")
    order.extend([2])


@pytest.fixture(autouse=True)
def append_third(order, append_second):
    print("\nAgregando el tercer elemento a la lista de orden...")
    order += [3]


def test_order(order):
    assert order == [1, 2, 3]