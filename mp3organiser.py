import music_tag
import os
import eyed3
import shutil

path = input("Enter path to the directory containing the MP3s (Example: \"D:\\Music\\Interpol\")")

audiofiles = []
music_tag_filesd3 = []
albums = []
og_album_names = []
unique_albums = []
directories = []
print(path)

#Getting the unique album names from a list of songs
for item in os.listdir(path):
    if item.endswith('.mp3'):
        audiofiles.append(path + "\\" +item)
        
for song in audiofiles:
    music_tag_filesd3.append(eyed3.load(song))
    
for song in music_tag_filesd3:
    og_album_names.append(song.tag.album)

    if ":" in song.tag.album:
        valid_album_name = song.tag.album.replace(":", "")
        albums.append(valid_album_name)
    elif "/" in song.tag.album:
        valid_album_name = song.tag.album.replace("/", "")
        albums.append(valid_album_name)
    elif "\\" in song.tag.album:
        valid_album_name = song.tag.album.replace("\\", "")
        albums.append(valid_album_name)
    elif "\"" in song.tag.album:
        valid_album_name = song.tag.album.replace("\"", "")
        albums.append(valid_album_name)
    elif "*" in song.tag.album:
        valid_album_name = song.tag.album.replace("*", "")
        albums.append(valid_album_name)
    elif "|" in song.tag.album:
        valid_album_name = song.tag.album.replace("|", "")
        albums.append(valid_album_name)
    elif ">" in song.tag.album:
        valid_album_name = song.tag.album.replace(">", "")
        albums.append(valid_album_name)
    elif "<" in song.tag.album:
        valid_album_name = song.tag.album.replace("<", "")
        albums.append(valid_album_name)
    elif "?" in song.tag.album:
        valid_album_name = song.tag.album.replace("?", "")
        albums.append(valid_album_name)
    else:
        valid_album_name = song.tag.album
        albums.append(valid_album_name)


unique_albums = sorted(list(set(albums)))
unique_albums_og = sorted(list(set(og_album_names)))
print(music_tag_filesd3[1])
print(unique_albums, unique_albums_og)

#Making directories of all unqiue albums
for album in unique_albums:
   os.mkdir(path + "\\" + str(album.replace(":", " ")))


#Moving songs into correct directory
for song in music_tag_filesd3:
    song_split = str(song).rsplit("\\")
    #choose correct album name
    album_name =  ""
    for i in range(len(unique_albums)):
        if song.tag.album == unique_albums_og[i]:
            album_name = unique_albums[i]
            break
        else:
            continue
    shutil.move(str(song), song_split[0] + "\\" + song_split[1] + "\\" + song_split[2] + "\\" + album_name + "\\" + song_split[3])
