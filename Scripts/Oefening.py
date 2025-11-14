# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:06:36 2025

@author: Nathan Verbeken
"""
# import db_communicatie



class Oefeningen:
    def __init__(self,naam,beschrijving,db):
        self.naam = naam
        self.beschrijving = beschrijving
        self.id_oef = db.getNewIdOefeningen()
        

    def add(self): 
        print()
        
        
        
        