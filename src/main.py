import start
import service

def main ():
    file = open ("list_of_words.txt", "r")
    # abre o arquivo chamado list of words

    line = file.readline()
    #le arquivo

    list_of_words = line.split(', ')
    #separa as plavras na virgula  
     
    file.close()
    #fecha o arquivo

    start.start(list_of_words)
    # chama o módulo e a função start

    service.clean_file_historic()
    print("Programa encerrado.")
    
main()