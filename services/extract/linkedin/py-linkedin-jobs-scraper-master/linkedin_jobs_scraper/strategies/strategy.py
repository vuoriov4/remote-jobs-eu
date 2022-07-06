from selenium import webdriver
from ..chrome_cdp import CDP
from ..query import Query


class Strategy:
    def __init__(self, scraper: 'LinkedinScraper'):
        self.scraper = scraper

    def run(
        self,
        driver: webdriver,
        cdp: CDP,
        search_url: str,
        query: Query,
        location: str,
        apply_link: bool
    ) -> None:
        raise NotImplementedError('Must implement method in subclass')
