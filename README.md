Just a little script I made that I use in conjunction with spotDL (https://github.com/spotDL/spotify-downloader). A lot of the time I download the entire discography of
a new artist that I've found and I wanted a way to sort all the MP3 files into directories named after each album. This does this successfully 90% of the time I've
 found. Often, it has trouble if spotDL fails to download the album name in the metadata, but it is good enough for me XD

 IMPORTANT:
 Often times an artist will have the same track appear on multiple albums / EPs. When this happens, the script falls over because multiple files have the same 
 name. To prevent this you just need to add "--options {title}+", "+{album}" to your spotDL command so that every file downloaded will have a unique name, like below.

 ![image](https://github.com/JpPjJp/MP3-Organiser/assets/40423237/d57d57f9-22d1-4e69-b5cc-c7e981326714)

 

EXAMPLE:
Lots of MP3s...

![image](https://github.com/JpPjJp/MP3-Organiser/assets/40423237/41469f9e-aa06-4432-9c6d-e216e047cb74)

Directories!

![image](https://github.com/JpPjJp/MP3-Organiser/assets/40423237/85bcf6fd-3e72-4000-84a9-c8f94bdf0e9c)
