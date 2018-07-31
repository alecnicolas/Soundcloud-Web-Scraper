from selenium import webdriver
import requests
import bs4
import os

#new, top, mix, track, artists urls
topUrl= "http://soundcloud.com/charts/top"
newUrl= "http://soundcloud.com/charts/new"
trackUrl= "http://soundcloud.com/search/sounds?q="
artistUrl= "http://soundcloud.com/search/people?q="
mixUrlEnd= "&filter.duration=epic"

#create selenium web browser
browser = webdriver.Chrome("C:/Users/Alec/Desktop/chromedriver.exe")
browser.get("https://soundcloud.com")

#main
print()
print("Python SoundCloud Scraper")

while True:
    print("Menu")
    print("1 - Search for Track")
    print("2 - Search for an artist")
    print("3 - Search for a mix")
    print("4 - Top Charts")
    print("5 - Hot Charts")
    print("0 - Exit")
    print()

    choice = int(input("Your choice:"))

    if choice == 0:
        browser.quit()
        break
    print()

    # search for a track
    if choice == 1:
        name = input("Name of the track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(trackUrl+name)
        continue
    # search artist
    if choice == 2:
        name = input("Name of the artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artistUrl+name)
        continue

    # search mix
    if choice == 3:
        name = input("Name of the mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(trackUrl+name+mixUrlEnd)
        continue

    # get top 50 tracks
    if choice == 4:
        request = requests.get(topUrl)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        print(request.text)

        genres = soup.select("a[href*=genre]")[2:]
        genreLinks = []

        # print out all available genres
        for index, genre in enumerate(genres):
            print(str(index)+": "+genre.text)
            genreLinks.append(genre.get("href"))

            print()
            choice = input("Your choice (x to go back to the main menu): ")
            print()

            if choice =="x":
                break
            else:
                choice = int(choice)

            url ="http://soundcloud.com"+genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")
            print(request.text)
            tracks = soup.select("h2")[3:]

            for track in tracks:
                print(track)

        # tracks = soup.select()

        # for genre in genres:
        #     print(genre)

print()
print("Goodbye!")
print()
