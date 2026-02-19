# Programma: Calcolo dell'età

from typing import Dict, Any, Optional, Tuple
import string
class student:


    def __init__(self, nome, data_nascita, voto):
        self.studente = {
            "nome": nome,
            "data_nascita": data_nascita,
            "voto": voto
        }

    def __str__(self):
        return f"Studente: {self.studente['nome']}, Data di nascita: {self.studente['data_nascita']}, Voto: {self.studente['voto']}"
    
    def set_voto(self, nuovo_voto): #interrogazione ripatore
        self.studente["voto"] = nuovo_voto
    
    #def media_voti(self): -> str




def main():
    print("Benvenuto al sistema di gestione voti!")
    count_stud = int(input("Professore inserisca il numero di studenti da inserire: "))
    students_list = []
    for i in range(count_stud):
        nome = input(f"Come si chiama lo studente {i+1}? ")
        data_nascita = input("data di nascita? (formato gg/mm/aaaa) ")
        voto = int(input("voto? (formato 0-10) "))
        students_list.append(student(nome, data_nascita, voto))

    students = student(nome, data_nascita, voto)
    print(students)

    

if __name__ == "__main__":
    main()
