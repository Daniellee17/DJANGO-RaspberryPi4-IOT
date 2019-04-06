drop table if exists myDB;

create table myDB (
 sensorTemp text,
 sensorHum text,
 sensorMoist text
);

INSERT INTO myDB (sensorTemp, sensorHum, sensorMoist) VALUES ("10", "20", "30");

