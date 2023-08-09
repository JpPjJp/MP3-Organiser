Just a little script I made that I use in conjunction with spotDL (https://github.com/spotDL/spotify-downloader). A lot of the time I download the entire discography of
a new artist that I've found and I wanted a way to sort all the MP3 files into directories named after each album. This does this successfully 90% of the time I've
 found. Often, it has trouble if spotDL fails to download the album name in the metadata, but it is good enough for me XD

 IMPORTANT:
 Often times an artist will have the same track appear on multiple albums / EPs. When this happens, the script falls over because multiple files have the same 
 name. To prevent this you just need to add "--options {title}+", "+{album}" to your spotDL command so that every file downloaded will have a unique name, like below.

 
