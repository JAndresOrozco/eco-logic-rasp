import pymongo


class Mongo:
    def __init__(self):
        
        MONGODB_HOST = '127.0.0.1'
        MONGODB_PORT = '27027'
        MONGODB_TIMEOUT = 1000

        URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"

        try:
            self._client = pymongo.MongoClient(URI_CONNECTION)
            print ('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))
            self._db = self._client['sensorTyH']
            self._cDatos = self._db['Datos']
            
        except pymongo.errors.ServerSelectionTimeoutError as error:
            print ('Error with MongoDB connection: %s' % error)
        except pymongo.errors.ConnectionFailure as error:
            print ('Could not connect to MongoDB: %s' % error)
        
    def insertarDatos(self,t,h,f):
        c = self._cDatos.find()
        d = self._cDatos.insert({"_id":c.count()+1,"temperatura":t,"humedad":h,"fecha":f})
        #print(str(d))
        

        