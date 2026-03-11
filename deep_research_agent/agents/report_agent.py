from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


def report_agent(topic, text):

    prompt = f"""
Explain the topic clearly:

Topic: {topic}

Information:
{text}

Write a detailed explanation with examples.
"""

    result = generator(
        prompt,
        max_length=350,
        do_sample=True
    )[0]["generated_text"]

    return result