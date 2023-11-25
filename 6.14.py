pessoas = {
    662023:{
        "sexo":"M","idade":50,"peso":60,"altura": 1.70}
}

def metabolismo(pacientes):
    output = dict()
    for paciente in pacientes:
        if pacientes[paciente] ["sexo"] == "M":
            pacientes[paciente] = 66 + (6.3*pacientes[paciente])
            ["peso"] + (12.9*pacientes[paciente])
            ["altura"] - (6.8*pacientes[paciente])
            ["idade"]

        else:
            pacientes[paciente]["basal"] = 65.5 + (4.3*pacientes[paciente] ["peso"]) (4.7*pacientes[paciente]["altura"])-(4.7*pacientes[paciente]["idade"])
        

    return metabolismo(pacientes)

print(metabolismo(pacientes))