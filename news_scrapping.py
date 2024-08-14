from requests_html import HTMLsession

mySession = HTMLSession()
topStoriesUrl = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

renderPage = mySession.get(topStoriesUrl)
renderPage.html.render(sleep = 1, scrowdown = 3)



