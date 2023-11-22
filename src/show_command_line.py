from utilities import comand_line_colors as color

def home_menu():
    print(color.colour("\t Bem-vindo ao jogo Termo!", color.MAGENTA))
    print (color.colour("\t-------------------------------", color.MAGENTA))
    print (color.colour("\t 1 - Inciar primeira partida.", color.CYAN))
    print (color.colour("\t 2 - Como jogar.", color.CYAN))
    print (color.colour("\t 3 - Sair", color.CYAN))
    print (color.colour("\t-------------------------------", color.MAGENTA))

def menu():
    print(color.colour("\t\t  Termo!", color.MAGENTA))
    print (color.colour("\t-------------------------------", color.MAGENTA))
    print (color.colour("\t 1 - Próxima partida", color.CYAN))
    print (color.colour("\t 2 - Como jogar.", color.CYAN))
    print (color.colour("\t 3 - Sair", color.CYAN))
    print (color.colour("\t 4 - Ver palavras sorteadas", color.CYAN))
    print (color.colour("\t 5 - Limpar palavras sorteadas", color.CYAN))
    print (color.colour("\t-------------------------------", color.MAGENTA))

def show():

    print(color.colour("Regras do jogo: ", color.RED))
    print("\tA palavra do dia sempre tem 5 letras. Você tem seis chances para adivinhar a palavra.")
    print(color.colour("Fazendo um Palpite: ", color.CYAN))
    print("\tEm cada tentativa, você insere uma palavra de 5 letras. Após cada tentativa, o jogo fornece feedback sobre quão perto você está da palavra correta.")
    print(color.colour("Feedback do Jogo:", color.BLUE))
    print("\tSe uma letra está na palavra e na posição correta, ela será destacada de verde. Se uma letra está na palavra, mas na posição errada, será destacada de amarelo. E se a letra não estiver na palavra de todo, ela ficará cinza")
