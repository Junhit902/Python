letras = ["A", "B", ["C", "D"]]

print(letras[2][0])


cidades: dict[str, list[str]] = {
"Japao": {"provincias": ["Tokyo", "Osaka", "Gunma", "Miyagi"], 
            "numero_vezes_visitado": 4
        },
"Brasi": ["Sao Paulo", "Rio de Janeiro", "Bahia", "Paraná"]
}


print(cidades["Japao"]["provincias"][2])