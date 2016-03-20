from bs4 import BeautifulSoup
import urllib2

url = "http://www.cricbuzz.com/cricket-match/live-scores"
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, 'html.parser')
soup.prettify().encode('UTF-8')

live_matches = soup.find_all('div', attrs={'class': 'cb-lv-main'})

print
print('Cricbuzz Live Updates\n----------------------')
print

for match in live_matches:
	print(match.find('div', attrs={'class': 'cb-schdl'}).find('a').text) + ': ',
	try:
		print(match.find('div', attrs={'class': 'cb-text-complete'}).text)
	except:
		print('Match Scheduled')
	print