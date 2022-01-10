import time
import pafy
from selenium import webdriver


count = int(input("Number of times to be repeated: "))
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

refreshrate = None

driver = webdriver.Firefox()

try:
	video = pafy.new(url)
	if hasattr(video, 'length'):
		refreshrate = video.length
except Exception as e:
	print(e)
	print("Length of video:")
	minutes = int(input("Minutes "))
	seconds = int(input("Seconds "))
	refreshrate = minutes * 60 + seconds


if url.startswith("https://"):
    driver.get(url)
else:

    driver.get("https://" + url)

for i in range(count):
    time.sleep(refreshrate)
    driver.refresh()

