use retos_viajes_app;

ALTER TABLE user AUTO_INCREMENT = 1;

INSERT INTO user (name, username, email, bio, total_points, auth_method, hashed_password, is_verified, created_at, updated_at)
VALUES
('Carlos López', 'carlos_lopez', 'carlos.lopez@example.com', 'Viajero apasionado', 1200, 'traditional', 'hashedpassword1', TRUE, NOW(), NOW()),
('María Fernández', 'maria_fernandez', 'maria.fernandez@example.com', 'Aventurera de corazón', 980, 'traditional', 'hashedpassword2', TRUE, NOW(), NOW()),
('Juan Pérez', 'juan_perez', 'juan.perez@example.com', 'Descubriendo el mundo', 1450, 'traditional', 'hashedpassword3', TRUE, NOW(), NOW()),
('Ana García', 'ana_garcia', 'ana.garcia@example.com', 'Exploradora empedernida', 1100, 'traditional', 'hashedpassword4', TRUE, NOW(), NOW()),
('Pedro Martínez', 'pedro_martinez', 'pedro.martinez@example.com', 'Amante de la naturaleza', 750, 'traditional', 'hashedpassword5', TRUE, NOW(), NOW()),
('Laura Sánchez', 'laura_sanchez', 'laura.sanchez@example.com', 'Conociendo nuevas culturas', 1250, 'traditional', 'hashedpassword6', TRUE, NOW(), NOW()),
('David Rodríguez', 'david_rodriguez', 'david.rodriguez@example.com', 'Fotógrafo de paisajes', 1350, 'traditional', 'hashedpassword7', TRUE, NOW(), NOW()),
('Sara Ramírez', 'sara_ramirez', 'sara.ramirez@example.com', 'Aventuras sin límites', 900, 'traditional', 'hashedpassword8', TRUE, NOW(), NOW()),
('Javier Torres', 'javier_torres', 'javier.torres@example.com', 'Buscando nuevos horizontes', 1020, 'traditional', 'hashedpassword9', TRUE, NOW(), NOW()),
('Isabel Gómez', 'isabel_gomez', 'isabel.gomez@example.com', 'Cazadora de atardeceres', 1150, 'traditional', 'hashedpassword10', TRUE, NOW(), NOW()),
('Roberto Díaz', 'roberto_diaz', 'roberto.diaz@example.com', 'Siempre en movimiento', 890, 'traditional', 'hashedpassword11', TRUE, NOW(), NOW()),
('Cristina Moreno', 'cristina_moreno', 'cristina.moreno@example.com', 'Planificando mi próximo viaje', 1330, 'traditional', 'hashedpassword12', TRUE, NOW(), NOW()),
('Alberto Jiménez', 'alberto_jimenez', 'alberto.jimenez@example.com', 'Viviendo el presente', 780, 'traditional', 'hashedpassword13', TRUE, NOW(), NOW()),
('Patricia Ruiz', 'patricia_ruiz', 'patricia.ruiz@example.com', 'En busca de nuevas experiencias', 1270, 'traditional', 'hashedpassword14', TRUE, NOW(), NOW()),
('Diego Herrera', 'diego_herrera', 'diego.herrera@example.com', 'Explorando el planeta', 1125, 'traditional', 'hashedpassword15', TRUE, NOW(), NOW()),
('Elena Castro', 'elena_castro', 'elena.castro@example.com', 'Siempre lista para una aventura', 980, 'traditional', 'hashedpassword16', TRUE, NOW(), NOW()),
('Francisco Ortega', 'francisco_ortega', 'francisco.ortega@example.com', 'Conquistando destinos', 1400, 'traditional', 'hashedpassword17', TRUE, NOW(), NOW()),
('Beatriz Vega', 'beatriz_vega', 'beatriz.vega@example.com', 'Pasaporte siempre listo', 860, 'traditional', 'hashedpassword18', TRUE, NOW(), NOW()),
('Alejandro Flores', 'alejandro_flores', 'alejandro.flores@example.com', 'Turista por naturaleza', 990, 'traditional', 'hashedpassword19', TRUE, NOW(), NOW()),
('Silvia Reyes', 'silvia_reyes', 'silvia.reyes@example.com', 'En busca de nuevos desafíos', 1080, 'traditional', 'hashedpassword20', TRUE, NOW(), NOW()),
('Oscar Medina', 'oscar_medina', 'oscar.medina@example.com', 'Explorador de ciudades', 920, 'traditional', 'hashedpassword21', TRUE, NOW(), NOW()),
('Marta Romero', 'marta_romero', 'marta.romero@example.com', 'Paisajes que enamoran', 1360, 'traditional', 'hashedpassword22', TRUE, NOW(), NOW()),
('Hugo Navarro', 'hugo_navarro', 'hugo.navarro@example.com', 'Siempre en busca de aventuras', 1240, 'traditional', 'hashedpassword23', TRUE, NOW(), NOW()),
('Clara Campos', 'clara_campos', 'clara.campos@example.com', 'Disfrutando cada viaje', 1190, 'traditional', 'hashedpassword24', TRUE, NOW(), NOW()),
('Fernando León', 'fernando_leon', 'fernando.leon@example.com', 'Enamorado de los viajes', 1045, 'traditional', 'hashedpassword25', TRUE, NOW(), NOW()),
('Paula Suárez', 'paula_suarez', 'paula.suarez@example.com', 'El mundo es mi hogar', 930, 'traditional', 'hashedpassword26', TRUE, NOW(), NOW()),
('Adrián Vázquez', 'adrian_vazquez', 'adrian.vazquez@example.com', 'Viviendo experiencias inolvidables', 1410, 'traditional', 'hashedpassword27', TRUE, NOW(), NOW()),
('Natalia Blanco', 'natalia_blanco', 'natalia.blanco@example.com', 'Siempre planeando el próximo destino', 1370, 'traditional', 'hashedpassword28', TRUE, NOW(), NOW()),
('Manuel Ríos', 'manuel_rios', 'manuel.rios@example.com', 'Mapas y brújula en mano', 950, 'traditional', 'hashedpassword29', TRUE, NOW(), NOW()),
('Andrea Cortés', 'andrea_cortes', 'andrea.cortes@example.com', 'Viajando sin límites', 1000, 'traditional', 'hashedpassword30', TRUE, NOW(), NOW());

