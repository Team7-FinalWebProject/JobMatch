docker-compose down
wsl --shutdown
taskkill /f /fi "IMAGENAME eq Docker*" /T
taskkill /f /fi "IMAGENAME eq docker*" /T