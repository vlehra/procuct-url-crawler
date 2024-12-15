import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import json

# Global Configuration
CONCURRENCY = 10  # Number of concurrent requests
MAX_DEPTH = 3     # Maximum crawl depth
HEADERS = {"User-Agent": "ProductURLCrawler/1.0"}

# URL patterns to identify product pages
PRODUCT_URL_PATTERNS = [
    re.compile(r"/product/", re.IGNORECASE),
    re.compile(r"/item/", re.IGNORECASE),
    re.compile(r"/p/", re.IGNORECASE)
]

async def fetch_url(session, url):
    """Fetch content from a URL using aiohttp."""
    try:
        async with session.get(url, headers=HEADERS) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Failed to fetch {url}: HTTP {response.status}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

def is_product_url(url):
    """Check if a URL matches common product URL patterns."""
    return any(pattern.search(url) for pattern in PRODUCT_URL_PATTERNS)

async def crawl(session, base_url, current_url, visited, results, depth):
    """Recursively crawl a given URL to discover product pages."""
    if depth > MAX_DEPTH or current_url in visited:
        return

    visited.add(current_url)
    print(f"Crawling: {current_url} (Depth: {depth})")

    # Fetch page content
    html = await fetch_url(session, current_url)
    if not html:
        return

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find and process all links
    for a_tag in soup.find_all('a', href=True):
        href = urljoin(base_url, a_tag['href'])
        parsed_url = urlparse(href)

        # Ignore external links or non-HTTP URLs
        if parsed_url.netloc != urlparse(base_url).netloc or not parsed_url.scheme.startswith("http"):
            continue

        # Check if the URL is a product page
        if is_product_url(href):
            results.add(href)

        # Recursively crawl other pages
        await crawl(session, base_url, href, visited, results, depth + 1)

async def main(domains):
    """Main function to initialize and start the crawler."""
    results = {}
    visited = set()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for domain in domains:
            base_url = f"https://{domain}"
            results[domain] = set()
            tasks.append(crawl(session, base_url, base_url, visited, results[domain], depth=0))

        await asyncio.gather(*tasks)

    # Save results to a JSON file
    with open("product_urls.json", "w") as f:
        json.dump({domain: list(urls) for domain, urls in results.items()}, f, indent=4)
    print("Crawling completed. Results saved to product_urls.json")

if __name__ == "__main__":
    # Example input domains
    domains = [
        "amazon.com"
    ]

    asyncio.run(main(domains))