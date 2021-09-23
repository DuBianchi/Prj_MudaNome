import re #regular expression
import os #para caminhas pelos diretorios
import shutil #para que seja possivel alterar o nome do arquivo

main_folder = r'C:\Users\Bianchi\Desktop\Peixes'
segue = 0
# função para renomear o arquivo
def rename_file(file):
    #separar o nome do arquivo da extensao
    file_name, file_extension = os.path.splitext(file) # o splitext é um path da os que ja faz essa separação
    file_name_numbers = re.findall(r'\d+', file_name)

    # verificar se o return retornou algum numero, caso não ele retorna o nome mesmo
    if not file_name_numbers:
        return file

    file_name_numbers = file_name_numbers[0].zfill(4) #função da zfill aumenta a quantidade de numeros 0 conforme colocado nos parenteses

    return f'{file_name_numbers}{file_extension}'

# função que le o nome dos arquivos e que retorna os parametros
def file_loop(root, dirs, files):
    for file in files:
        if not re.search(r'\.txt$', file): #verifica se o arquivo a ser alterado é mesmo txt
            continue
   
        new_file_name = rename_file(file)
        #pegar o nome antigo do arquivo   
        old_file_full_path = os.path.join(root, file)
        #pegar o nome novo do arquivo
        new_file_full_path = os.path.join(root, new_file_name)
        #verificando a mudança de nome
        print(f'Movendo arquivo "{file}" para "{new_file_name}"')
        #mudando o nome do arquivo atraves da função shutill
        shutil.move(old_file_full_path, new_file_full_path)

# função que entra nas pastas verificandos os parametros passados dos diretorios
def main_loop():
    for root, dirs, files in os.walk(main_folder):
        file_loop(root, dirs, files)


if __name__ == '__main__':
    main_loop()


segue = input('Digite qualquer tecla para continuar...')