#!/bin/zsh

# Abre la primera terminal para el maestro
kitty --hold --title "Master" sh -c "
    sleep 1;
    echo 'Uploading to master...';
    pio run -e master -t upload;
    echo 'Starting monitor for master...';
    pio device monitor -p /dev/ttyACM0 -b 9600" &

# Abre la segunda terminal para la estación 1
kitty --hold --title "Station_1" sh -c "
    sleep 1;
    echo 'Uploading to station1...';
    pio run -e station1 -t upload;
    echo 'Starting monitor for station1...';
    pio device monitor -p /dev/ttyACM1 -b 9600" &

# Abre la tercera terminal para la estación 2
kitty --hold --title "Station_2" sh -c "
    sleep 1;
    echo 'Uploading to station2...';
    pio run -e station2 -t upload;
    echo 'Starting monitor for station2...';
    pio device monitor -p /dev/ttyACM2 -b 9600" &

# Espera un momento para asegurarse de que las terminales se abran
sleep 2

# Cierra la terminal de origen
exit