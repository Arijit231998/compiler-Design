class SymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def lookup(self, key):
        return self.table.get(key, None)

    def update(self, key, value):
        if key in self.table:
            self.table[key] = value

    def remove(self, key):
        if key in self.table:
            del self.table[key]

# Usage example:
if __name__ == "__main__":
    country_code_table = SymbolTable()
    country_code_table.insert('91', 'India')
    print(country_code_table.lookup('91'))  # Output: India

    country_code_table.update('91', 'United States')
    print(country_code_table.lookup('91'))  # Output: United States

    country_code_table.remove('91')
    print(country_code_table.lookup('91'))  # Output: None