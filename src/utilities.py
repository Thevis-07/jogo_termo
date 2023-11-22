import sys
import os
import time

class comand_line_colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    RESET = '\033[0m'

    @staticmethod
    def colour(text, color):
        return color + text + comand_line_colors.RESET

def clean_and_back():# mova o cursor para o incio da ultima linha
    
    sys.stdout.write('\x1b[1A')
    # Apague a última linha
    sys.stdout.write('\x1b[2K')

def validate_number_letters_and_letters(message, number_letters):
    laps = 0
    while True:
            
            word = input (message)

            if not validation_string(word):
                laps += 1
                print("Digite apenas palavras válidas")
                time_sleep(2)
                while laps < 0:
                    clean_and_back()
                continue

            elif len(word) != number_letters:
                laps += 1
                print("A palavra deve ter 5 letras.")
                time_sleep(2)
                while laps < 0:
                    clean_and_back()
                continue
                
            if verifiy_space (word):
                 print ("A palavra não deve ter espaço.")
                 continue
            
            break
    return word

def validated_sim_nao (message):
      """
      Função que valida se a resposta do usuario foi S ou N.
      Se não for S ou N solicita que o usuario digite novamente a resposta.

      :param message: Nota para o usuario.
      :return: S/N
      """

      while True: 
             opition = input(message).upper() 
             if opition == "S": 
                 
                 return opition 
  
             elif opition == "N": 
                 return opition
            
             else:  
                 print ("Resposta inválida tente novamente.") 


def clear():
      """
      Função para limpar o terminal
      """
      os.system("cls")

def validation_string (string):
    for i in range (len(string)):
          
        try:
            num = int (string[i])           
            return False
               
        except ValueError:           
            continue
          
    return True   
               
def time_sleep(value):
     """
     Função que conta um tempo de espera
     :param value: 
     """
     time.sleep(value)

def verifiy_space (string):
     
     return len(string.split()) > 1

def valided_input_int(message):
    """
    Entrada de numero inteiro validada, aceita apenas numeros inteiro
    Se a entrada não for um numero inteiro solicita que digite novamente
    retorna um numreo inteiro

    :param message: Nota para o usuario.
    :return: Numero inteiro.
    """

    while True:        
             value = input(message) 
             try: 
                value = int(value) 
             except ValueError: 
                print("Opção inválida, tente novamente...") 
                time_sleep(1) 
                continue 
             break
    return int(value)