ALTER TABLE destination AUTO_INCREMENT = 1;

INSERT INTO destination (city, country, description, image_url, active, created_at, updated_at)
VALUES
('Málaga', 'España', 'Ciudad costera con un clima increíble y una gran oferta cultural.', 'https://example.com/malaga.jpg', 1, NOW(), NOW()),
('Madrid', 'España', 'La capital de España, conocida por su vida nocturna y museos de renombre.', 'https://example.com/madrid.jpg', 1, NOW(), NOW()),
('Tokio', 'Japón', 'Una metrópoli vibrante con una mezcla de tradición y modernidad.', 'https://example.com/tokyo.jpg', 1, NOW(), NOW()),
('Roma', 'Italia', 'Historia, arte y la mejor gastronomía en un solo lugar.', 'https://example.com/roma.jpg', 1, NOW(), NOW());

ALTER TABLE category AUTO_INCREMENT = 1;

INSERT INTO category (name, description, icon_url)
VALUES
('Aventura', 'Actividades extremas y experiencias llenas de adrenalina.', 'https://example.com/adventure.png'),
('Cultura', 'Explora la historia, el arte y las tradiciones de diferentes lugares.', 'https://example.com/culture.png'),
('Gastronomía', 'Descubre los sabores únicos de cada destino.', 'https://example.com/food.png'),
('Naturaleza', 'Conexión con la fauna, flora y paisajes impresionantes.', 'https://example.com/nature.png');

ALTER TABLE challenge AUTO_INCREMENT = 1;

