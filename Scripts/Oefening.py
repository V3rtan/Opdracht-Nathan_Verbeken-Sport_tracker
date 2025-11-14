# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:06:36 2025

@author: Nathan Verbeken
"""
# import db_communicatie



class Oefeningen:
    def __init__(self,db,naam = None):
        if naam == None:
            naam = input("geef de naam van de nieuwe oefening").strip().title()
        beschrijving = input("geef een beschrijving van de oefening")
        self.naam = naam
        self.beschrijving = beschrijving
        self.id_oef = db.getNewIdOefeningen()
        

    def add(self,db): 
        db.voegOefeningToe(self.id_oef,self.naam,self.beschrijving)
        
        
        
        