# Esteganografia em Imagens PNG com Python

Com esse projeto, é possível inserir uma imagem do tipo PNG na pasta "imagem_entrada", e assim executar a "main.py" buscando esconder uma mensagem dentro dessa imagem.

## Como Funciona
Dessa forma, caso sua mensagem caiba na imagem inserida, esse texto será escrito dentro da imagem de maneira sutil dentro de seus pixels, onde o bit menos significativo de um dos valores do RGB é alterado (para 0 ou 1, dependendo qual o bit do caracter que precisa ser escrito). 
Após inserir a mensagem, o programa salva a nova imagem obrigatoriamente na pasta de saída, e se você preferir, já também salva na pasta "imagem_com_mensagem":

- `imagem_saida/` → imagem com a mensagem escondida
- `imagem_com_mensagem/` → imagem que terá sua mensagem revelada

---
Assim, com a sua imagem original dentro da pasta de entrada, e com a sua imagem com a mensagem escrita dentro da pasta "imagem_com_mensagem", é possível executar o código buscando revelar sua mensagem, dessa forma será printado no terminal o seu texto secreto! Vale ressaltar que é importante que só haja uma única imagem dentro de cada uma das pastas.

## Vantagens
Nesse sentido, como apenas o bit menos significativo está sendo alterado (para 0 ou 1, dependendo para qual bit do caracter ele precisa ser transformado), a diferença de cor do pixel alterado é muito sutil, o que torna muito difícil saber que aquela mensagem foi alterada.

Além disso, como a imagem se mantém quase idêntica à original, saber qual a mensagem escondida sem ter a imagem original se torna quase impossível.

## Texto padrão do repositório
Por padrão, está uma imagem de uma paisagem em Itajaí, que no arquivo imagem_saida e no arquivo imagem_com_mensagem contém essa foto com todo o texto do roteiro do filme Shrek 2 escondido. Para revelar, basta rodar o código e escolher a opção para ele revelar a mensagem, porém, é possível escrever uma nova mensagem na imagem, ou também fazer isso com qualquer outra imagem PNG inserida.

## ⚙️ Requisitos

Para executar este projeto, você precisa apenas de:

- Python
- Biblioteca [Pillow](https://python-pillow.org/) para manipular imagens PNG

### Instalação da biblioteca Pillow:

Você pode instalar o Pillow facilmente com:

```bash
pip install Pillow
```


## 📁 Estrutura de Pastas

```bash
📂 imagens
│  ├── 📂 imagem_entrada         # Pasta onde é inserido o PNG original
│  ├── 📂 imagem_saida           # Pasta que vai possuir o PNG de saída, com a mensagem escondida
│  └── 📂 imagem_com_mensagem    # Pasta que possui a imagem pronta para revelar o conteúdo oculto
📄 main.py                       # Script principal que lê e grava as imagens
