# Brett M.
# INFOTC 4401-01
# Challenge: Music Analyzer

from collections import OrderedDict

# Function to open, read, copy text, and close file chosen by user.
def retrieveFile():
    file_lines = []

    while True:
        try:
            file_name = input("\nPlease enter the name of the file: ")
            file = open(file_name, "r", encoding = "utf-16")
            break
        except:
            continue
    for line in file:
        line = line.split("\t")
        file_lines.append(line)
    file.close()

    return file_lines

# Function to find total number of songs in file.
def find_number_of_songs(file):
    song_total = len(file)

    return song_total

# Function of determine number of songs released each year.
def number_songs_released_each_year(file):
    songs_each_year = {}

    for song in file:
        year = song[16]
        if year == "":
            year = "Unknown Year"
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

    return genre_list

# Function to determine if the song has been played or not.
def find_if_song_played(file):
    song_played = [0,0]

    for song in file:
        if song[25] == "":
             song_played[0] += 1
        else:
            song_played[1] += 1

    return song_played

# Function to display songs released each year data.
def display_all_data(total, song_per_year, long_song, short_song, genre_data, song_played):
    print("\n\n**** Music Playlist Data ****\n")
    print("Total number of songs in the playlist: {}\n".format(total))
    song_year_ordered_dict = OrderedDict(sorted(song_years_dict.items(), key=lambda key:key[0]))
    print("Number of songs released each year in playslist: ")
    for key, value in song_year_ordered_dict.items():
        print("   {} : {}".format(key,value))
    for key, value in long_song.items():
        if value == "":
            value = "Unknown Artist"
        print("\nThe longest song in the playlist:\n   Name: {}\n   Artist: {}".format(key,value))
    for key, value in short_song.items():
        if value == "":
            value = "Unknown Artist"
        print("\nThe shortest song in the playlist:\n   Name: {}\n   Artist: {}".format(key,value))
    print("\nGenre specific data:")
    for genre in genre_data:
        long_name_artist = genre[4]
        short_name_artist = genre[5]
        song_count = genre[1]

        print("\n   Number of {} songs in playlist: {}".format(genre[0], genre[1]))
        if song_count == 1:
            for key, value in long_name_artist.items():
                if value == "":
                    value = "Unknown Artist"
                print("\tLongest & shortest {} song in playlist:\n   \t   Name: {}\n   \t   Artist: {}".format(genre[0],key,value))
        else:
            for key, value in long_name_artist.items():
                if value == "":
                    value = "Unknown Artist"
                print("\tLongest {} song in playlist:\n   \t   Name: {}\n   \t   Artist: {}".format(genre[0],key,value))
            for key, value in short_name_artist.items():
                if value == "":
                    value = "Unknown Artist"
                print("\tShortest {} song in playlist:\n   \t   Name: {}\n   \t   Artist: {}".format(genre[0],key,value))
    print("\nSong play data:")
    print("   Number of songs played: {}".format(song_played[1]))
    print("   Number of songs not yet played: {}\n".format(song_played[0]))




print("*****************************")
print("* Welcome to Music Analyzer *")
print("*****************************\n")

while True:
    file = retrieveFile()
    file.pop(0)

    total_number_of_songs = find_number_of_songs(file)
    song_years_dict = number_songs_released_each_year(file)
    overall_longest_song = find_longest_song(file)
    overall_shortest_song = find_shortest_song(file)
    genre_data = find_genre_data(file)
    is_song_played = find_if_song_played(file)

    display_all_data(total_number_of_songs, song_years_dict,overall_longest_song,overall_shortest_song,genre_data,is_song_played)

    answer = input("Would you like to analyze another song? (y/n) ")
    if answer == 'y':
        continue
    else:
        print("\nHave a great day!\n")
        break
