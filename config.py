#!/usr/bin/python
from configparser import ConfigParser

def db_config(filename='./databse.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db ={} 
    if parser.has_section("postgresql"):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")

    return db
