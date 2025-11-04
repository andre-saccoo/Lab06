from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
import mysql.connector

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        # creo la connessione al database e creo un cursore per leggere i dati, svolgo la query
        cnx = get_connection()
        cursor = cnx.cursor()
        query="""SELECT * FROM automobile"""
        cursor.execute(query)
        rows = cursor.fetchall() #con fatchall tiro giù tutti i dati dal database
        automobili = [] # creo la lista per disporre le automobili
        for row in rows:
            automobili.append(Automobile(*row)) #per ogni riga del database creo l'oggetto automobile e lo metto nella lista
        cursor.close() #chiudo il cursore e la connessione per non sprecare risorse e restituisco la lista
        cnx.close()
        return automobili

    def cerca(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        #creo la connessione al database e creo un cursore per leggere i dati, svolgo la query
        cnx = get_connection()
        cursor = cnx.cursor()
        query="""SELECT * FROM automobile 
                WHERE modello=%s"""
        cursor.execute(query, (modello,))
        rows = cursor.fetchall() #con fatchall tiro giù tutti i dati dal database
        automobili_ordinate = [] # creo la lista per disporre le automobili
        for row in rows:
            automobili_ordinate.append(Automobile(*row)) #per ogni riga del database creo l'oggetto automobile e lo metto nella lista
        cursor.close() #chiudo il cursore e la connessione per non sprecare risorse e restituisco la lista
        cnx.close()
        return automobili_ordinate