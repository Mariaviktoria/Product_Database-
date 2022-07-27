from create_tables import create_tables
import psycopg2
from config import config


def insert_values():
    params = config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    #Copy all the CSV files from \Postgresql\Database_Tables to your C:/

    sql = '''COPY brand(brandname,brandlocation,brandfocus)\
    FROM 'C:/brand.csv' DELIMITER ',' CSV HEADER;'''
    cur.execute(sql)

    sql = '''COPY eyeliner(eyelinername,eyelinerType,cost, brandId)\
    FROM 'C:/eyeliner.csv' DELIMITER ',' CSV HEADER;'''
    cur.execute(sql)

    sql = '''COPY foundation(FoundationName,FoundationRGB,Cost,SkinType,FoundationType, brandId)\
    FROM 'C:/foundation.csv' DELIMITER ',' CSV HEADER;'''
    cur.execute(sql)

    sql = '''COPY lipstick(LipstickName,LipstickColor,Cost, brandId)\
    FROM 'C:/Lipstick.csv' DELIMITER ',' CSV HEADER;'''
    cur.execute(sql)

    sql = '''COPY Moisturizer(MoisturizerName,SkinType,Cost, brandId)\
    FROM 'C:/Moisturizer.csv' DELIMITER ',' CSV HEADER;'''
    cur.execute(sql)

    sql = '''COPY users(userName,userAge,userLocation,userColorRGB)\
    FROM 'C:/users.csv' DELIMITER ',' CSV HEADER;'''
    cur.execute(sql)

    conn.commit()
    conn.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_tables()
    insert_values()