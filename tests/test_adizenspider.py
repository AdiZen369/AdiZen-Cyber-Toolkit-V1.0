import unittest
from adizen_cyber_toolkit import adizenspider


class TestAdiZenSpider(unittest.TestCase):
    def test_crawl_invalid_returns_list(self):
        links = adizenspider.crawl("http://invalid.localhost.test", limit=2)
        self.assertIsInstance(links, list)
        self.assertTrue(len(links) > 0)
        self.assertTrue(links[0].startswith("Error"))

    def test_crawl_limit_respected(self):
        # Even if successful, should not return more than limit
        links = adizenspider.crawl("https://example.com", limit=3)
        self.assertLessEqual(len(links), 3)


if __name__ == "__main__":
    unittest.main()
