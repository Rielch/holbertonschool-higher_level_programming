-- Lists all genres and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_show_genres.genre_id is NOT NULL ORDER BY number_of_shows DESC;
