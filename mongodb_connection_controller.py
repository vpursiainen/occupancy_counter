import mongoengine as me

def connect_to_mongodb():
    db_username = 'martino'
    db_password = 'armbims'
    db_presets = 'mongodb+srv://'
    db_host = '@cluster0-hlb5v.mongodb.net/'
    db_name = 'test'#armbims'
    db_config = '?retryWrites=true&w=majority'
    db_conn_string = db_presets + db_username + ':' + db_password + db_host + db_name + db_config
    try:
        me.connect(host=db_conn_string)
        db_client = me.get_connection()
        return db_client
    except me.MongoEngineConnectionError:
        print("The connection to mondoBD raised an exception")

def disconnect_from_mongodb(client):
    client.close()
