from src.analyze_log import (
    client_dishes,
    uneaten_client_dishes,
    not_week_days
)

from collections import Counter


class TrackOrders:
    def __init__(self) -> list:
        self.data = []
    # aqui deve expor a quantidade de estoque

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return client_dishes(customer, self.data)

    def get_never_ordered_per_customer(self, customer):
        return uneaten_client_dishes(customer, self.data)

    def get_days_never_visited_per_customer(self, customer):
        return not_week_days(customer, self.data)

    def get_busiest_day(self):
        get_days = []

        for item in self.data:
            get_days.append(item[2])

        return Counter(get_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        pass
