import knowledge_base

def update_knowledge_base(intent, response):
    # Update the knowledge base with a new intent and response
    knowledge_base.knowledge_base[intent] = response
    print(f"Updated knowledge base with {intent}: {response}")
    
    # Save the updated knowledge base
    knowledge_base.save_knowledge_base()

if __name__ == "__main__":
    # Example update - in a real scenario, this might come from processing NLP insights
    new_intent = 'ask_time'
    new_response = 'It\'s 3 PM right now. How can I assist you further?'

    update_knowledge_base(new_intent, new_response)