INSERT INTO challenge (category_id, destination_id, title, short_description, long_description, image_url, points, difficulty, active, created_at, updated_at, latitude, longitude)
VALUES
-- Málaga
(1, 1, 'Escalada en El Chorro', 'Súbete a las rocas en un entorno increíble.', 'El Chorro es uno de los lugares más famosos para la escalada en España.', 'https://example.com/elchorro.jpg', 100, 3, 1, NOW(), NOW(), 36.9200, -4.7600),
(2, 1, 'Visita la Alcazaba', 'Explora la historia de Málaga.', 'Un castillo musulmán con vistas espectaculares de la ciudad.', 'https://example.com/alcazaba.jpg', 50, 2, 1, NOW(), NOW(), 36.7213, -4.4152),
(3, 1, 'Ruta de tapas en el centro', 'Descubre los mejores sabores de Málaga.', 'Desde espetos hasta vino dulce, prueba lo mejor de la gastronomía local.', 'https://example.com/tapas.jpg', 80, 2, 1, NOW(), NOW(), 36.7213, -4.4213),
(4, 1, 'Caminata por el Caminito del Rey', 'Disfruta de la naturaleza en un sendero único.', 'Uno de los senderos más impresionantes de España, rodeado de paisajes increíbles.', 'https://example.com/caminito.jpg', 120, 4, 1, NOW(), NOW(), 36.9310, -4.7722),

-- Madrid
(1, 2, 'Parapente en la Sierra', 'Siente la adrenalina volando sobre Madrid.', 'Sobrevuela la Sierra de Madrid y disfruta de vistas únicas.', 'https://example.com/parapente.jpg', 150, 4, 1, NOW(), NOW(), 40.7311, -3.6904),
(2, 2, 'Tour por el Prado', 'Explora el museo más famoso de España.', 'Descubre obras de Goya, Velázquez y más.', 'https://example.com/prado.jpg', 60, 1, 1, NOW(), NOW(), 40.4138, -3.6921),
(3, 2, 'Cata de vinos en Lavapiés', 'Prueba vinos españoles en un barrio bohemio.', 'Disfruta de una selección de vinos locales en un ambiente relajado.', 'https://example.com/vinos.jpg', 90, 2, 1, NOW(), NOW(), 40.4077, -3.7033),
(4, 2, 'Excursión al Parque del Retiro', 'Relájate y explora uno de los parques más bonitos.', 'Navega en el estanque, pasea por los jardines y descubre su historia.', 'https://example.com/retiro.jpg', 70, 1, 1, NOW(), NOW(), 40.4154, -3.6846),

-- Tokio
(1, 3, 'Escalada en el Monte Takao', 'Sube a la cima y disfruta de la vista.', 'Un reto físico con una gran recompensa visual.', 'https://example.com/takao.jpg', 110, 3, 1, NOW(), NOW(), 35.6311, 139.2437),
(2, 3, 'Explora el Templo Senso-ji', 'Visita el templo más antiguo de Tokio.', 'Sumérgete en la historia y cultura japonesa.', 'https://example.com/sensoji.jpg', 50, 2, 1, NOW(), NOW(), 35.7148, 139.7967),
(3, 3, 'Prueba sushi en Tsukiji', 'Disfruta del sushi más fresco.', 'Un must para los amantes de la comida japonesa.', 'https://example.com/sushi.jpg', 100, 2, 1, NOW(), NOW(), 35.6655, 139.7706),
(4, 3, 'Senderismo en el Monte Fuji', 'Una experiencia inolvidable.', 'El reto definitivo para cualquier aventurero.', 'https://example.com/fuji.jpg', 200, 5, 1, NOW(), NOW(), 35.3606, 138.7274),

-- Roma
(1, 4, 'Explora las catacumbas', 'Atrévete a descubrir el pasado subterráneo.', 'Un recorrido lleno de historia y misterio.', 'https://example.com/catacumbas.jpg', 80, 3, 1, NOW(), NOW(), 41.8575, 12.5118),
(2, 4, 'Tour por el Coliseo', 'El anfiteatro más famoso del mundo.', 'Revive la época de los gladiadores.', 'https://example.com/coliseo.jpg', 60, 1, 1, NOW(), NOW(), 41.8902, 12.4922),
(3, 4, 'Degustación de pasta en Trastevere', 'La mejor pasta de Italia.', 'Prueba diferentes tipos de pasta en un barrio emblemático.', 'https://example.com/pasta.jpg', 100, 2, 1, NOW(), NOW(), 41.8905, 12.4768),
(4, 4, 'Excursión a Villa Borghese', 'Disfruta de la naturaleza y el arte.', 'Un parque con jardines impresionantes y museos de clase mundial.', 'https://example.com/borghese.jpg', 70, 1, 1, NOW(), NOW(), 41.9131, 12.4923);

