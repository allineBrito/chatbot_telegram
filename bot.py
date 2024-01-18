import telebot

CHAVE_API = "SUA_CHAVE_TELEGRAM"

bot = telebot.TeleBot(CHAVE_API)

#MAGO
@bot.message_handler(commands=["Mago"])
def opcao1(mensagem):
    with open("mago.jpg", "rb") as foto:
        bot.send_photo(mensagem.chat.id, photo=foto)

    texto = """
    Você é um mago poderoso, mas também arrogante. Você acredita que pode resolver qualquer problema com sua magia. Escolha uma opção:
    /Ajude os aldeões
    /Ignore os aldeões"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Ajude"])
def Ajude(mensagem):
    bot.send_message(mensagem.chat.id, "Você usa sua magia para derrotar os goblins. Os aldeões estão agradecidos por sua ajuda. Eles o levam para sua aldeia e lhe oferecem um lugar para ficar.")

@bot.message_handler(commands=["Ignore"])
def Ignore(mensagem):
    texto = """
    Você continua andando pela floresta. Você encontra uma caverna e decide entrar.  Escolha uma opção:
    /Continue explorando a caverna
    /Volte para a floresta"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Volte"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Você encontra um tesouro escondido na caverna. Você decide levar o tesouro para a aldeia e usá-lo para ajudar os aldeões.")

@bot.message_handler(commands=["Continue"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id, "Você continua andando pela floresta. Você encontra um grupo de goblins. Você luta contra os goblins e os derrota.")



#BRUXO

@bot.message_handler(commands=["Bruxo"])
def opcao1(mensagem):
    with open("bruxo.jpg", "rb") as foto:
        bot.send_photo(mensagem.chat.id, photo=foto)

    texto = """
    Você é um bruxo misterioso e poderoso. Você esconde seus segredos de todos, até mesmo de si mesmo. Escolha uma opção:
    /Impeca o ritual
    /Assista ao ritual"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Impeça"])
def Impeça(mensagem):
    bot.send_message(mensagem.chat.id, " Você usa sua magia para derrotar os goblins e impedir o ritual. Você sente uma força maligna dentro de você. Você não sabe se pode controlá-la.")

@bot.message_handler(commands=["Assista"])
def Assista(mensagem):
    bot.send_message(mensagem.chat.id, "Você assiste ao ritual e descobre que os goblins estão tentando invocar um demônio. Você decide impedir o ritual, mas é tarde demais. O demônio é invocado e você precisa lutar contra ele.")


#GUERREIRO
@bot.message_handler(commands=["Guerreiro"])
def opcao1(mensagem):
    with open("guerreiro.jpg", "rb") as foto:
        bot.send_photo(mensagem.chat.id, photo=foto)

    texto = """
    Você é um guerreiro forte e corajoso. Você está sempre pronto para lutar pelo que é certo. Escolha uma opção:
    /Ajude os viajantes
    /Ignore os viajantes"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Ajude"])
def Ajude(mensagem):
    bot.send_message(mensagem.chat.id, "Você usa sua magia para derrotar os goblins. Os aldeões estão agradecidos por sua ajuda. Eles o levam para sua aldeia e lhe oferecem um lugar para ficar.")

@bot.message_handler(commands=["Ignore"])
def Ignore(mensagem):
    texto = """
    Você continua andando pela floresta. Você encontra uma caverna e decide entrar.  Escolha uma opção:
    /Continue explorando a caverna
    /Volte para a floresta"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Volte"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Você encontra um tesouro escondido na caverna. Você decide levar o tesouro para a aldeia e usá-lo para ajudar os aldeões.")

@bot.message_handler(commands=["Continue"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id, "Você continua andando pela floresta. Você encontra um grupo de goblins. Você luta contra os goblins e os derrota.")


#GOBLIN
@bot.message_handler(commands=["Goblin"])
def opcao1(mensagem):
    with open("goblin.jpg", "rb") as foto:
        bot.send_photo(mensagem.chat.id, photo=foto)

    texto = """
     Você é um goblin pequeno e feio. Você é oprimido pelos humanos e pelos outros goblins. Escolha uma opção:
    /Lidere os goblins em uma revolta
    /Fuja dos humanos"""
    bot.send_message(mensagem.chat.id, texto)



@bot.message_handler(commands=["Lídere"])
def Lídere(mensagem):
    bot.send_message(mensagem.chat.id, "Você encontra um tesouro escondido na caverna. Você decide levar o tesouro para a aldeia e usá-lo para ajudar os aldeões.")

@bot.message_handler(commands=["Fuja"])
def Fuja(mensagem):
    bot.send_message(mensagem.chat.id, "Você foge dos humanos e se esconde na floresta. Você vive uma vida solitária, mas aprende a se defender.")


#CONFIGURAÇÕES
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Você acorda em uma floresta escura e desconhecida. Você não sabe como chegou lá ou quem você é. Tudo o que você sabe é que precisa encontrar uma maneira de sair. Escolha uma opção:
     /Mago
     /Bruxo
     /Guerreiro
     /Goblin """
    bot.reply_to(mensagem, texto)

bot.polling()









