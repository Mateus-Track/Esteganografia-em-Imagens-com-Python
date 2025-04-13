# Projeto de Esteganografia - Esconder mensagens dentro de imagens

Com esse projeto, é possível inserir uma imagem do tipo PNG na pasta "imagem_entrada", e assim executar a "main.py" buscando esconder uma mensagem dentro dessa imagem.

Dessa forma, caso essa mensagem caiba na imagem inserida, esse texto será escrito dentro da imagem de maneira sutil dentro de seus pixels, e depois salva dentro da pasta "imagem_saida". 

No final da execução, é possível também já salvar essa imagem na pasta "imagem_com_mensagem", facilitando o próximo passo.

Assim, com a sua imagem original dentro da pasta de entrada, e com a sua imagem de saída dentro da pasta "imagem_com_mensagem", executando o código buscando revelar a mensagem vai assim printar no terminal o seu texto secreto!

Para realizar esse procedimento, o código utiliza de uma técnica de Esteganografia para alterar o bit menos significativo de um dos valores do RGB de um pixel, onde para cada caracter ele precisa de 8 pixels para escondê-lo.
Nesse sentido, como apenas o bit menos significativo está sendo alterado (para 0 ou 1, dependendo para qual bit do caracter ele precisa ser transformado), a diferença de cor do pixel alterado é muito sutil, o que torna muito difícil saber que aquela mensagem foi alterada.

Além disso, como a imagem se mantém quase idêntica à original, saber qual a mensagem escondida sem ter a imagem original se torna quase impossível.

Por padrão, está uma imagem de uma paisagem em Itajaí, que no arquivo imagem_saida e no arquivo imagem_com_mensagem contém essa foto com todo o texto do roteiro do filme Shrek 2 escondido. Para revelar, basta rodar o código e escolher a opção para ele revelar a mensagem, porém, é possível escrever uma nova mensagem na imagem, ou também fazer isso com qualquer outra imagem PNG inserida.
