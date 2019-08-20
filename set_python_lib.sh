#!/bin/bash

docker-compose exec python3  python -m pip install numpy
docker-compose exec python3  python -m pip install pandas
docker-compose exec python3  python -m pip install matplotlib
docker-compose exec python3  python -m pip install networkx
docker-compose exec python3  python -m pip install pyyaml
docker-compose exec python3  python -m pip install xlsxwriter
docker-compose exec python3  python -m pip install tornado
docker-compose exec python3  python -m pip install pyperclip
docker-compose exec python3  python -m pip install requests
