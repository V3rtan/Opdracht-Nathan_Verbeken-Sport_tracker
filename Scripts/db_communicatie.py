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


    #Returned de tabel Oefeningen
    def getTabelOefeningen(self):        
        try:
            query = "SELECT oefening_id,naam,beschrijving FROM Oefeningen"
            self.mijncursor.execute(query)
            tabel = self.mijncursor.fetchall()
            return tabel
        except:
            print("querry is gefaald")
            return None
            
    
    
    def voegOefeningToe(self,oefening_naam,oefening_id):
        print("voeg oefeningen toe")