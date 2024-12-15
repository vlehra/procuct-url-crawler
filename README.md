# Product URL Crawler

# Overview
    This Python script is a web crawler designed to discover and list all product URLs across multiple e-commerce websites. It recursively scans the provided domains, identifies product pages based on predefined URL patterns, and outputs the results in a structured JSON file.

# Features
    1 URL Discovery:
        Intelligently identifies product URLs using common patterns (e.g., /product/, /item/, /p/).
    2 Concurrency:
        Utilizes asynchronous programming (aiohttp and asyncio) to fetch multiple pages concurrently, improving performance.
    3 Scalability:
        Handles crawling for large websites with deep hierarchies efficiently.
    4 Robustness:
        Deals with edge cases like dynamic content loading, URL structure variations, and invalid links.
    5 Output:
        Saves discovered product URLs grouped by domain into a JSON file (product_urls.json).

# Requirements
    Before running the script, ensure the following Python modules are installed:
    aiohttp: For asynchronous HTTP requests.
    beautifulsoup4: For parsing HTML content.
    lxml: (Optional) As an additional parser for BeautifulSoup.
    asyncio: For managing asynchronous tasks (built into Python).
    re: For regular expression matching (built into Python).
    json: For handling and saving output data (built into Python).

# Installation
    Install the required modules using pip:
    pip install aiohttp beautifulsoup4 lxml

#How to Use
    Clone the repository to your local system:
    git clone https://github.com/vlehra/procuct-url-crawler.git
    cd procuct-url-crawler
    
    Update the domains list in the script with the e-commerce domains you want to crawl:

    domains = [
        "example1.com",
        "example2.com",
        "example3.com"
    ]
    Run the script using Python (requires Python 3.8+):
    python crawler.py
    View the output in the generated product_urls.json file.
    Example Output
    The output is saved as a JSON file with the discovered product URLs grouped by domain:
    {
        "example1.com": [
            "https://example1.com/product/123",
            "https://example1.com/item/456"
        ],
        "example2.com": [
            "https://example2.com/p/789"
        ]
    }

# Customization
    Modify the PRODUCT_URL_PATTERNS list in the script to add or update patterns for identifying product URLs:

    PRODUCT_URL_PATTERNS = [
        re.compile(r"/product/", re.IGNORECASE),
        re.compile(r"/item/", re.IGNORECASE),
        re.compile(r"/p/", re.IGNORECASE)
    ]

    Adjust the CONCURRENCY and MAX_DEPTH settings to tune performance:

    CONCURRENCY = 10  # Number of concurrent requests
    MAX_DEPTH = 3     # Maximum crawl depth

# Example Websites to Test
    Here are some example e-commerce websites to test the crawler (ensure compliance with their robots.txt files):
    
    Amazon
    eBay
    Walmart
    Best Buy
    Target
    Flipkart
    AliExpress

# Limitations
    The crawler does not execute JavaScript. To handle websites that rely heavily on JavaScript for rendering content, integration with tools like Selenium may be required.
    The script respects the robots.txt rules of each domain, and compliance is mandatory.


# Contributing
    Contributions are welcome! Please follow these steps:
    Fork the repository.
    Create a feature branch (git checkout -b feature-name).
    Commit your changes (git commit -m 'Add new feature').
    Push to the branch (git push origin feature-name).
    Open a pull request.

# Contact
    For questions or feedback, please reach out to vaibhavlehra@gmail.com.

