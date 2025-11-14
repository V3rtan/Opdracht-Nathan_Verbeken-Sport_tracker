# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:42:05 2025

@author: Nathan Verbeken
"""

import db_communicatie
import sys
import Oefening as oef

def maakKeuze():
    print("\n \n \n \n"
          "------------------------------------------------------\n"
          "typ het nummer van de actie dat je wilt doen")
    keuze = input("1: print Workouts\n"
                  "2: print Oefeningen\n"
                  "3: voeg nieuwe oefening toe\n"
                  "4: voeg nieuwe workout toe\n"
                  
                  
                  
                  "0: programma afsluiten \n \n"
                  )
    return keuze







if __name__ == "__main__":    
    while(True):
        keuze = maakKeuze()
        try:
            db = db_communicatie.Db_comm()
        except:
            print("comunicatie is gefaald, controleer instellingen.py")
            sys.exit()
            
            
        match keuze:
            case "1":
                print("workouts worden geprint")
                print(db.getTabelWorkouts())
            case "2":
                print("oefeningen worden geprint")
                print(db.getTabelOefeningen())
            case "3":
                print("nieuwe oefening wordt toegevoegd")
                naam = input("geef de naam van de nieuwe oefening")
                beschrijving = input("geef een beschrijving van de oefening")
                oefening = oef.Oefeningen(naam, beschrijving, db)
                
                
                
                
                
                
                
            case "0":
                print("programma wordt afgesloten")
                sys.exit()
            case _:
                print("geen geldige optie, probeer opnieuw")
        input("druk op enter om door te gaan")
    





