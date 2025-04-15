from typing import List

class AnalizadorTemperaturas:

    def __init__(self, dias: int = 7):
        self.dias = dias
        self.temperaturas: List[float] = []

    def solicitar_temperaturas(self):
        print("Ingreso de temperaturas diarias\n")

        for dia in range(1, self.dias + 1):
            while True:
                try:
                    entrada = input(f"Ingrese la temperatura del día {dia}: ")
                    temp = float(entrada)
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")

    def analizar_temperaturas(self):
        if not self.temperaturas:
            print("No hay datos para analizar.")
            return

        total = sum(self.temperaturas)
        promedio = total / self.dias
        temp_max = max(self.temperaturas)
        temp_min = min(self.temperaturas)

        print(f"\nAnálisis de temperaturas:")
        print(f"Promedio semanal: {promedio:.2f}°C")
        print(f"Temperatura máxima: {temp_max:.2f}°C")
        print(f"Temperatura mínima: {temp_min:.2f}°C")

        if promedio > 30:
            print("Semana calurosa")
        elif promedio < 15:
            print("Semana fresca")
        else:
            print("Temperaturas moderadas esta semana")

def main():
    analizador = AnalizadorTemperaturas()
    analizador.solicitar_temperaturas()
    analizador.analizar_temperaturas()

if __name__ == "__main__":
    main()
