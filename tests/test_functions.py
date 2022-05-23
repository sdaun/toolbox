from toolbox.scraping import scrape

def test_scraping():
    assert scrape("https://www.google.com/") != None
