# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:07:10 2025

@author: Nathan Verbeken 
"""
import Oefening as oef
from datetime import datetime

class Workout:
    def __init__(self,db):
        self.id_oef = None
        tabelOefeningen = db.getTabelOefeningen()
        tabelOefNamen = [x[0:2] for x in tabelOefeningen]
        print(tabelOefNamen)
        i_naam = input("gebruik een bestaande oefening door een van bovenstaande"
                       " namen of id's te gebruiken.").strip().title()
        tr = True
        while tr == True:
            for tple in tabelOefeningen:
                if i_naam == str(tple[0]) or i_naam == tple[1]:
                    self.id_oef = tple[0]
                    tr = False
            if self.id_oef == None:
                i_naam = input("geen geldige waarde, probeer opnieuw")
            
        self.id_workout = db.getNewIdWorkouts()
        print("geef de datum in van deze oefening (formaat: (dd-mm-jjjj)")
        self.datum = self.datumInvoegen()
        self.reps = input("Geef aan hoeveel keer je deze oefening hebt gedaan: ")
        self.tijd = input("Geef hoe lang de oefening heeft geduurt: ")
        self.notities = input("Indien gewenst kan je hier nog enkele notities aan toevoegen: ")
        
        
    #voegt een nieuwe workout toe aan de database
    def add(self,db): 
        db.voegWorkoutToe(self.id_workout,self.id_oef,self.datum.date(),self.reps,self.tijd,self.notities)
        
        
    #controleerd of de datum wel van het juiste formaat is
    def datumInvoegen(self):
        while True:
            datum = input()
            try:
                return datetime.strptime(datum,"%d-%m-%Y" )
            except ValueError:
                print(datum + " is een ongeldige datum, probeer het opnieuw (dd-mm-jjjj): ")