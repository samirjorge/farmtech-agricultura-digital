import math
import csv
from datetime import datetime

culturas = []
areas = []
insumos = []
datas = []
metodos = []  # Armazena o tipo de aplicação: Trator ou Avião ou Drone


def calcular_area(cultura):
    try:
        if cultura == "café":
            print("\nCultura selecionada: Café")
            print("Produto aplicado: Fosfato")
            print("Dosagem: 500 mL por metro")
            print("Formato da área: Retangular\n")
            largura = float(input("Informe a largura da plantação (em metros): "))
            comprimento = float(input("Informe o comprimento da plantação (em metros): "))
            return largura * comprimento, largura, comprimento

        elif cultura == "milho":
            print("\nCultura selecionada: Milho")
            print("Produto aplicado: Calcário")
            print("Dosagem: 300 mL por metro")
            print("Formato da área: Quadrada\n")
            lado = float(input("Informe o lado da plantação (em metros): "))
            return lado * lado, lado, lado
    except ValueError:
        print("[ERRO] Valor inválido! Digite um número.")
        return calcular_area(cultura)


def calcular_insumos(cultura, area, largura, comprimento):
    if cultura == "café":
        produto = "Fosfato"
        dose_metro = 500
        espacamento_entre_ruas = 3
    elif cultura == "milho":
        produto = "Calcário"
        dose_metro = 300
        espacamento_entre_ruas = 1
    else:
        return "", 0, ""

    print("\nComo será feita a aplicação do produto?")
    print("1 - Trator (aplicação terrestre, baseada em ruas)")
    print("2 - Avião ou Drone (aplicação aérea, baseada na área total)")
    escolha = input("Escolha o método (1 ou 2): ")

    if escolha == "1":
        metodo = "Trator"
        try:
            sugestao_ruas = int(largura // espacamento_entre_ruas)
            print(f"Sugestão: com espaçamento de {espacamento_entre_ruas}m, seriam cerca de {sugestao_ruas} ruas.")
            numero_ruas = int(input("Quantas ruas a lavoura possui? "))

            comprimento_total = numero_ruas * comprimento
            total_litros = (dose_metro * comprimento_total) / 1000
            return produto, total_litros, metodo
        except ValueError:
            print("[ERRO] Valor inválido! Digite um número.")
            return calcular_insumos(cultura, area, largura, comprimento)

    elif escolha == "2":
        metodo = "Avião ou Drone"
        total_litros = (dose_metro * area) / 1000
        return produto, total_litros, metodo

    else:
        print("[ERRO] Opção inválida.")
        return calcular_insumos(cultura, area, largura, comprimento)


while True:
    opcao = ""
    while opcao not in ["1", "2", "3", "4", "5"]:
        print("\n=== Menu FarmTech ===")
        print("1. Inserir nova cultura")
        print("2. Mostrar dados")
        print("3. Atualizar cultura")
        print("4. Deletar cultura")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao not in ["1", "2", "3", "4", "5"]:
            print("[ERRO] Opção inválida. Tente novamente.")

    if opcao == "1":
        print("Escolha a cultura:")
        print("1 - Café")
        print("2 - Milho")
        escolha = input("Digite o número da cultura: ")

        if escolha == "1":
            cultura = "café"
        elif escolha == "2":
            cultura = "milho"
        else:
            print("[ERRO] Opção inválida.")
            continue

        area, largura, comprimento = calcular_area(cultura)
        produto, insumo, metodo = calcular_insumos(cultura, area, largura, comprimento)

        culturas.append(cultura)
        areas.append(area)
        insumos.append((produto, insumo))
        datas.append(datetime.now().strftime("%d/%m/%Y %H:%M"))
        metodos.append(metodo)

        print("\n[OK] Dados salvos com sucesso!")
        print("Cultura:", cultura)
        print(f"Área plantada: {area:.2f} m²")
        print("Produto aplicado:", produto)
        print(f"Quantidade total de insumo: {insumo:.2f} L")
        print("Aplicação:", metodo)

        # Salvar em CSV
        with open("dados_lavouras.csv", mode="a", newline="") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            if arquivo_csv.tell() == 0:
                escritor.writerow(["Data", "Cultura", "Área (m²)", "Produto", "Insumo (L)", "Aplicação"])
            escritor.writerow([datas[-1], cultura, f"{area:.2f}", produto, f"{insumo:.2f}", metodo])

    elif opcao == "2":
        if len(culturas) == 0:
            print("Nenhum dado cadastrado ainda.")
        else:
            print("\n--- Dados Cadastrados ---")
            for i in range(len(culturas)):
                produto, quantidade = insumos[i]
                print(f"{i + 1}. [{datas[i]}] Cultura: {culturas[i]}, Área: {areas[i]:.2f} m², Produto: {produto}, "
                      f"Total: {quantidade:.2f} L, Aplicação: {metodos[i]}")

    elif opcao == "3":
        if len(culturas) == 0:
            print("Nenhum dado para atualizar.")
            continue

        print("\n--- Culturas cadastradas ---")
        for i in range(len(culturas)):
            produto, quantidade = insumos[i]
            print(f"{i + 1}. [{datas[i]}] Cultura: {culturas[i]}, Área: {areas[i]:.2f} m², Produto: {produto}, "
                  f"Total: {quantidade:.2f} L, Aplicação: {metodos[i]}")

        try:
            indice = int(input("Informe o número da cultura que deseja atualizar: ")) - 1
            if 0 <= indice < len(culturas):
                print("Escolha a nova cultura:")
                print("1 - Café")
                print("2 - Milho")
                escolha = input("Digite o número da nova cultura: ")

                if escolha == "1":
                    nova_cultura = "café"
                elif escolha == "2":
                    nova_cultura = "milho"
                else:
                    print("[ERRO] Opção inválida.")
                    continue

                nova_area, nova_largura, novo_comprimento = calcular_area(nova_cultura)
                novo_produto, novo_insumo, novo_metodo = calcular_insumos(nova_cultura, nova_area, nova_largura, novo_comprimento)

                culturas[indice] = nova_cultura
                areas[indice] = nova_area
                insumos[indice] = (novo_produto, novo_insumo)
                metodos[indice] = novo_metodo
                datas[indice] = datetime.now().strftime("%d/%m/%Y %H:%M")

                print("\n[OK] Dados atualizados com sucesso!")
                print(f"Cultura: {nova_cultura}")
                print(f"Área plantada: {nova_area:.2f} m²")
                print(f"Produto aplicado: {novo_produto}")
                print(f"Quantidade total de insumo: {novo_insumo:.2f} L")
                print(f"Aplicação: {novo_metodo}")
            else:
                print("[ERRO] Índice inválido.")
        except ValueError:
            print("[ERRO] Valor inválido! Digite um número.")

    elif opcao == "4":
        if len(culturas) == 0:
            print("Nenhum dado para deletar.")
            continue

        print("\n--- Culturas cadastradas ---")
        for i in range(len(culturas)):
            produto, quantidade = insumos[i]
            print(f"{i + 1}. [{datas[i]}] Cultura: {culturas[i]}, Área: {areas[i]:.2f} m², Produto: {produto}, "
                  f"Total: {quantidade:.2f} L, Aplicação: {metodos[i]}")

        try:
            indice = int(input("Informe o número da cultura que deseja deletar: ")) - 1
            if 0 <= indice < len(culturas):
                culturas.pop(indice)
                areas.pop(indice)
                insumos.pop(indice)
                datas.pop(indice)
                metodos.pop(indice)
                print("[OK] Cultura removida com sucesso!")
            else:
                print("[ERRO] Índice inválido.")
        except ValueError:
            print("[ERRO] Valor inválido! Digite um número.")

    elif opcao == "5":
        print("\n--- Resumo Final ---")
        total_geral = sum([i[1] for i in insumos])
        print(f"Total de culturas cadastradas: {len(culturas)}")
        print(f"Total de insumos aplicados: {total_geral:.2f} L")
        print("Encerrando o programa... Até logo!")
        break
