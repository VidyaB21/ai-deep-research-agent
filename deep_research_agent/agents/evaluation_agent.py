from transformers import pipeline

generator = pipeline("text-generation", model="google/flan-t5-small")

def evaluation_agent(report_text):
    
    prompt = f"""
    Evaluate the following research report based on:
    - Clarity
    - Logical structure
    - Relevance
    - Depth of analysis

    Give a short evaluation summary and a score out of 10.

    Report:
    {report_text}
    """

    output = generator(prompt, max_length=300)[0]["generated_text"]

    return output