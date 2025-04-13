from PIL import Image
import sys
import os


def escrever_senha(senha, imagem1, tamanho):
    print("Escrevendo senha")

    index_senha = 0
    index_bit = 7 #reverso
    coord_x = 0
    coord_y = 0
    
    while index_senha < tamanho:
        char_atual = senha[index_senha]
        print("Numero atual = " + str(char_atual))
        while index_bit >= 0:
            bit_atual = (ord(char_atual) >> index_bit) & 1

            r, g, b = imagem1.getpixel((coord_x, coord_y))
            # print("r antes = " + str(r))
            numero_alterado = int(r)
            while((numero_alterado & 1) == bit_atual):
                coord_x+=1
                coord_y+=1
                r, g, b = imagem1.getpixel((coord_x, coord_y))
                # print(f"Pixel em ({coord_x}, {coord_y}): R={r}, G={g}, B={b}")
                # print("r antes = " + str(r))
                numero_alterado = int(r)
            
            print("Achei")
            numero_alterado >>= 1
            numero_alterado <<= 1
            numero_alterado |= bit_atual

            r = numero_alterado
            # print("r depois = " + str(r))
            
            imagem1.putpixel((coord_x, coord_y), (r, g, b))
            print("pixel alterado no coord x = " + str(coord_x) + "e coord y = " + str(coord_y))

            # print("Bit = "+ str(bit_atual))
            # print("Index bit = "+ str(index_bit))
            index_bit -= 1
            coord_x += 1
            coord_y += 1

        index_bit = 7
        print("\n\n")

        index_senha += 1

    imagem1.save("imagem_saida/saida.png")
    # sys.exit()


def escrever_senha_completo(senha, imagem1, tamanho):
    print("Escrevendo senha")

    index_senha = 0
    index_bit = 7 #reverso
    coord_x = 0
    coord_y = 0
    largura, altura = imagem1.size
    while index_senha < tamanho:
        char_atual = senha[index_senha]
        print("Char atual = " + str(char_atual))
        while index_bit >= 0:
            bit_atual = (ord(char_atual) >> index_bit) & 1

            # print("Indo nas coordenadas:  X = " + str(coord_x) + "Y = "+ str(coord_y))

            r, g, b = imagem1.getpixel((coord_x, coord_y))
            
            numero_alterado_r = int(r)
            red_indisponivel = (numero_alterado_r & 1) == bit_atual
            numero_alterado_g = int(g)
            green_indisponivel = (numero_alterado_g & 1) == bit_atual
            numero_alterado_b = int(b)
            blue_indisponivel = (numero_alterado_b & 1) == bit_atual
            while((red_indisponivel) and (green_indisponivel) and (blue_indisponivel)):
                if(coord_x < largura - 1):
                    coord_x += 1
                else:
                    coord_y += 1
                    coord_x = 0
                
                # print("Indo nas coordenadas:  X = " + str(coord_x) + "Y = "+ str(coord_y))
                r, g, b = imagem1.getpixel((coord_x, coord_y))
                
                numero_alterado_r = int(r)
                red_indisponivel = (numero_alterado_r & 1) == bit_atual
                numero_alterado_g = int(g)
                green_indisponivel = (numero_alterado_g & 1) == bit_atual
                numero_alterado_b = int(b)
                blue_indisponivel = (numero_alterado_b & 1) == bit_atual

            if(not red_indisponivel):
                numero_alterado = int(r)
                
            elif not green_indisponivel:
                numero_alterado= int(g)

            elif not blue_indisponivel:
                numero_alterado = int(b)

            else:
                print("ERRO - Na hora de definir o RGB onde seria escrito")
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

            # print("r depois = " + str(r))
            
            imagem1.putpixel((coord_x, coord_y), (r, g, b))
            
            # print("Bit = "+ str(bit_atual))
            # print("Index bit = "+ str(index_bit))
            if(coord_x < largura - 5):
                coord_x += 2
            else:
                coord_y += 1
                coord_x = 0

            index_bit -= 1

        index_bit = 7
        index_senha += 1

    print("Ultimas coordenadas: X = " + str(coord_x) + "Y = "+ str(coord_y))

    imagem1.save("imagem_saida/saida.png")

    pergunta = input("Deseja ja salvar essa imagem com a senha na pasta criptografada? (1)")
    if(int(pergunta) == 1):
        imagem1.save("imagem_criptografada/senha.png")
    

def comparar_imagens(imagem1, imagem2):
    print("Comparar")
    senha_criptografada = []
    index_senha = 0
    index_bit = 7 #reverso
    numero_atual = 0
    coord_x = 0
    coord_y = 0
    largura, altura = imagem1.size
    print("Largura = " + str(largura) + "Altura = " + str(altura))
    # sys.exit()
    for coord_x in range(largura):
        for coord_y in range(altura):
            r1, g1, b1 = imagem1.getpixel((coord_x, coord_y))
            r2, g2, b2 = imagem2.getpixel((coord_x, coord_y))
            # print("r1 = " + str(r1) + "r2 = " + str(r2))
            if(r1 != r2):
                print("Pixels diferentes na coord x = " + str(coord_x) + "e coord y = " + str(coord_y))
                print("r2 = " + str(r2))
                numero_atual |= (r2 & 1) << index_bit
                print("NUmero atual agr momentos = " + str(numero_atual))
                index_bit -= 1
            if(index_bit == -1):
                print("numero atual descoberto = " + str(numero_atual))
                print("Index senha = " + str(index_senha))
                senha_criptografada.append(numero_atual)
                index_bit = 7
                index_senha+=1
                numero_atual = 0
    print("senha criptografada: ")
    i=0
    senha_string = desord(senha_criptografada)
    print(senha_string)
    # while i < 6:
    #     print(str(senha_criptografada[i]))
    #     i += 1

    

def comparar_imagens_completo(imagem1, imagem2):
    print("Comparar completo")
    senha_criptografada = []
    index_senha = 0
    index_bit = 7 #reverso
    numero_atual = 0
    coord_x = 0
    coord_y = 0
    largura, altura = imagem1.size
    print("Largura = " + str(largura) + "Altura = " + str(altura))
    # sys.exit()
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

    pasta_entrada = "imagem_entrada"
    arquivos = os.listdir(pasta_entrada)
    if arquivos:
        arquivo = os.path.join(pasta_entrada, arquivos[0])
    else:
        print("Sem arquivo na pasta de entrada!")
        sys.exit()

    if(int(decisao) == 1):

        senha = input('Digite a mensagem que vai ser escondida na imagem: ')

        tamanho = len(senha)

        imagem1 = Image.open(arquivo)
        
        imagem_original = imagem1


        imagem1 = imagem1.convert("RGB")

        # escrever_senha(senha, imagem1, tamanho)
        escrever_senha_completo(senha, imagem1, tamanho)
        
        print("Sua imagem com a senha está dentro de 'imagem/saida'!")
        
    elif int(decisao) == 2:
        
        imagem_original = Image.open(arquivo)
        imagem_original = imagem_original.convert("RGB")

        pasta_senha = "imagem_criptografada"
        arquivos = os.listdir(pasta_senha)
        if arquivos:
            arquivo = os.path.join(pasta_senha, arquivos[0])
        else:
            print("Sem arquivo na pasta de imagem com senha!")
            sys.exit()
        
        imagem_criptografada = Image.open(arquivo)
        imagem_criptografada = imagem_criptografada.convert("RGB")

        # comparar_imagens(imagem_original, imagem_criptografada)
        comparar_imagens_completo(imagem_original, imagem_criptografada)
    else:
        print("Decisao invalida!")
    