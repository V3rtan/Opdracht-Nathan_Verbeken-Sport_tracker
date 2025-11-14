# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:42:05 2025

@author: Nathan Verbeken
"""

import db_communicatie
import sys

def maakKeuze():
    print("typ het nummer van de actie dat je wilt doen")
    keuze = input("1: print Workouts\n"
                  "2: print Oefeningen\n"
                  "3: voeg nieuwe oefening toe\n"
                  "4: voeg nieuwe workout toe\n"
                  
                  
                  
                  "0: programma afsluiten"
                  )
    return keuze







if __name__ == "__main__":
    keuze = maakKeuze()
    try:
        db = db_communicatie.Db_comm()
    except:
        print("comunicatie is gefaald, controleer instellingen.py")
        sys.exit()
        
        
    match keuze:
        case "1":
            print("workouts worden geprint")
        case "2":
            print("oefeningen worden geprint")
            print(db.getTabelOefeningen())
            
            
            
            
            
        case "0":
            print("programma wordt afgesloten")
            sys.exit()
        case _:
            print("geen geldige optie, probeer opnieuw")
    





