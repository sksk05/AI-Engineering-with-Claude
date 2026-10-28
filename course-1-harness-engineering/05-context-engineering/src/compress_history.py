# Placeholder history compression helper.

def compress_history(history: list[str], max_items: int = 10):
    return history[-max_items:]
