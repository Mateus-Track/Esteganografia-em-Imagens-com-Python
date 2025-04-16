from PIL import Image
import sys
import os

def escrever_senha(senha, imagem1, tamanho):
    print("\nEscrevendo senha")

    index_senha = 0
    index_bit = 7 #percorrer todos os bits (7 - 0) do char.
    coord_x = 0
    coord_y = 0
    largura, altura = imagem1.size
    while index_senha < tamanho:
        char_atual = senha[index_senha]
        # print("Char atual = " + str(char_atual))
        while index_bit >= 0:
            bit_atual = (ord(char_atual) >> index_bit) & 1

            r, g, b = imagem1.getpixel((coord_x, coord_y))
            
            red_indisponivel = (r & 1) == bit_atual
            green_indisponivel = (g & 1) == bit_atual
            blue_indisponivel = (b & 1) == bit_atual

            while((red_indisponivel) and (green_indisponivel) and (blue_indisponivel)):
                if(coord_x < largura - 1):
                    coord_x += 1
                else:
                    coord_y += 1
                    coord_x = 0
                    if(coord_y >= altura):
                        print("Mensagem muito longa para essa imagem! Não foi possível guardar.")
                        sys.exit()
                
                r, g, b = imagem1.getpixel((coord_x, coord_y))
                
                red_indisponivel = (r & 1) == bit_atual
                green_indisponivel = (g & 1) == bit_atual
                blue_indisponivel = (b & 1) == bit_atual

            if(not red_indisponivel):
                numero_alterado = r
                
            elif not green_indisponivel:
                numero_alterado = g

            elif not blue_indisponivel:
                numero_alterado = b

            else:
                print("Erro - Nenhum dos RGB disponível para a escrita.")
                sys.exit()

            numero_alterado >>= 1
            numero_alterado <<= 1
            numero_alterado |= bit_atual

            if(not red_indisponivel):
                r = numero_alterado
            elif not green_indisponivel:
                g = numero_alterado
            elif not blue_indisponivel:
                b = numero_alterado
            
            imagem1.putpixel((coord_x, coord_y), (r, g, b))
            
            if(coord_x < largura - 4):
                coord_x += 2 #dar um pouco mais de espaço entre os pixels que estão sendo alterados.
            else:
                coord_y += 1
                coord_x = 0
                if(coord_y >= altura):
                    print("Mensagem muito longa para essa imagem! Não foi possível guardar. Abortando...")
                    sys.exit()

            index_bit -= 1

        index_bit = 7
        index_senha += 1

    
    # print("Ultimas coordenadas: X = " + str(coord_x) + "Y = "+ str(coord_y))

    imagem1.save("imagens/imagem_saida/saida.png")
            
    print("Sua imagem com a senha está dentro de 'imagem/saida'!")
    print("\n")

    pergunta = input("Deseja já salvar essa imagem com a senha na pasta da senha? (1)  ")

    if(int(pergunta) == 1):
        imagem1.save("imagens/imagem_com_mensagem/mensagem_escondida.png")
        print("\nE sua imagem também está salva já dentro da pasta imagem_com_mensagem, e assim, pronta para ser revelada!\n")
        

def extraindo_mensagem(imagem1, imagem2):
    senha_criptografada = []
    index_bit = 7 # 0 - 7 = indices do byte, bit a bit
    index_senha = 0
    numero_atual = 0
    coord_x = 0
    coord_y = 0
    largura, altura = imagem1.size
    # print("Largura = " + str(largura) + "Altura = " + str(altura))
    for coord_y in range(altura):
        for coord_x in range(largura):
            r1, g1, b1 = imagem1.getpixel((coord_x, coord_y))
            r2, g2, b2 = imagem2.getpixel((coord_x, coord_y))

            if(r1 != r2):
                numero_atual |= (r2 & 1) << index_bit
                index_bit -= 1
            elif g1 != g2:
                numero_atual |= (g2 & 1) << index_bit
                index_bit -= 1

            elif b1 != b2:
                numero_atual |= (b2 & 1) << index_bit
                index_bit -= 1

            if(index_bit == -1):
                senha_criptografada.append(numero_atual)
                index_bit = 7
                index_senha+=1
                numero_atual = 0

    print("Senha Escondida: ")
    senha_string = desord(senha_criptografada)
    print(senha_string)
    

def desord(senha_inteiros):
    return ''.join(chr(n) for n in senha_inteiros)

if __name__ == "__main__": 

    decisao = input("Deseja esconder a mensagem em uma imagem (1) | ou revelar a senha de uma já existente (2) ?  \n")

    pasta_entrada = "imagens/imagem_entrada"
    arquivos = os.listdir(pasta_entrada)
    if arquivos:
        arquivo = os.path.join(pasta_entrada, arquivos[0])
    else:
        print("Sem arquivo na pasta de entrada!")
        sys.exit()

    if(int(decisao) == 1):

        senha = input('Digite a mensagem que vai ser escondida na imagem: ')

        tamanho = len(senha)
        nome = os.path.basename(arquivo)
        extensao = os.path.splitext(nome)[1].lower()  
        imagem1 = Image.open(arquivo)  

        if extensao in ['.jpg', '.jpeg']:

            novo_nome = os.path.splitext(arquivo)[0] + ".png"
            imagem1.save(novo_nome)
            imagem1.close()

            imagem_antiga = "imagens/imagem_entrada/" + nome
            os.remove(imagem_antiga)

            arquivos = os.listdir(pasta_entrada)
            arquivo = os.path.join(pasta_entrada, arquivos[0])

            imagem1 = Image.open(arquivo)
        
        imagem1 = imagem1.convert("RGB")
        escrever_senha(senha, imagem1, tamanho)

        
    elif int(decisao) == 2:
        
        imagem_original = Image.open(arquivo)

        pasta_senha = "imagens/imagem_com_mensagem"
        arquivos = os.listdir(pasta_senha)
        if arquivos:
            arquivo = os.path.join(pasta_senha, arquivos[0])
        else:
            print("Sem arquivo na pasta de imagem com senha!")
            sys.exit()
        
        imagem_criptografada = Image.open(arquivo)

        imagem_criptografada = imagem_criptografada.convert("RGB")
        imagem_original = imagem_original.convert("RGB")
        extraindo_mensagem(imagem_original, imagem_criptografada)
    else:
        print("Decisao invalida!")
    