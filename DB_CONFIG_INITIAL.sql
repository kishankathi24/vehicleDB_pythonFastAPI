use vehiclesdb;

CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    lock_status VARCHAR(10) NOT NULL,
    current_speed VARCHAR(10) NOT NULL,
    battery_level VARCHAR(10) NOT NULL,
    status ENUM('PARKING', 'MOVING', 'IDLING', 'TOWING') NOT NULL,
    location VARCHAR(50) NOT NULL,
    last_updated DATETIME NOT NULL
);

INSERT INTO vehicles (vehicle_id, type, lock_status, current_speed, battery_level, status, location, last_updated)
VALUES
(132456, 'Scooter', 'Lock', '0 km/h', '100%', 'PARKING', '3.142,012', '2019-07-02 09:00:00'),
(987654, 'Scooter', 'Unlock', '5 km/h', '75%', 'MOVING', '2.125,114', '2019-07-02 10:00:00'),
(569825, 'Scooter', 'Unlock', '0 km/h', '50%', 'IDLING', '4.125,114', '2019-07-02 10:00:00'),
(125864, 'Scooter', 'Lock', '0 km/h', '15%', 'TOWING', '5.125,114', '2019-07-02 10:00:00'),
(125865, 'Scooter', 'Lock', '0 km/h', '0%', 'TOWING', '5.125,114', '2019-07-02 10:00:00');