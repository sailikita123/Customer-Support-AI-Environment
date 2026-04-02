def grade(task, action):
    score = 0.0

    # Correct action
    if action.action_type == task["correct_action"]:
        score += 0.4

    # Tone handling
    if task["sentiment"] == "angry" and action.action_type == "respond":
        score += 0.2

    # Resolution
    if action.action_type == "close_ticket":
        score += 0.2

    # Asking info is okay sometimes
    if action.action_type == "ask_more_info":
        score += 0.1

    # Penalty
    if action.action_type not in ["respond", "ask_more_info", "escalate", "close_ticket"]:
        score -= 0.3

    return max(0.0, min(score, 1.0))