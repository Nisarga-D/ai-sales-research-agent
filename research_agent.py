import wikipedia
import ollama


def get_company_info(company):
    try:
        # search for possible pages
        results = wikipedia.search(company)

        if not results:
            return "No information found."

        # try first few results until one works
        for result in results[:5]:
            try:
                page = wikipedia.page(result, auto_suggest=False)
                return page.summary
            except wikipedia.DisambiguationError:
                continue
            except wikipedia.PageError:
                continue

        return "No information found."

    except Exception as e:
        print("Wikipedia error:", e)
        return "No information found."
def analyze_company(summary):

    prompt = f"""
    Based on this company description:

    {summary}

    Provide:
    1. Industry
    2. Key services
    3. Potential business travel needs
    4. Short company summary
    """

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']


def main():

    company = input("Enter company name: ")

    summary = get_company_info(company)

    print("\nCompany info collected...\n")

    analysis = analyze_company(summary)

    print("\n===== AI Research Report =====\n")
    print(analysis)


if __name__ == "__main__":
    main()