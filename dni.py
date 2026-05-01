LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

def calcular_letra(numero):
    return LETRAS[numero % 23]

def validar_dni(dni):
    dni = dni.strip().upper()
    
    if len(dni) != 9:
        return False, "El DNI debe tener 9 caracteres (8 números + 1 letra)"
    
    parte_numerica = dni[:-1]
    letra_introducida = dni[-1]
    
    if not parte_numerica.isdigit():
        return False, "Los primeros 8 caracteres deben ser números"
    
    letra_correcta = calcular_letra(int(parte_numerica))
    
    if letra_introducida == letra_correcta:
        return True, f"DNI válido. La letra {letra_correcta} es correcta."
    else:
        return False, f"DNI no válido. La letra debería ser {letra_correcta}, no {letra_introducida}."

def main():
    print("=== Validador de DNI español ===")
    while True:
        dni = input("\nIntroduce un DNI (o 'salir' para terminar): ")
        if dni.lower() == "salir":
            print("Hasta luego.")
            break
        valido, mensaje = validar_dni(dni)
        estado = "VÁLIDO" if valido else "NO VÁLIDO"
        print(f"{estado} — {mensaje}")

if __name__ == "__main__":
    main()