def token_to_cost(tokens: int, price_per_1m_tokens: float) -> float:
    """Return estimated cost for a number of tokens at a given price per 1M tokens."""
    return (tokens / 1_000_000) * price_per_1m_tokens


def format_cost(amount: float) -> str:
    return f"${amount:.4f}"
