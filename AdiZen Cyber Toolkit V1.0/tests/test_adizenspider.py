import unittest
import tools.adizenspider as spider

class TestAdiZenSpider(unittest.TestCase):
    def test_crawl_invalid(self):
        links = spider.crawl("http://invalid.localhost", limit=2)
        self.assertTrue(isinstance(links, list))

if __name__ == "__main__":
    unittest.main()