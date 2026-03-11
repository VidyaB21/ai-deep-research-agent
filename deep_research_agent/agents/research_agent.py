import wikipedia


def research_agent(topic):

    sources = []
    combined_text = ""

    try:

        results = wikipedia.search(topic)

        for r in results[:5]:

            try:

                page = wikipedia.page(r)

                combined_text += page.content[:1500]

                sources.append(page.url)

            except:
                continue

    except:
        pass

    if combined_text == "":
        combined_text = f"""
{topic} is an important field of study.
Researchers analyze its concepts, applications,
challenges, and future developments.
"""

    return combined_text, sources