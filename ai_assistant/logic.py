def get_ai_response(message):
    msg = message.lower()

    if "how to vote" in msg or "vote process" in msg:
        return (
            "To vote, log in with your CNIC, go to the Vote page, "
            "select your preferred candidate, and submit your vote. "
            "You can only vote once."
        )

    if "constituency" in msg:
        return (
            "Your constituency represents your electoral area. "
            "Candidates in your constituency are shown during voting."
        )

    if "after vote" in msg or "what happens" in msg:
        return (
            "After voting, your vote is securely recorded. "
            "Results are published by the Election Commission after voting ends."
        )

    if "is my vote safe" in msg or "security" in msg:
        return (
            "Yes. Each voter can vote only once. Votes are protected by "
            "authentication, database constraints, and audit logging."
        )

    if "result" in msg:
        return (
            "Election results are published officially after voting ends. "
            "You can view them on the Results page."
        )

    return (
        "I can help you with voting steps, security, constituency information, "
        "and result announcements. Please ask a clear question."
    )
