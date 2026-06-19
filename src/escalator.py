def should_escalate(user_message):

    escalation_keywords = [

        "hacked",
        "legal",
        "lawsuit",
        "complaint",
        "fraud",
        "human agent",
        "manager",
        "refund not received",
        "chargeback",
        "account locked",
        "refund"
    ]

    user_message = user_message.lower()

    for keyword in escalation_keywords:

        if keyword in user_message:
            return True

    return False