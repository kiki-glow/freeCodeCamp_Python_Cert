class HashTable:
    def __init__(self):
        # Initialize the collection as an empty dictionary
        self.collection = {}
    
    def hash(self, key):
        # Return the sum of Unicode values of each character
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed_key = self.hash(key)
        # If the hash index doesn't exist, create a nested dictionary
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        
        # Add the key-value pair to the nested dictionary at that hash index
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        # Check if the hash index and the specific key exist
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
            
            # Optional: Clean up the hash index if it becomes empty
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        # Use .get() to return the value if key exists, otherwise return None
        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key, None)
        return None

ht = HashTable()
ht.add("fcc", "coding")
ht.add("cfc", "chemical")

print(ht.collection) 
# Output: {300: {'fcc': 'coding', 'cfc': 'chemical'}}

print(ht.lookup("fcc")) # Output: coding