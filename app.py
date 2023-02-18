from classes import Estudiante
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("Jairo 1", "Raudales", "93458111")
    estudiante.save()
    estudiante.apellido = "Raudales Baca"
    estudiante.update()

if __name__  == "__main__":
    load_dotenv()
    main()
