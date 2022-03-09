import pymongo 

connection_url = 'mongodb+srv://costumer:costumer2022@cluster0.sxqpd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
try:
    client = pymongo.MongoClient(connection_url)
    database = client.get_database('costumer')
    SampleTable = database.Sampletable
    print('conectado')
except:
    print('error')