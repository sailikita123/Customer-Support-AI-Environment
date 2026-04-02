def run_inference():
    scenarios = [
        {
            "query": "Where is my order?",
            "type": "easy"
        },
        {
            "query": "My product is damaged and I want a refund",
            "type": "medium"
        },
        {
            "query": "I have been waiting for 2 weeks, very frustrated, want refund NOW!",
            "type": "hard"
        }
    ]

    results = []

    for s in scenarios:
        response = generate_response(s["query"])
        reward = evaluate_response(response)

        results.append({
            "difficulty": s["type"],
            "query": s["query"],
            "response": response,
            "reward": reward
        })

    return results


def generate_response(query):
    q = query.lower()

    if "frustrated" in q or "angry" in q:
        return "We sincerely apologize for the inconvenience. I completely understand your frustration. Your refund has been prioritized and will be processed immediately."

    elif "damaged" in q:
        return "We’re really sorry your product arrived damaged. We will initiate a refund or replacement immediately."

    elif "where is my order" in q:
        return "We apologize for the delay. Your order is on the way and should reach you soon. Thank you for your patience."

    else:
        return "Thank you for reaching out. We are here to help you."


def evaluate_response(response):
    r = response.lower()
    reward = 0.0

    # politeness
    if "sorry" in r or "apologize" in r:
        reward += 0.3

    # solution
    if "refund" in r or "replace" in r:
        reward += 0.4

    # empathy
    if "understand" in r or "frustration" in r:
        reward += 0.3

    return reward