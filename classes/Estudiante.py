from classes.DbMongo import DbMongo
class Estudiante:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__collection = "estudiante"

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        query = {'_id':self._id}
        values = {'$set':self.__dict__}
        collection.update_one(query, values)
        client.close()


