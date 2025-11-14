# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:19:44 2025

@author: Nathan Verbeken
"""
import sqlite3
import instellingen

class Db_comm:
    def __init__ (self):
        self.dbconnectie = sqlite3.connect(instellingen.path_DB)
        self.mijncursor = self.dbconnectie.cursor()

    #haalt bestanden uit de tabellen
    def getQuery(self,query):
        try:
            self.mijncursor.execute(query)
            tabel = self.mijncursor.fetchall()
            return tabel
        except sqlite3.Error as e:
            print("query gefaald: " + e)
            return None
        except:
            print("querry is gefaald")
            return None
        
    #Returned de tabel Oefeningen
    def getTabelOefeningen(self):          
        return self.getQuery("SELECT oefening_id,naam,beschrijving FROM Oefeningen")

    #Returned de tabel Workouts
    def getTabelWorkouts(self):  
        return self.getQuery("SELECT workout_id,oefeningen_id,datum,reps,tijd,notities FROM Workouts")
    
    #genereert een nieuw id
    def getNewIdOefeningen(self):
        return int((self.getQuery("SELECT max(oefening_id) FROM Oefeningen")[0][0])) +1
        
    #pushed nieuwe oefening naar de database
    def voegOefeningToe(self,oefening_naam,oefening_id):
        print("voeg oefeningen toe")