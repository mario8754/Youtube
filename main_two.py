
import webbrowser
import time


url = "https://www.youtube.com/watch?v=SFH6fzRly7g"

views = 10

duration = 20

for i in range(int(views)):

    webbrowser.open_new(url)

    time.sleep(int(duration))
