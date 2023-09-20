# tabela_hash_resultados = {}
import timeit


def calcular_qtd_termos_sequencia_collatz(numero):
    qtd_termos = 1
    # numero_inicial = numero

    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = 3 * numero + 1
        # quantidade_ja_calculada = tabela_hash_resultados.get(numero)

        # if quantidade_ja_calculada:
        #     qtd_termos += quantidade_ja_calculada
        #     break

        qtd_termos += 1

    # tabela_hash_resultados[numero_inicial] = qtd_termos

    return qtd_termos


def encontrar_maior_sequencia_collatz(numero_final):
    numero_maior_sequencia = 0
    maior_sequencia = 0

    for numero in range(1, numero_final+1):
        qtd_termos = calcular_qtd_termos_sequencia_collatz(numero)

        if qtd_termos >= maior_sequencia:
            numero_maior_sequencia = numero
            maior_sequencia = qtd_termos

    return numero_maior_sequencia, maior_sequencia


inicio = timeit.default_timer()
numero_com_maior_sequencia, total_de_termos = encontrar_maior_sequencia_collatz(
    1000000)
fim = timeit.default_timer()

print(fim-inicio)

print(
    f"O número {numero_com_maior_sequencia} produz a sequencia com mais items: {total_de_termos}")
