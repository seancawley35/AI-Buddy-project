# Initial knowledge base of Buddy
knowledge_base = {
    'greet': 'Hello! How can I help you today?',
    'thank': 'You\'re welcome!',
    'bye': 'Goodbye! Have a great day!',
}

def save_knowledge_base():
    # This function saves the knowledge_base dict to a file
    # For simplicity, we'll overwrite the same file each time.
    with open('knowledge_base_data.py', 'w') as file:
        file.write('knowledge_base = ' + str(knowledge_base))
