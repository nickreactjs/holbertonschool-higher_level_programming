-- List all shows that have at least one genre linked.
-- tv_shows.title - tv_show_genres.genre_id
-- Sorted ascending by title and id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres
LEFT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
