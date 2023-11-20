docker-compose down
taskkill /f /fi "IMAGENAME eq Docker*" /T
taskkill /f /fi "IMAGENAME eq docker*" /T
wsl --shutdown