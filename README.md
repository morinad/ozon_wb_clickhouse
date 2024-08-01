# ozon_wb_clickhouse

### Получаем нужную версию Clichouse:
wget https://github.com/ClickHouse/ClickHouse/releases/download/v24.6.2.17-stable/clickhouse-common-static_24.6.2.17_amd64.deb

wget https://github.com/ClickHouse/ClickHouse/releases/download/v24.6.2.17-stable/clickhouse-server_24.6.2.17_amd64.deb

wget https://github.com/ClickHouse/ClickHouse/releases/download/v24.6.2.17-stable/clickhouse-client_24.6.2.17_amd64.deb

### Устанавливаем Clickhouse:
sudo apt upgrade

sudo apt upgrade -y

sudo apt install -y apt-transport-https ca-certificates dirmngr

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4

echo "deb https://repo.clickhouse.com/deb/stable/ main/" | sudo tee /etc/apt/sources.list.d/clickhouse.list

sudo dpkg -i clickhouse-common-static_24.6.2.17_amd64.deb

sudo dpkg -i clickhouse-server_24.6.2.17_amd64.deb 

sudo dpkg -i clickhouse-client_24.6.2.17_amd64.deb


### Запускаем Clickhouse:
sudo systemctl start clickhouse-server

sudo systemctl enable clickhouse-server

sudo systemctl status clickhouse-server

clickhouse-client

### Проверка SQL-запроса из Clickhouse-Client:
select version();

### Переход в папку /home и установка pip+nano:
cd /home

sudo apt update

sudo apt install python3-pip

sudo apt install nano

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

sudo python3 get-pip.py

### Правки файла конфигураций Clickhouse:
sudo nano /etc/clickhouse-server/config.xml

ctrl+W для поиска

<listen_host>0.0.0.0</listen_host>  (убираем <--  и --> )

sudo systemctl restart clickhouse-server (перезапуск после правки)

### Установка и запуск cron:
sudo apt update 

sudo apt install cron

crontab -e

30 7 * * * /usr/bin/python3 /home/wb_reklama.py (размещается внутри cron)

30 7 * * * /usr/bin/python3 /home/ozon_reklama.py (размещается внутри cron)

### Установка библиотек и запуск скриптов (делаем из папки /home):
ls (посмотреть файлы в текущей папке)

python3 -m pip install -r requirements.txt (установка библиотек)

python3 wb_reklama.py

python3 ozon_reklama.py

nano ozon_client_settings.json (правки настроек ozon)

nano wb_client_settings.json (правки настроек wb)

### Несколько вспомогательных команд:
ПРОВЕРКА РАБОТЫ СКРИПТОВ PYTHON: ps aux | grep python

ЗАПУСК БЕЗ ПРИВЯЗКИ К ТЕРМИНАЛУ ТЕКУЩЕМУ: nohup python3 ozon_reklama.py &

ОСТАНОВКА СКРИПТА: pkill -f wb_reklama.py