ALTER TABLE trip AUTO_INCREMENT = 1;

INSERT INTO trip (user_id, destination_id, start_date, end_date, status, created_at)
VALUES
-- Trip para el antepenúltimo usuario a Málaga
(28, 1, '2025-06-10 10:00:00', '2025-06-20 18:00:00', 'planned', NOW()),

-- Trip para el penúltimo usuario a Madrid
(29, 2, '2025-07-05 09:30:00', '2025-07-12 17:45:00', 'ongoing', NOW()),

-- Trip para el último usuario a Roma
(30, 4, '2025-08-15 08:00:00', '2025-08-22 20:30:00', 'completed', NOW());

-- Insertar categorías para el trip de cada usuario
INSERT INTO trip_category (trip_id, category_id)
VALUES
-- Categorías para el trip del usuario 28 (Málaga)
(1, 1),
(1, 2),
(1, 3),
(1, 4),

-- Categorías para el trip del usuario 29 (Madrid)
(2, 1),
(2, 2),
(2, 3),
(2, 4),

-- Categorías para el trip del usuario 30 (Roma)
(3, 1),
(3, 2),
(3, 3),
(3, 4);

-- Insertar los challenges para cada trip
INSERT INTO trip_challenge (trip_id, challenge_id)
VALUES
-- Challenges para el trip del usuario 28 (Málaga)
(1, 1),  -- Challenge de la categoría 1 para Málaga
(1, 2),  -- Challenge de la categoría 2 para Málaga
(1, 3),  -- Challenge de la categoría 3 para Málaga
(1, 4),  -- Challenge de la categoría 4 para Málaga

-- Challenges para el trip del usuario 29 (Madrid)
(2, 5),  -- Challenge de la categoría 1 para Madrid
(2, 6),  -- Challenge de la categoría 2 para Madrid
(2, 7),  -- Challenge de la categoría 3 para Madrid
(2, 8),  -- Challenge de la categoría 4 para Madrid

-- Challenges para el trip del usuario 30 (Roma)
(3, 13), -- Challenge de la categoría 1 para Roma
(3, 14), -- Challenge de la categoría 2 para Roma
(3, 15), -- Challenge de la categoría 3 para Roma
(3, 16); -- Challenge de la categoría 4 para Roma

ALTER TABLE completed_challenge AUTO_INCREMENT = 1;

-- Insertar los CompletedChallenges para el usuario 28 (Málaga)
INSERT INTO completed_challenge (user_id, challenge_id, trip_id, completed_at, description)
VALUES
(28, 1, 1, NOW(), 'Completado el reto de categoría 1 en Málaga'),
(28, 2, 1, NOW(), 'Completado el reto de categoría 2 en Málaga'),
(28, 3, 1, NOW(), 'Completado el reto de categoría 3 en Málaga'),
(28, 4, 1, NOW(), 'Completado el reto de categoría 4 en Málaga');

-- Insertar los CompletedChallenges para el usuario 29 (Madrid)
INSERT INTO completed_challenge (user_id, challenge_id, trip_id, completed_at, description)
VALUES
(29, 5, 2, NOW(), 'Completado el reto de categoría 1 en Madrid'),
(29, 6, 2, NOW(), 'Completado el reto de categoría 2 en Madrid'),
(29, 7, 2, NOW(), 'Completado el reto de categoría 3 en Madrid'),
(29, 8, 2, NOW(), 'Completado el reto de categoría 4 en Madrid');

-- Insertar los CompletedChallenges para el usuario 30 (Roma)
INSERT INTO completed_challenge (user_id, challenge_id, trip_id, completed_at, description)
VALUES
(30, 13, 3, NOW(), 'Completado el reto de categoría 1 en Roma'),
(30, 14, 3, NOW(), 'Completado el reto de categoría 2 en Roma'),
(30, 15, 3, NOW(), 'Completado el reto de categoría 3 en Roma'),
(30, 16, 3, NOW(), 'Completado el reto de categoría 4 en Roma');
