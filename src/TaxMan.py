class TaxMan:
    
    def __init__(self, items, sales_tax):
        self._total = 0
        self.items = items
        self.sales_tax = float(sales_tax[:-1])/100

    def get_total(self): 
        return self._total
    
    def calc_total(self):
        self._total = round((sum([item['price'] for item in self.items])) * (1 + self.sales_tax), 1)
        