# Brett M.
# INFOTC 4401-01
# Challenge: Music Analyzer

def retrieveFile():
    file_lines = []

    file_name = input("Please enter the name of the file: ")
    file = open(file_name, "r", encoding = "utf-16")
    for line in file:
        line = line.split("\t")
        file_lines.append(line)
    file.close()
    return file_lines

def find_song_name(file):
    song_name_list = []
    for index in file:
        song_name = index[0]
        song_name_list.append(song_name)

    return song_name_list

def find_number_of_songs(file):
    song_total = len(file)
    print(song_total)

    return song_total

def number_songs_released_each_year(file):
    songs_each_year = {}
    for song in file:
        year = song[16]
        if year in songs_each_year:
            songs_each_year[year] += 1
        else:
            songs_each_year[year] = 1

    print(songs_each_year.items())

file = retrieveFile()
file.pop(0)
for song in file:
    print(song, "\n")
find_song_name(file)
find_number_of_songs(file)
number_songs_released_each_year(file)
