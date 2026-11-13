unidades = ["Hospital Provincial do Uíge", "Centro de Saúde de Sanza Pombo"]
pacientes = {}


def registar_unidade():
    nome = input("Nome da unidade de saúde: ")
    if nome in unidades:
        print("Essa unidade já existe.")
    else:
        unidades.append(nome)
        print("Unidade registada.")


def listar_unidades():
    print("\n--- Unidades de saúde ---")
    for i in range(len(unidades)):
        print(i + 1, "-", unidades[i])


def escolher_unidade():
    listar_unidades()
    numero = int(input("Escolha o número da unidade: "))
    if numero < 1 or numero > len(unidades):
        print("Unidade inválida.")
        return None
    return unidades[numero - 1]


def registar_paciente():
    print("\n--- Registar paciente ---")
    bi = input("Número do BI: ")
    if bi in pacientes:
        print("Este paciente já está registado.")
        return
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    pacientes[bi] = {"nome": nome, "idade": idade, "historico": []}
    print("Paciente registado.")


def registar_consulta():
    print("\n--- Registar consulta ---")
    bi = input("Número do BI do paciente: ")
    if bi not in pacientes:
        print("Paciente não encontrado.")
        return
    unidade = escolher_unidade()
    if unidade is None:
        return
    data = input("Data (dd/mm/aaaa): ")
    diagnostico = input("Diagnóstico: ")
    tratamento = input("Tratamento: ")

    consulta = [data, unidade, diagnostico, tratamento]
    pacientes[bi]["historico"].append(consulta)
    print("Consulta registada no histórico clínico.")


def consultar_historico():

    print("\n--- Histórico clínico ---")
    bi = input("Número do BI do paciente: ")
    if bi not in pacientes:
        print("Paciente não encontrado.")
        return
    p = pacientes[bi]
    print("Paciente:", p["nome"], "| Idade:", p["idade"])
    if len(p["historico"]) == 0:
        print("Sem consultas registadas.")
    for c in p["historico"]:
        print("-", c[0], "|", c[1])
        print("   Diagnóstico:", c[2])
        print("   Tratamento:", c[3])


def relatorio_coordenacao():

    print("\n--- Consultas por unidade ---")
    for u in unidades:
        total = 0
        for p in pacientes.values():
            for c in p["historico"]:
                if c[1] == u:
                    total = total + 1
        print(u, ":", total, "consultas")
    print("Total de pacientes:", len(pacientes))


opcao = ""
while opcao != "0":
    print("\n===== SISTEMA INTEGRADO DE SAÚDE - UÍGE =====")
    print("1 - Registar unidade de saúde")
    print("2 - Listar unidades de saúde")
    print("3 - Registar paciente")
    print("4 - Registar consulta")
    print("5 - Consultar histórico clínico")
    print("6 - Relatório (coordenação dos serviços)")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        registar_unidade()
    elif opcao == "2":
        listar_unidades()
    elif opcao == "3":
        registar_paciente()
    elif opcao == "4":
        registar_consulta()
    elif opcao == "5":
        consultar_historico()
    elif opcao == "6":
        relatorio_coordenacao()
    elif opcao == "0":
        print("Até logo!")
    else:
        print("Opção inválida.")

