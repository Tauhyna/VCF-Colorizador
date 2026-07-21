import pandas as pd


def ler_vcf(caminho_arquivo):
    """
    Lê um arquivo VCF ignorando as linhas iniciadas por ##
    """

    linhas = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            if linha.startswith("##"):
                continue

            linhas.append(linha.strip().split("\t"))

    cabecalho = linhas[0]
    dados = linhas[1:]

    df = pd.DataFrame(dados, columns=cabecalho)

    return df
