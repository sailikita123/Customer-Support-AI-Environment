import random

class SupportEnv:
    def __init__(self, task):
        self.task = task
        self.reset()

    def reset(self):
        self.state = {
            "customer_query": self.task["customer_query"],
            "order_status": self.task.get("order_status", "processing"),
            "delay_days": self.task.get("delay_days", 0),
            "sentiment": self.task["sentiment"],
            "conversation_history": [],
            "ticket_status": "open"
        }
        return self.state

    def step(self, action):
        reward = 0.0
        done = False

        # Save history
        self.state["conversation_history"].append(action.action_type)

        # Simple transitions
        if action.action_type == "close_ticket":
            self.state["ticket_status"] = "closed"
            done = True

        elif action.action_type == "escalate":
            self.state["ticket_status"] = "escalated"
            done = True

        elif action.action_type == "ask_more_info":
            reward += 0.1

        elif action.action_type == "respond":
            reward += 0.2

        return self.state, reward, done