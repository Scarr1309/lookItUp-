from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Create an HTML session
mySession = HTMLSession()
topStoriesUrl = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

try:
    # Fetch the page
    renderPage = mySession.get(topStoriesUrl)

    # Render the page with some sleep time and scroll down to ensure content loads
    renderPage.html.render(sleep=1, scrolldown=1)  

    articleTags = renderPage.html.find('article')

    for tag in articleTags:
      aTags = tag.find('a')
      if(len(aTags) >= 2):
        newsArticle = aTags[1]
        newsTitle = newsArticle.text
        titleLink = newsArticle.absolute_links
        print(newsTitle, titleLink)
      else:
         continue
        
            
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    mySession.close()
