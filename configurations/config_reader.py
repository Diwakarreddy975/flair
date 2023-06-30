from configparser import ConfigParser

def readConfigurations(key,value):
    config=ConfigParser()
    config.read("C:\\Users\\91789\\PycharmProjects\\flair\\testData\\config.ini")
    return config.get(key,value)


