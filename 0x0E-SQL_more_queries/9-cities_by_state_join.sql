-- Lists all cities contained in the database

SELECT cities.id, cities.name, state.name AS name FROM cities JOIN states ON cities.states_id = states.id ORDER BY  cities.id ASC;
