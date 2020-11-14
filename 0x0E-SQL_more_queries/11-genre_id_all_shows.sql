-- SELECT ALL SHOWS
-- Sorted by ascending order title genre_id
-- if show doesnt have a genre display NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
