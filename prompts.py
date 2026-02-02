'''
File for storing prompts for reuse and tracking.
'''

def get_prompt(content: str) -> str:
    return '''
    Article: {content}

    You are a strict news-trustworthiness classifier.
    Given the article title and body, output exactly one word:
    trustworthy OR untrustworthy.

    Make your decision based on the following criteria:
    1. Source Credibility: Consider the reputation of the source.
    2. Factual Accuracy: Check for verifiable facts and data.
    3. Bias and Objectivity: Assess the neutrality of the language used.
    4. Evidence and References: Look for citations and supporting evidence.
    5. Consistency: Ensure the information aligns with known facts.
    6. Sensationalism: Be wary of exaggerated or emotionally charged language.

    Output Format:
    trustworthy
    OR
    untrustworthy

    '''

def get_prompt_v2(content: str) -> str:
    pass  # Placeholder for future implementation


def get_prompt_v3(content: str) -> str:
    pass  # Placeholder for future implementation