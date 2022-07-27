#!/usr/bin/python
import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            userID SERIAL PRIMARY KEY,
            userName varchar(255) NOT NULL,
            userAge integer,
            userLocation varchar(255),
            userColorRGB decimal(15,2)
        )
        """,
        """ 
        CREATE TABLE Brand (
            BrandID SERIAL PRIMARY KEY,
            BrandName varchar(255) NOT NULL,
            BrandLocation varchar(255),
            BrandFocus varchar(100)
        )
        """,
        """
        CREATE TABLE Foundation (
            FoundationID SERIAL PRIMARY KEY,
            FoundationName varchar(255) NOT NULL,
            FoundationRGB decimal(15,2),
            Cost decimal(15,2),
            SkinType varchar(255),
            FoundationType varchar(255),
            BrandID integer REFERENCES Brand(BrandID)
        )
        """,
        """
        CREATE TABLE Lipstick (
            LipstickID SERIAL PRIMARY KEY,
            LipstickName varchar(255) NOT NULL,
            LipstickColor varchar(255) NOT NULL,
            Cost decimal(15,2),
            BrandID integer REFERENCES Brand(BrandID)
        )
        """,
        """
        CREATE TABLE EyeLiner (
            EyelinerID SERIAL PRIMARY KEY,
            EyelinerName varchar(255),
            EyelinerType varchar(255),
            Cost decimal(15,2),
            BrandID integer REFERENCES Eyeliner(EyelinerID)
        )
        """,
        """
        CREATE TABLE Moisturizer (
            MoisturizerID SERIAL PRIMARY KEY,
            MoisturizerName varchar(255),
            Skintype varchar(255),
            Cost decimal(15,2),
            BrandID integer REFERENCES Eyeliner(EyelinerID)
        )
        """,
        """ 
        CREATE TABLE UserMaster ( 
        TranID SERIAL PRIMARY KEY, 
        UserID integer REFERENCES users(UserID), 
        BrandID integer REFERENCES Brand(BrandID)
        )
        """
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
