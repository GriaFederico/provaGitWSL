# Programma: Calcolo dell'età

from typing import Dict, Any, Optional, Tuple
import string
class student:


    def __init__(self, nome, data_nascita, voti):
        self.studente = {
            "nome": nome,
            "data_nascita": data_nascita,
            "voti": voti
        }

    def __str__(self):
        return f"Studente: {self.studente['nome']}, Data di nascita: {self.studente['data_nascita']}, Voti: {self.studente['voti']}"
    
    def set_voto(self, nuovo_voto): #interrogazione ripatore
        self.studente["voti"].append(nuovo_voto)
    
    def media_voti(self) -> float:
        if not self.studente["voti"]:
            return 0.0
        return sum(self.studente["voti"]) / len(self.studente["voti"])
    
    #def max_voto(self) -> Optional[int]:

def main():
    print("Benvenuto al sistema di gestione voti!")
    count_stud = int(input("Professore inserisca il numero di studenti da inserire: "))
    students_list = []
    for i in range(count_stud):
        nome = input(f"Come si chiama lo studente {i+1}? ")
        data_nascita = input("data di nascita? (formato gg/mm/aaaa) ")
        voti = []
        count_voti = int(input("Quanti voti vuoi inserire per questo studente? "))    
        for j in range(count_voti):  
            voto = int(input("voto? (formato 0-10) "))
            voti.append(voto)
        students_list.append(student(nome, data_nascita, voti))

    students = student(nome, data_nascita, voto)
    print(students)

    

if __name__ == "__main__":
    main()
