# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:42:05 2025

@author: Nathan Verbeken
"""

import db_communicatie
import sys
import Oefening as oef
import Workout
import csv

def maakKeuze():
    print("\n \n \n \n"
          "------------------------------------------------------\n"
          "typ het nummer van de actie dat je wilt doen")
    keuze = input("1: print Workouts\n"
                  "2: print Oefeningen\n"
                  "3: voeg nieuwe oefening toe\n"
                  "4: voeg nieuwe workout toe\n"
                  "5: verwijder een workout   \n"
                  "6: Verwijder een Oefening   \n"
                  "7: Maak een excel bestand van de workouts\n"
                  
                  
                  "0: programma afsluiten \n \n"
                  )
    return keuze


def printTableworkouts():
    print("workouts worden geprint")
    for i in db.getTabelWorkouts():
        print(i)
        
        
def printTableOef():
    print("oefeningen worden geprint")
    for i in db.getTabelOefeningen():
        print(i)



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
                printTableworkouts()
            case "2":
                printTableOef()
            case "3":
                print("nieuwe oefening wordt toegevoegd")
                oefening = oef.Oefeningen(db)
                oefening.add(db)
            case "4":
                print("nieuwe Workout wordt toegevoegd")
                workout = Workout.Workout(db)
                workout.add(db)
            case "5":
                printTableworkouts()
                workouts = [x[0] for x in db.getTabelWorkouts()]
                while True:
                    workout = input("geef het id van de workout dat je wilt verwijderen of typ quit")
                    if workout == "quit":
                        break
                    try:
                        temp = int(workout)
                        if temp in workouts:
                            db.removeWorkout(temp)
                            break
                    except:
                        print(workout + " is geen geldige workout id")     
            case "6":
                printTableOef()
                oefeningen = [x[0] for x in db.getTabelOefeningen()]
                while True:
                    temp_oef = input("geef het id van de oefening dat je wilt verwijderen of typ quit")
                    if temp_oef == "quit":
                        break
                    try:
                        temp = int(temp_oef)
                        if temp in oefeningen:
                            db.removeOef(temp)
                            break
                    except:
                        print(temp_oef + " is geen geldige oefening id") 
            case "7":
                print("excel bestand wordt gemaatkt")
                tabel = db.getJoinedTabel()
                print(tabel)
                
                
                
            case "0":
                print("programma wordt afgesloten")
                sys.exit()
            case _:
                print("geen geldige optie, probeer opnieuw")
        input("druk op enter om door te gaan")
        
        
        
        






