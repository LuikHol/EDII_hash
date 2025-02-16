class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Lista de listas para encadeamento

    def hash_function(self, key):
        return key % self.size  # Função hash h(k) = k mod m

    def insert(self, key):
        """Insere uma chave na tabela hash"""
        index = self.hash_function(key)
        posição = self.table[index]
        
        # Verifica se a chave já existe na posição
        if key not in posição:
            posição.append(key)
            print(f"Inserido {key} na posição {index}")
        else:
            print(f"Chave {key} já existe na posição {index}")

    def search(self, key):
        """Busca uma chave na tabela hash"""
        index = self.hash_function(key)
        posição = self.table[index]
        
        if key in posição:
            print(f"Chave {key} encontrada na posição {index}")
            return True
        else:
            print(f"Chave {key} não encontrada")
            return False

    def delete(self, key):
        """Remove uma chave da tabela hash"""
        index = self.hash_function(key)
        posição = self.table[index]
        
        if key in posição:
            posição.remove(key)
            print(f"Chave {key} removida da posição {index}")
            return True
        else:
            print(f"Chave {key} não encontrada para remoção")
            return False

    def print_table(self):
        """Exibe o estado atual da tabela hash"""
        print("\nEstado final da tabela:")
        for i in range(self.size):
            print(f"Posição {i}: {self.table[i]}")
        print()


if __name__ == "__main__":
    # Criação da tabela com m = 9
    ht = HashTable(9)
    
    # Chaves para inserção
    keys = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    
    print("Inserindo chaves na tabela:")
    for key in keys:
        ht.insert(key)
    
    # Exibe o estado final da tabela
    ht.print_table()