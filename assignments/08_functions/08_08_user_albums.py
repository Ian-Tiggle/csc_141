"""
Ian Tiggle
Chapter 8
Difficulty 4/10
"""

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title
    }

    if songs is not None:
        album['songs'] = songs

    return album


while True:
    print("\nEnter album information ('q' to quit).")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

make_album()