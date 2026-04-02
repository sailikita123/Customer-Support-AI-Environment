TASKS = [
    {
        "name": "easy_faq",
        "customer_query": "What is your refund policy?",
        "sentiment": "neutral",
        "correct_action": "respond"
    },
    {
        "name": "angry_customer",
        "customer_query": "My order is late!",
        "sentiment": "angry",
        "delay_days": 3,
        "correct_action": "respond"
    },
    {
        "name": "complex_issue",
        "customer_query": "My product is damaged and delivery was late",
        "sentiment": "angry",
        "delay_days": 5,
        "correct_action": "escalate"
    }
]