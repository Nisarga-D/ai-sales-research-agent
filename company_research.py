
import wikipedia


def get_company_info(company):
    try:
        results = wikipedia.search(company)

        if not results:
            return None

        for result in results[:5]:
            try:
                page = wikipedia.page(result, auto_suggest=False)
                return page.summary, page.url
            except Exception:
                continue

        return None

    except Exception as e:
        print("Wikipedia error:", e)
        return None


if __name__ == "__main__":

    company = input("Enter company name: ")

    info = get_company_info(company)

    if info is None:
        print("Company information not found.")
    else:
        summary, url = info

        print("\nSource:", url)
        print("\nCompany Summary:\n")
        print(summary)