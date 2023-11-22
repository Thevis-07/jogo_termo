import utilities
import random

def input_guess(message): 

    guess = utilities.validate_number_letters_and_letters(message, 5)
    
    utilities.clean_and_back()
    return guess.upper()

def check_word(guess, secret_word):
    letters_used = [] 
    result = [1, 2, 3, 4, 5]

    for i in range (len(guess)): # usa o for pra percorrer as letras da palavra digitada 
        if guess [i] == secret_word[i]: # verifica se a lestra da palavra digitada está na mesma posição da secret word
            result[i] = utilities.comand_line_colors.colour(guess[i], utilities.comand_line_colors.GREEN) #verde adiciona a lestra digitada na mesma posição da secret word, na cor verde :)
            letters_used.append(guess[i]) # adiciona a letra na lista de letras usadas

    for j in range (len(guess)):
        if guess[j] in secret_word and guess[j] not in letters_used:
            result[j] = utilities.comand_line_colors.colour(guess[j], utilities.comand_line_colors.YELLOW)  # amarelo
            letters_used.append(guess[j])
    

    for x in range (len(guess)):
        if guess[x] not in secret_word: # verifica se a lestra não está na palavra secreta
            result[x] = utilities.comand_line_colors.colour(guess[x], utilities.comand_line_colors.WHITE)  # branco para letras ausentes

        elif isinstance(result[x], int): # 
            result[x] = '\033[97m' + guess[x] + '\033[0m'

    if secret_word == guess:
            return True, result
 
    return False, result

def get_secret_word(list_of_words): #Remova espaços em branco e quebras de linha de cada palavra

    list_of_words = [word.strip() for word in list_of_words]
    
    secret_word = random.choice(list_of_words).strip() # gera uma palavra aleatória e guarda na secret word
     
    return secret_word
 

def validation_used_words (list_of_type_words, type_word): # função para adicionar a secret word no arquivo

    if type_word in list_of_type_words:

        return True
    
    return False

def add_word_in_file (word): 

    file = open('used_words.txt', 'a')
    
    file.write(str(f'{word}\n'))

    file.close()

    return True

def word_exists_used_words(word): # verifica se uma determinada palavra existe no arquivo used words
    
    file = open('used_words.txt', 'r') 
    if word in file: # verifica se a palavra está no arquivo
        file.close()
        return True
    file.close()
    return False

def clean_file_historic (): # função pra limpar o used words
  
    file = open('used_words.txt', 'w')

    file.close ()

def show_words_drawn():
    file = open ("used_words.txt", "r")
    
    print(utilities.comand_line_colors.colour("\t As palavras sorteadas são: ", utilities.comand_line_colors.MAGENTA))
    counter = 0
    for linha in file:
        counter += 1
        palavra = linha.strip() # Remova os espaços em branco no início e no fim da linha
       
        print(f"\t {palavra}")  # Imprima a palavra
     
    lines = file.readlines()

    if counter == 0:
        print (utilities.comand_line_colors.colour("\t Você ainda não possui palavras salvas. ", utilities.comand_line_colors.RED))
        print("\n\n")
        return False
    
    file.close()
    print("\n\n")
    return
