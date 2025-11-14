# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:19:44 2025

@author: Nathan Verbeken
"""
import sqlite3
import instellingen

class Db_comm:
    def __init__ (self):
        pass  

    #haalt bestanden uit de tabellen
    def getQuery(self,query):
        try:
            self.connect()
            self.mijncursor.execute(query)
            tabel = self.mijncursor.fetchall()
            return tabel
        except sqlite3.Error as e:
            print("query gefaald: ", e)
            return None
        except:
            print("querry is gefaald")
            return None
        finally:
            self.close()
        
    def putQuery(self,query,values):
        try:
            self.connect()
            self.mijncursor.execute(query,values)
            self.dbconnectie.commit()
        except sqlite3.Error as e:
            print("pushen mislukt: ", e)
        finally:
            self.close()
            
        
    #Returned de tabel Oefeningen
    def getTabelOefeningen(self):          
        return self.getQuery("SELECT oefening_id,naam,beschrijving FROM Oefeningen")

    #Returned de tabel Workouts
    def getTabelWorkouts(self):  
        return self.getQuery("SELECT workout_id,oefeningen_id,datum,reps,tijd,notities FROM Workouts")
    
    #genereert een nieuw id voor oefening
    def getNewIdOefeningen(self):
        temp_id = self.getQuery("SELECT max(oefening_id) FROM Oefeningen")[0][0]
        if temp_id != None:
            return int(temp_id) +1
        else:
            return int(1)
    
    #genereert een nieuw id voor workout
    def getNewIdWorkouts(self):
        temp_id = (self.getQuery("SELECT max(workout_id) FROM Workouts")[0][0])
        if temp_id != None:
            return int(temp_id) +1
        else:
            return int(1)
        
    #pushed nieuwe oefening naar de database
    def voegOefeningToe(self,oefening_id, oef_naam, beschrijving):
        self.putQuery(("INSERT INTO Oefeningen (oefening_id,naam,beschrijving) VALUES (?,?,?)"),(oefening_id,oef_naam,beschrijving))
        
    #pushed nieuwe oefening naar de database
    def voegWorkoutToe(self, workout_id, oef_id , datum, reps, tijd, notities):
        self.putQuery(("INSERT INTO Workouts (workout_id,oefeningen_id,datum,\
                       reps,tijd,notities)VALUES (?,?,?,?,?,?)"),(workout_id, oef_id, datum,reps,tijd,notities))
        
    def connect(self):
        self.dbconnectie = sqlite3.connect(instellingen.path_DB)
        self.mijncursor = self.dbconnectie.cursor()
        
    def removeWorkout(self, workout_id):
        self.putQuery(("DELETE FROM Workouts WHERE workout_id = ?"),(workout_id,))
        
    def removeOef(self, oef_id):
        self.putQuery(("DELETE FROM Oefeningen WHERE oefening_id = ?"),(oef_id,))
        
    #sluit connectie
    def close(self):
        self.dbconnectie.close()        