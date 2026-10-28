# Placeholder case facts block helper.

def case_facts_block(facts: list[str]):
    return "\n".join(f"- {fact}" for fact in facts)
