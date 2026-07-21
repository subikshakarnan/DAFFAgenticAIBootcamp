import requests
from langchain.tools import tool
from bs4 import BeautifulSoup

TRENDING_URL = 'https://github.com/trending/{language}'

# Common natural-language phrasings that are NOT GitHub language slugs.
# We route these to the all-languages trending page instead of letting them
# hit an empty page (which used to make the agent loop and burn tokens).
_ALL_LANGUAGE_ALIASES = {
    "", "all", "any", "everything", "trending", "popular", "top", "best",
    "most popular", "most starred", "most popular git repos",
    "most popular repos", "most popular repositories", "trending repos",
    "trending repositories", "repos", "repositories", "github", "git",
}


def _clean_language(language: str) -> str:
    """Normalise the caller's argument into a GitHub language slug.

    GitHub's trending path accepts a language slug (e.g. 'python',
    'javascript', 'go') or an empty string for all languages. Natural-language
    phrases resolve to all languages rather than an empty result page.
    """
    lang = (language or "").strip().lower()
    if lang in _ALL_LANGUAGE_ALIASES:
        return ""
    return lang


@tool
def trending(language: str = "") -> str:
    """Return today's trending GitHub repositories for a programming language.

    Args:
        language: A single GitHub language slug such as 'python', 'javascript',
            'typescript', 'go', or 'rust'. Pass an empty string to get the most
            popular repositories across all languages. This must be a language
            name, NOT a natural-language search phrase.

    Returns a ranked list of repositories with their star counts. This result
    is final — call this tool at most once per request and do not retry it.
    """
    lang = _clean_language(language)
    try:
        res = requests.get(
            TRENDING_URL.format(language=lang),
            timeout=30,
            headers={'User-Agent': 'Mozilla/5.0'},
        )
        res.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching the GitHub trending page: {e}. Do not retry."

    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.find_all('article', class_='Box-row')

    repos = []
    for row in rows:
        heading = row.find('h2')
        link = heading.find('a') if heading else None
        if not link:
            continue
        # The href is '/owner/repo', which is the clean full repository name.
        name = link.get('href', '').strip('/') or link.get_text(strip=True)
        star_link = row.find('a', href=lambda h: h and h.endswith('/stargazers'))
        stars = star_link.get_text(strip=True) if star_link else 'unknown'
        repos.append((name, stars))

    if not repos:
        scope = f"language '{lang}'" if lang else "all languages"
        return (
            f"No trending repositories were found for {scope}. This is a final "
            f"answer — do NOT call this tool again. If a specific language was "
            f"requested it may not be a valid GitHub language slug; valid "
            f"examples are python, javascript, typescript, go, and rust, or use "
            f"an empty string for all languages."
        )

    scope = f"'{lang}'" if lang else "all languages"
    lines = [f"Top {min(len(repos), 10)} trending GitHub repositories for {scope}:"]
    for i, (name, stars) in enumerate(repos[:10], 1):
        lines.append(f"{i}. {name} - {stars} stars")
    return "\n".join(lines)


if __name__ == '__main__':
    print(trending('python'))
    print('---')
    print(trending('most popular git repos'))
