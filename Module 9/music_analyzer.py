# Brett M.
# INFOTC 4401-01
# Challenge: Music Analyzer

from collections import OrderedDict

# Function to open, read, copy text, and close file chosen by user.
def retrieveFile():
    file_lines = []

    file_name = input("Please enter the name of the file: ")
    file = open(file_name, "r", encoding = "utf-16")
    for line in file:
        line = line.split("\t")
        file_lines.append(line)
    file.close()
    return file_lines

# Function to find the name of all songs in the list.
def find_song_name(file):
    song_name_list = []
    for index in file:
        song_name = index[0]
        song_name_list.append(song_name)

    return song_name_list

# Function to find total number of songs in file.
def find_number_of_songs(file):
    song_total = len(file)
    print("Total number of songs: {}\n".format(song_total))

    return song_total

# Function of determine number of songs released each year.
def number_songs_released_each_year(file):
    songs_each_year = {}

    for song in file:
        year = song[16]
        if year == "":
            year = "Unknown"
        if year in songs_each_year:
            songs_each_year[year] += 1
        else:
            songs_each_year[year] = 1

    return songs_each_year

# Function to find the Name & Artist of the longest song in playlist.
def find_longest_song(file):
    time = 0
    song_index = []
    counter = 0

    for song in file:
        try:
            song_time = int(song[11])
            if song_time > time:
                time = song_time
                song_index = [counter]
                counter += 1
            elif song_time == time:
                song_index.append(counter)
                counter += 1
            else:
                counter += 1
                continue
        except:
            continue

    longest_song = {}
    for index in song_index:
        song = file[index]
        longest_song[song[0]] = song[1]

    return longest_song

# Function to find the Name & Artist of the shortest song in the playlist.
def find_shortest_song(file):
    time = 999999999999
    song_index = []
    counter = 0

    for song in file:
        try:
            song_time = int(song[11])
            if song_time < time:
                time = song_time
                song_index = [counter]
                counter += 1
            elif song_time == time:
                song_index.append(counter)
                counter += 1
            else:
                counter += 1
                continue
        except:
            continue

    shortest_song = {}
    for index in song_index:
        song = file[index]
        shortest_song[song[0]] = song[1]

    return shortest_song

# Function to find the number of songs/longest & shortest songs per genre.
def find_genre_data(file):
    genre_list = []
    genres_found = []
    counter = 0

    for song in file:
        genre = song[9]
        if genre == "":
            genre = "Unknown genre"
        try:
            song_time = int(song[11])
        except:
            continue
        song_name = song[0]
        song_artist = song[1]

        if genre in genres_found:
            for nested_list in genre_list:
                if nested_list[0] == genre:
                    nested_list[1] += 1
                    if song_time > nested_list[2]:
                        nested_list[4] = {song_name:song_artist}
                        nested_list[2] = song_time
                    elif song_time == nested_list[2]:
                        genre_longest_song = nested_list[4]
                        genre_longest_song[song_name] = song_artist

                    if song_time < nested_list[3]:
                        nested_list[5] = {song_name:song_artist}
                        nested_list[3] = song_time
                    elif song_time == nested_list[3]:
                        genre_shortest_song = nested_list[5]
                        genre_shortest_song[song_name] = song_artist
        else:
            genre_list.append([genre, 1, song_time, song_time, {song_name:song_artist}, {song_name:song_artist}])
            genres_found.append(genre)


    for genre in genre_list:
        print(genre)

# Function to determine if the song has been played or not.

# Function to display songs released each year data.
def display_songs_each_year_data(song_years_dict):
    song_year_ordered_dict = OrderedDict(sorted(song_years_dict.items(), key=lambda key:key[0]))
    print("Number of songs release each year in playslist: ")
    for key, value in song_year_ordered_dict.items():
        print("   {} : {}".format(key,value))



file = retrieveFile()
file.pop(0)
for song in file:
    print(song, "\n")

find_song_name(file)
find_number_of_songs(file)
song_years_dict = number_songs_released_each_year(file)
overall_longest_song = find_longest_song(file)
overall_shortest_song = find_shortest_song(file)
find_genre_data(file)
display_songs_each_year_data(song_years_dict)
