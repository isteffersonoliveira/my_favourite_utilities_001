import streamlit as st
import string
from nltk.corpus import stopwords
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Baixar o conjunto de stopwords
nltk.download('stopwords')
nltk.download('punkt')


def process_text(text, to_lower, to_upper, to_title, replace_word, replace_with, tokenize, count_tokens, remove_punct,
                 remove_stopwords, to_list):
    if to_lower:
        text = text.lower()
    if to_upper:
        text = text.upper()
    if to_title:
        text = text.title()
    if replace_word and replace_with:
        text = text.replace(replace_word, replace_with)
    if remove_punct:
        text = text.translate(str.maketrans('', '', string.punctuation))
    if remove_stopwords:
        text = ' '.join([word for word in text.split() if word.lower() not in stopwords.words('portuguese')])
    if tokenize or to_list:
        tokens = nltk.word_tokenize(text)
        if count_tokens:
            st.write(f"Number of Tokens: {len(tokens)}")
        if to_list:
            return tokens
        text = ', '.join(tokens)
    return text

st.title('Editar Texto :page_facing_up:')

# Barra lateral com links úteis
st.sidebar.markdown("### Ferramentas Úteis 🛠️")
st.sidebar.markdown("[🌐 Gere Nuvens de Palavras e Analise Textos!](https://myfavouriteutilitiestextedit.streamlit.app/) - Transforme seus textos em visualizações impactantes e obtenha insights rápidos!")
st.sidebar.markdown("[🔍 Crie QR Codes de Graça!](https://myfavouriteutilitiesqrcodea.streamlit.app/) - Converta textos e links em QR Codes facilmente!")


# Adicione mais links conforme necessário

# Caixa de texto para entrada do usuário
user_input = st.text_area("Enter your text here:", height=300)

# Caixas de ferramenta para edição de texto
to_lower = st.checkbox('Minúsculo')
to_upper = st.checkbox('Maiúsculo')
to_title = st.checkbox('Título')
replace_word = st.text_input('Substituir palavra:')
replace_with = st.text_input('Substituir com:')
tokenize = st.checkbox('Tokenizar')
count_tokens = st.checkbox('Contar Tokens')
remove_punct = st.checkbox('Remover Pontuação')
remove_stopwords = st.checkbox('Remover Stopwords')
to_list = st.checkbox('Converter para Lista')

# Adicione uma opção para exibir a nuvem de palavras
show_wordcloud = st.checkbox('Exibir Nuvem de Palavras')

# Botão "Processar"
if st.button('Processar', key='btnProcessar'):
    # Processar o texto com base nas opções selecionadas
    result = process_text(user_input, to_lower, to_upper, to_title, replace_word, replace_with, tokenize,
                          count_tokens,
                          remove_punct, remove_stopwords, to_list)

    # Exibir o resultado em outra caixa de texto
    if isinstance(result, list):
        st.write("Lista de Itens:", result)
    else:
        st.text_area("Resultado:", value=result, height=200, max_chars=None, key=None)

    # Exibir contagem de palavras e caracteres
    if isinstance(result, list):
        st.write(f"Number of Words: {len(result)}")
        st.write(f"Number of Characters: {sum(len(word) for word in result)}")
    else:
        st.write(f"Number of Words: {len(result.split())}")
        st.write(f"Number of Characters: {len(result)}")

    # Exibir a nuvem de palavras, se a opção estiver marcada
    if show_wordcloud:
        if isinstance(result, list):
            text_for_wordcloud = ' '.join(result)
        else:
            text_for_wordcloud = result

        wordcloud = WordCloud(width=800, height=400, background_color='white', min_font_size=10).generate(
            text_for_wordcloud)

        plt.figure(figsize=(8, 6), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)

        st.pyplot(plt)

st.title('Manipulação de Strings em Python')

st.markdown("""


Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. É um dos idiomas mais versáteis e poderosos, conhecido por sua simplicidade e legibilidade de código. Uma das muitas áreas em que Python se destaca é a manipulação e edição de strings.

### 1. Conversão de Caixa
Python fornece métodos como `lower()` para converter uma string para minúsculas, `upper()` para maiúsculas e `title()` para converter a primeira letra de cada palavra em maiúscula.
```python
texto = "Python é Incrível"
print(texto.lower())  # python é incrível
print(texto.upper())  # PYTHON É INCRÍVEL
print(texto.title())  # Python É Incrível
``` 

### 2. Substituição de Texto

O método replace(old, new) é usado para substituir todas as ocorrências de uma sub-string por outra.


```
texto = "Python é divertido"
novo_texto = texto.replace("divertido", "incrível")
print(novo_texto)  # Python é incrível
```

### 3. Tokenização e Contagem de Tokens

Tokenização é o processo de converter uma string em uma lista de substrings (tokens), geralmente palavras. Isso pode ser alcançado usando o método split(). Para contar o número de tokens, você pode usar a função len() na lista de tokens.

```
texto = "Aprender Python é recompensador"
tokens = texto.split()
print(tokens)  # ['Aprender', 'Python', 'é', 'recompensador']
print(len(tokens))  # 4
```

### 4. Concatenação de Strings

Strings podem ser concatenadas usando o operador +.

```
saudacao = "Olá"
nome = "Mundo"
mensagem = saudacao + ", " + nome + "!"
print(mensagem)  # Olá, Mundo!
```

### 5. Fatiamento de Strings

Python permite que você acesse sub-strings através de fatiamento, especificando o índice inicial e final.

```
texto = "Python"
print(texto[1:4])  # yth
```

### 6. Formatação de Strings

Python 3.6 introduziu as f-strings, uma maneira conveniente de embutir expressões dentro de literais de string.

```
nome = "Mundo"
mensagem = f"Olá, {nome}!"
print(mensagem)  # Olá, Mundo!
```

### Conclusão

Python, com sua sintaxe clara e concisa, oferece uma variedade de métodos e operações para manipular strings de maneira eficiente. Seja você um cientista de dados, desenvolvedor web, ou apenas alguém que gosta de automatizar tarefas pequenas, a habilidade de manipular strings é uma ferramenta valiosa no seu arsenal de programação Python.
""")
