def image_search(search_query):
  import webbrowser

  firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
  firefox = webbrowser.Mozilla(firefox_path)

  links = [f"https://www.google.com/search?udm=2&q={search_query}"]
  for link in links:
    firefox.open(link)
