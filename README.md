# ATT: Tarifas de Internet Fijo

Este proyecto utiliza Scrapy y MongoDB Atlas para realizar el proceso de ETL para el proyecto de Business Intelliegence sobre las tarifas de internet fijo en Bolivia.

## Requisitos

- Python 3.x
- Scrapy
- pymongo
- MongoDB Atlas

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/dotM87/.git
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el spider de Scrapy para realizar el web scraping:

    ```bash
    scrapy crawl -s MONGODB_URI="mongodb+srv://<usuario>:<contraseña>@cluster0.ztxjdbr.mongodb.net/" -s MONGODB_DATABASE="att" att_spider
    ```

2. Los datos extraídos se almacenarán en la base de datos de MongoDB.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.