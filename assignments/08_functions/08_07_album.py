"""
Ian Tiggle
Chapter 8
Difficulty 5/10
"""

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title,
    }

    if songs:
        album['songs'] = songs

    return album


album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Ed Sheeran', 'Divide')
album3 = make_album('Adele', '25')
album4 = make_album('Michael Jackson', 'Thriller', 9)

print(album1)
print(album2)
print(album3)
print(album4)