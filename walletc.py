import datetime
import sqlite3

import sys
# date :
date = str(datetime.datetime.today().date())
monthindex = datetime.date.today().month
year = datetime.date.today().year

months = {
    1: "Janvier",
    2: "Fevrier",
    3: "Mars",
    4: "Avril",
    5: "Mai",
    6: "Juin",
    7: "Juillet",
    8: "Aout",
    9: "Septembre",
    10: "Octobre",
    11: "Novembre",
    12: "Decembre",
}
monname = months.get(monthindex)

# database:
db = sqlite3.connect(f"{monname}{year}.db")
db.execute(f"create table if not exists '{monname}{year}' "
           f"(date text, income integer, outcome integer, difference integer, monthly_income integer, monthly_outcome integer, monthly_difference integer, remarque text)")
# setting up cursor:
c = db.cursor()
c.execute(f"create table if not exists '{monname}{year}' "
          f"(date text, income integer, outcome integer, difference integer, monthly_income integer, monthly_outcome integer, monthly_difference integer, remarque text)")


def save_and_close():
    db.commit()
    db.close()
    print("saved and closed")


def mainf():
    #asking the user for the inputs:
    outcom = int(input("Combien tu as dépensé: ").strip())
    incom = int(input("Combien tu as obtenue: ").strip())
    difference = incom - outcom
    print(f" la difference est : {difference}")
    remarque= input("entrer votre remarque: \n")
    # counting different monthly results: 
    # monthly income:
    c.execute(f"SELECT income from '{monname}{year}'")
    sinc = c.fetchall()
    l1 = [i[0] for i in sinc]
    monin = sum(l1)+incom
    # monthly outcome:
    c.execute(f"SELECT outcome from '{monname}{year}'")
    sout = c.fetchall()
    l2 = [j[0] for j in sout]
    monout = sum(l2)+outcom

    # monthly difference:
    c.execute(f"select difference from '{monname}{year}'")
    sdif = c.fetchall()
    l3 = [z[0] for z in sdif]

    mondif = sum(l3)+difference

    # inserting monthly data:
    c.execute(
        f"insert into '{monname}{year}'(date,income,outcome,difference,monthly_income,monthly_outcome,monthly_difference, remarque) values('{date}','{incom}','{outcom}','{difference}','{monin}','{monout}','{mondif}','{remarque}')")


mainf()
save_and_close()
