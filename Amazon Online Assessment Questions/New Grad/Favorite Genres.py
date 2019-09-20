def solution(userSongs, genreSongs):
    songGenres = {}
    for genre in genreSongs:
        for song in genreSongs[genre]:
            songGenres[song] = genre

    results = {user: [] for user in userSongs}

    for user in userSongs:
        favouriteGenres = {}
        maxValue = 0
        for song in userSongs[user]:
            genre = songGenres[song]

            if genre in favouriteGenres:
                favouriteGenres[genre] += 1
            else:
                favouriteGenres[genre] = 1

            maxValue = max(maxValue, favouriteGenres[genre])

        for fav in favouriteGenres:
            if favouriteGenres[fav] == maxValue:
                results[user].append(fav)

    return results

userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

print(solution(userSongs, songGenres))
