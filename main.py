import bs4
import requests


result = requests.get("https://kushkaushik14.github.io")
soup = bs4.BeautifulSoup(result.text, "lxml")

songFav = soup.select("iframe")[0]
links = songFav["src"]

print('Favourite song:\n')
print(links)

movieFav = soup.select("iframe")[1]
links1 = movieFav["src"]
print('\n\nFavourite movie:\n')
print(links1)

print("\n\n\n\n\n")
songFav1 = str(songFav)
songFav2 = songFav1.replace('width="100%"', 'width="50%"')

print(songFav2)
print('\n\n')	

movieFav1 = str(movieFav)
movieFav2 = movieFav1.replace('width="1024"', 'width="50%"')

print(movieFav2)

file = open("index.html","r+")
file.truncate(0)
file.close()

with open("index.html", "a") as f:
	f.write('<html>')
	f.write('<head>')
	f.write("<title>Made By Mannat</title>")
	f.write('</head>')
	f.write('<body style="background-color: #121212; color: wheat">')
	f.write("<h1>Kush's Fav (Made by Mannat):</h1>")
	f.write("His fav song is: <br><br>")
	f.write(str(songFav2))
	f.write("<br> His fav movie is: <br><br>")
	f.write(str(movieFav2))
	f.write('</body>')
	f.write('</html>')
	f.close()