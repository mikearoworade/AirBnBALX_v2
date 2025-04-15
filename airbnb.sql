-- Create the database
CREATE DATABASE IF NOT EXISTS airbnb_clone;

-- Use the database
USE airbnb_clone;

-- Table: User
CREATE TABLE IF NOT EXISTS User (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128)
);

-- Table: State
CREATE TABLE IF NOT EXISTS State (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL
);

-- Table: City
CREATE TABLE IF NOT EXISTS City (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES State(id) ON DELETE CASCADE
);

-- Table: Place
CREATE TABLE IF NOT EXISTS Place (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    number_rooms INT DEFAULT 0,
    number_bathrooms INT DEFAULT 0,
    max_guest INT DEFAULT 0,
    price_by_night INT DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES City(id) ON DELETE CASCADE
);

-- Table: Amenity
CREATE TABLE IF NOT EXISTS Amenity (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL
);

-- Table: PlaceAmenity (Many-to-Many relationship table)
CREATE TABLE IF NOT EXISTS PlaceAmenity (
    place_id VARCHAR(60) NOT NULL,
    amenity_id VARCHAR(60) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id) ON DELETE CASCADE
);

-- Table: Review
CREATE TABLE IF NOT EXISTS Review (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    place_id VARCHAR(60) NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE
);


