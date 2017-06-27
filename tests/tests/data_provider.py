import time
from tests.data.customer import Customer


def current_time_millis():
    return int(round(time.time() * 1000))


test_customers = [Customer(firstname="John", lastname="Sparrow", phone="+191156233",
                           address="5th Street 15", postcode="11111", city="New York",
                           country="US", zone="NY",
                           email="john%s@gmail.com" % current_time_millis(),
                           password="2222222"),
                  Customer(firstname="AAAAA", lastname="ssssss", phone="+191156233",
                           address="5th cccccccc 15", postcode="11111", city="New York",
                           country="US", zone="NY",
                           email="john%s@gmail.com" % (current_time_millis()+1),
                           password="******"),
                  Customer(firstname="Johwwwwwn", lastname="Sparrweweweow", phone="+191156233",
                           address="5wqwqwqet 15", postcode="11111", city="New York",
                           country="US", zone="NY",
                           email="john%s@gmail.com" % (current_time_millis()+2),
                           password="******")
                  # ...
                  ]
