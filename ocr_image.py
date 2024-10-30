import easyocr
import re
import pandas as pd

# Inicializar o OCR Reader
def ocr_reader(image_path):
    reader = easyocr.Reader(['pt', 'en'])
    result = reader.readtext(image_path, detail=0)
    return result

# Função para filtrar os dados da tabela
def filtrar_dados(text):
    padrao_linhas = ["Colo", "G.T", "Inter trocanter", "Total Hip", "Ward"]
    colunas_tabela = ['ROI', 'BMD(g/cm²)', 'BMC(g)', 'Área(cm²)', 'T-score', 'Z-score']
    dados_tabela = []
    
    # Percorrer o texto e coletar dados das linhas
    for i, linha in enumerate(text):
        for padrao in padrao_linhas:
            if re.search(padrao, linha):
                dados_tabela.append(text[i:i+6])
                break
    
    # Organizar os dados na forma horizontal (transpor a tabela)
    dados_df = pd.DataFrame(dados_tabela, columns=colunas_tabela)
    return dados_df

# Função para salvar os dados em um arquivo .txt
def salvar_em_txt(dados_df, file_path):
    with open(file_path, 'w') as file:
        file.write(dados_df.to_string(index=False))

# Função principal
def main():
    image_path = r'C:\Users\jacks\Music\OCR\image.png'
    texto_extraido = ocr_reader(image_path)
    dados_filtrados = filtrar_dados(texto_extraido)
    
    # Exibir a tabela extraída
    print(dados_filtrados)
    
    # Salvar os dados em um arquivo txt
    salvar_em_txt(dados_filtrados, r'C:\Users\jacks\Music\OCR\resultado.txt')

if __name__ == "__main__":
    main()





#Faça um código em python para extrair os dados dessa tabela, irá fazer a leitura dessa imagem por meio de OCR, incluindo os títulos das linhas e colunas, esse código precisa ler essa imagem e converter em texto. A última coisa que essa tabela precisa ser organizada na horizontal, como mostrado na imagem. O Pyteressact não pode ser utilizado
#Faça um código em python para extrair os dados dessa tabela, irá fazer a leitura dessa imagem por meio de OCR, incluindo os títulos das linhas e colunas, esse código precisa ler essa imagem e converter em texto. A última coisa que essa tabela precisa ser organizada na horizontal, como mostrado na imagem. O Pyteressact não pode ser utilizado As linhas são: Colo, G.T, Inter trocanter, Total Hip, Ward. As colunas são: ROI, BMD(g/cm²), BMC(g), Área(cm²), T-score', 'Z-score. Os dados que estiverem fora da tabela precisam serem descartados.