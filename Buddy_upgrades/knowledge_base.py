class KnowledgeBase:
    def __init__(self):
        # Initialize an empty dictionary to store information
        self.data = {}

    def learn(self, key, information):
        """Store new information in the knowledge base."""
        # Here, 'key' is a string that represents the topic or category of the information,
        # and 'information' is the actual piece of data or fact to store.
        self.data[key] = information

    def retrieve(self, key):
        """Retrieve information from the knowledge base."""
        # Return the information associated with the 'key', or None if the key is not found.
        return self.data.get(key, None)

# Example usage
if __name__ == "__main__":
    kb = KnowledgeBase()
    
    # Learning some information
    kb.learn('greeting', 'Hello, how can I assist you?')
    kb.learn('farewell', 'Goodbye, have a nice day!')

    # Retrieving and printing information
    print(kb.retrieve('greeting'))  # Output: Hello, how can I assist you?
    print(kb.retrieve('farewell'))  # Output: Goodbye, have a nice day!
    print(kb.retrieve('unknown'))  # Output: None

