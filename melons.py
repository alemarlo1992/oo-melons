"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, tax, order_type):
        """Initialize melon order attritbutes"""
        self.species = species 
        self.qty = qty
        self.shipped = False
        self.tax = tax 
        self.order_type = order_type


    def get_total(self):
        """Calculate price, including tax."""
        # self.tax = 0.05

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty, tax = 0.08, order_type = "domestic"):
        """Initialize melon order attributes."""
        # self.tax = 0.08
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        super().__init__(species, qty, tax, order_type)
        # self.tax = 0.08
        # self.order_type = "domestic"

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.country_code = country_code
        # self.species = species
        # self.qty = qty
        
        super().__init__(species, qty, tax, order_type)
        
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
