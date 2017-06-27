import pytest
from .data_provider import test_customers


@pytest.mark.parametrize("customer", test_customers)
def test_can_register_customer(app, customer):
    initial_number = app.get_customers_number()
    app.register_new_customer(customer)
    final_number = app.get_customers_number()
    assert final_number == initial_number + 1