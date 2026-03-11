from duckduckgo_search import DDGS


def search_web(query, max_results=5):

    urls = []

    try:
        with DDGS() as ddgs:

            results = ddgs.text(query)

            for r in results:

                if len(urls) >= max_results:
                    break

                urls.append(r["href"])

    except Exception as e:
        print("Search failed:", e)

    return urls