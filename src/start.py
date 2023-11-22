import service
import utilities
import show_command_line as menus

def start (list_of_words):
    while True:
        menus.home_menu()
        option  = utilities.valided_input_int(utilities.comand_line_colors.colour("\t Digite sua opção: ", utilities.comand_line_colors.BLUE))

        if option == 1:
            break

        elif option == 2:
            menus.show()
            input()
            continue

        elif option == 3:
            return False
    
    while True:  
        while True:

            secret_word = service.get_secret_word(list_of_words) # verifica se a palavra está no arquivo de palavras usadas
            
            if service.word_exists_used_words(secret_word) == False:
                break

        result_round =  start_round(secret_word) # adiciona secret_word no arquivo de palavras usadas

        if result_round:
            service.add_word_in_file(secret_word)

        if show_menu() == False:
            return True

    return False


def start_round(secret_word):
    
    list_type_words = []

    for _ in range(5):
            
        while True:
            word = service.input_guess("Digite seu palpite: ")

            if word in list_type_words:
                print("Você já digitou essa palavra.")
                continue
                
            list_type_words.append(word)
            break

        result, letters = service.check_word(word, secret_word)

        if result == True:
            print(f"\t {letters[0]}|{letters[1]}|{letters[2]}|{letters[3]}|{letters[4]}")
            print("\t \033[38;5;206m🎉Parabéns você acertou a palavra!!🎉\n \033[0m")
            list_type_words.clear()
            return True
        
        else:
            print(f"\t {letters[0]}|{letters[1]}|{letters[2]}|{letters[3]}|{letters[4]}")

       
    list_type_words.clear()

    print("Não foi dessa vez, tente na próxima.") 

    return False

def show_menu():
    while True:
        menus.menu()
        option = utilities.valided_input_int(utilities.comand_line_colors.colour("\t Digite sua opção: ", utilities.comand_line_colors.BLUE))

        if option == 1:
            break

        elif option == 2:
            menus.show()
            input()
            continue
                
        if option == 3:
            return False
        
        elif option ==4:
            service.show_words_drawn()
            continue


        elif option ==5:
            service.clean_file_historic ()
            continue
    return True
