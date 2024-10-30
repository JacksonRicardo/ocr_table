# OCR para Extração de Dados de Imagem de Exames Médicos

Este projeto tem como objetivo realizar a extração de texto a partir de uma imagem que contém resultados de exames médicos, utilizando OCR (Reconhecimento Óptico de Caracteres), filtrar os dados relevantes e salvar os resultados em um arquivo de texto. O código foi desenvolvido com Python e utiliza bibliotecas como EasyOCR, pandas e regex para processar os dados.

## Funcionalidades

- **Leitura de texto**: Através da imagem fornecida, o OCR extrai o texto.
- **Filtragem de dados**: O texto extraído é filtrado para identificar e capturar apenas as informações relevantes da tabela do exame.
- **Salvamento em arquivo**: Os dados filtrados são organizados em uma tabela e salvos em um arquivo de texto (.txt).

## Pré-requisitos

Antes de executar o código, certifique-se de ter instalado os seguintes pacotes:

1. **EasyOCR** - Utilizado para realizar o reconhecimento de texto nas imagens.
    ```bash
    pip install easyocr
    ```

2. **Pandas** - Utilizado para organizar os dados extraídos em formato tabular.
    ```bash
    pip install pandas
    ```

3. **Regex (re)** - Biblioteca padrão do Python, usada para busca e manipulação de padrões de texto.

## Como utilizar

1. **Clonar o repositório ou baixar o código.**

2. **Preparar a imagem**: O arquivo de imagem contendo o texto (exames médicos) deve estar em um caminho acessível. Atualize o caminho da imagem no código:
    ```python
    image_path = r'C:\Users\jacks\Music\OCR\image.png'
    ```

3. **Executar o código**: Execute o código no terminal ou ambiente Python:
    ```bash
    python script.py
    ```

4. **Saída**: O script vai extrair o texto, filtrar os dados relevantes e exibir a tabela com os dados extraídos. Além disso, os dados filtrados serão salvos em um arquivo `.txt` no caminho especificado:
    ```python
    salvar_em_txt(dados_filtrados, r'C:\Users\jacks\Music\OCR\resultado.txt')
    ```

## Estrutura do código

- **ocr_reader(image_path)**: Função responsável por inicializar o EasyOCR e extrair o texto da imagem.
- **filtrar_dados(text)**: Função para filtrar o texto extraído e capturar as informações relevantes da tabela médica.
- **salvar_em_txt(dados_df, file_path)**: Função para salvar os dados filtrados em um arquivo de texto.
- **main()**: Função principal que coordena o fluxo de execução das outras funções.

## Ajustes possíveis

- **Idiomas suportados**: O EasyOCR está configurado para reconhecer texto em português e inglês. Caso o exame esteja em outro idioma, é possível adicionar o código de idioma correspondente:
    ```python
    reader = easyocr.Reader(['pt', 'en'])
    ```

- **Padrões de busca**: O código atualmente filtra linhas que contêm palavras-chave específicas de exames médicos, como "Colo", "G.T", "Inter trocanter", "Total Hip", "Ward". Se necessário, esses padrões podem ser ajustados para adequar-se a outros formatos de tabela.

## Contribuições

Contribuições são bem-vindas! Se encontrar algum bug ou tiver sugestões para melhorias, fique à vontade
