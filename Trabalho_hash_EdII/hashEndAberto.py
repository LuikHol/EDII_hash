class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        for i in range(self.size):
            current = (index + i) % self.size
            if self.table[current] is None or self.table[current] == "DELETED":
                self.table[current] = key
                print(f"Inserido {key} na posição {current}")
                return
        print(f"Tabela cheia! Não foi possível inserir {key}")

    def search(self, key):
        index = self.hash(key)
        for i in range(self.size):
            current = (index + i) % self.size
            if self.table[current] == key:
                return current
            if self.table[current] is None:
                return -1
        return -1

    def delete(self, key):
        pos = self.search(key)
        if pos != -1:
            self.table[pos] = "DELETED"
            return True
        return False

    def print_table(self):
        print("Tentativa Linear:", self.table)

class QuadraticProbingHashTable:
    def __init__(self, size, c1=1, c2=3):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        for i in range(self.size):
            current = (index + self.c1*i + self.c2*i*i) % self.size
            if self.table[current] is None or self.table[current] == "DELETED":
                self.table[current] = key
                print(f"Inserido {key} na posição {current}")
                return
        print(f"Tabela cheia! Não foi possível inserir {key}")

    def search(self, key):
        index = self.hash(key)
        for i in range(self.size):
            current = (index + self.c1*i + self.c2*i*i) % self.size
            if self.table[current] == key:
                return current
            if self.table[current] is None:
                return -1
        return -1

    def delete(self, key):
        pos = self.search(key)
        if pos != -1:
            self.table[pos] = "DELETED"
            return True
        return False

    def print_table(self):
        print("Tentativa Quadrática:", self.table)

class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        h1 = self.hash1(key)
        h2 = self.hash2(key)
        for i in range(self.size):
            current = (h1 + i*h2) % self.size
            if self.table[current] is None or self.table[current] == "DELETED":
                self.table[current] = key
                print(f"Inserido {key} na posição {current}")
                return
        print(f"Tabela cheia! Não foi possível inserir {key}")

    def search(self, key):
        h1 = self.hash1(key)
        h2 = self.hash2(key)
        for i in range(self.size):
            current = (h1 + i*h2) % self.size
            if self.table[current] == key:
                return current
            if self.table[current] is None:
                return -1
        return -1

    def delete(self, key):
        pos = self.search(key)
        if pos != -1:
            self.table[pos] = "DELETED"
            return True
        return False

    def print_table(self):
        print("Dispersão Dupla:", self.table)

# Testando com as chaves fornecidas
keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]
m = 11

print("\n=== Tentativa Linear ===")
ht_linear = LinearProbingHashTable(m)
for key in keys:
    ht_linear.insert(key)
ht_linear.print_table()

print("\n=== Tentativa Quadrática ===")
ht_quadratic = QuadraticProbingHashTable(m, c1=1, c2=3)
for key in keys:
    ht_quadratic.insert(key)
ht_quadratic.print_table()

print("\n=== Dispersão Dupla ===")
ht_double = DoubleHashingHashTable(m)
for key in keys:
    ht_double.insert(key)
ht_double.print_table()