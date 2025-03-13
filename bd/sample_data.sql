use retos_viajes_app;
ALTER TABLE destination AUTO_INCREMENT = 1;
ALTER TABLE category AUTO_INCREMENT = 1;
INSERT INTO destination (city, country, description, image_url, active) VALUES
('París', 'Francia', 'La ciudad del amor', 'paris.jpg', 1),
('Tokio', 'Japón', 'La capital del sol naciente', 'tokio.jpg', 1),
('Nueva York', 'EE.UU.', 'La gran manzana', 'nueva_york.jpg', 1);

INSERT INTO category (name, description, icon_url) VALUES
('Aventura', 'Desafíos para los amantes de la adrenalina', 'aventura.png'),
('Gastronomía', 'Prueba platillos típicos de la región', 'gastronomia.png'),
('Cultura', 'Explora la historia y tradiciones locales', 'cultura.png');

INSERT INTO challenge (category_id, destination_id, title, short_description, long_description, image_url, points, difficulty, active, latitude, longitude) VALUES
-- Retos para París
(1, 1, 'Subir a la Torre Eiffel', 'Llega a la cima y toma una foto', 'Disfruta de la vista panorámica de París desde la Torre Eiffel', 'torre_eiffel.jpg', 50, 3, 1,  48.8584, 2.2945),
(1, 1, 'Recorrer el Sena en kayak', 'Explora París desde el agua', 'Disfruta de una vista única desde el río Sena', 'kayak_sena.jpg', 60, 4, 1, 48.8566, 2.3522),
(2, 1, 'Probar caracoles franceses', 'Degusta este platillo típico', 'Atrévete a probar los caracoles en un restaurante tradicional', 'caracoles.jpg', 40, 2, 1,  48.8566, 2.3522),
(2, 1, 'Visitar una panadería y probar croissants', 'Disfruta de la mejor repostería francesa', 'Encuentra la mejor panadería y prueba un croissant recién hecho', 'croissant.jpg', 30, 1, 1, 48.8566, 2.3522),
(3, 1, 'Explorar el Louvre', 'Descubre el museo más famoso del mundo', 'Admira la Mona Lisa y muchas otras obras de arte', 'louvre.jpg', 50, 3, 1, 48.8606, 2.3376),
(3, 1, 'Asistir a un espectáculo en el Moulin Rouge', 'Sumérgete en la cultura parisina', 'Disfruta de un espectáculo de cabaret en este icónico lugar', 'moulin_rouge.jpg', 45, 3, 1, 48.8841, 2.3325),

-- Retos para Tokio
(1, 2, 'Subir al Monte Takao', 'Llega a la cima y disfruta la vista', 'Explora esta montaña cercana a Tokio', 'monte_takao.jpg', 60, 4, 1, 35.6251, 139.2430),
(1, 2, 'Explorar el cruce de Shibuya', 'Cruza la intersección más famosa del mundo', 'Vive la experiencia de caminar por el icónico cruce', 'shibuya.jpg', 30, 1, 1, 35.6595, 139.7006),
(2, 2, 'Comer sushi auténtico', 'Prueba sushi en un restaurante tradicional', 'Disfruta del sushi preparado por un maestro en Tokio', 'sushi_tokio.jpg', 30, 2, 1, 35.6895, 139.6917),
(2, 2, 'Tomar té en una ceremonia japonesa', 'Vive la experiencia de una auténtica ceremonia del té', 'Descubre la tradición y significado del té en Japón', 'ceremonia_te.jpg', 40, 2, 1, 35.6895, 139.6917),
(3, 2, 'Visitar el Templo Senso-ji', 'Descubre uno de los templos más antiguos de Tokio', 'Explora la historia y cultura japonesa en este templo', 'sensoji.jpg', 45, 3, 1, 35.7148, 139.7967),
(3, 2, 'Asistir a un espectáculo de sumo', 'Observa una pelea de sumo en vivo', 'Conoce este deporte tradicional japonés', 'sumo.jpg', 50, 3, 1, 35.6947, 139.7800),

-- Retos para Nueva York
(1, 3, 'Subir al Empire State', 'Disfruta la vista desde la cima', 'Admira el skyline de Nueva York desde lo alto', 'empire_state.jpg', 50, 3, 1, 40.7488, -73.9854),
(1, 3, 'Recorrer Central Park en bicicleta', 'Explora el parque más famoso de Nueva York', 'Disfruta de un paseo en bicicleta por sus senderos', 'central_park.jpg', 40, 2, 1, 40.7851, -73.9683),
(2, 3, 'Comer una pizza estilo Nueva York', 'Prueba una auténtica rebanada de pizza neoyorquina', 'Encuentra la mejor pizzería y disfruta una slice', 'pizza_ny.jpg', 30, 1, 1, 40.7128, -74.0060),
(2, 3, 'Visitar un mercado de comida callejera', 'Prueba diferentes platillos en un food market', 'Descubre la diversidad gastronómica de Nueva York', 'food_market.jpg', 35, 2, 1, 40.7128, -74.0060),
(3, 3, 'Visitar la Estatua de la Libertad', 'Tómate una foto con la estatua', 'Explora la icónica Estatua de la Libertad en Nueva York', 'estatua_libertad.jpg', 40, 2, 1, 40.6892, -74.0445),
(3, 3, 'Asistir a un musical en Broadway', 'Disfruta de una obra en el distrito teatral más famoso', 'Vive la magia del teatro en Broadway', 'broadway.jpg', 50, 3, 1, 40.7590, -73.9845);
