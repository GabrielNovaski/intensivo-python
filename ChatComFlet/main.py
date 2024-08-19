#TItulo
#Botao: Iniciar o chat
    #popup
    #Campo de Texto: Escreva seu nome no chat
    #Botao: Entrar no chat
        #Sumir com o titutlo eo botao inicial
        #Fechar o popup
        #criar o chat (com a mensagem de "usuario" entrou no chat)
        #Embaixo do chat
            #Campo de texto: Digite sua mensagme
            #Botao enviar
                #Vai aparecer a mensagem no chat com o nome do usuario
                #Usuario: TESTANDO


import flet as ft

def main(pagina):
    def entrar_chat(e):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)

        textou_entrou_chat = (f'{campo_nome_usuario.value} entrou no chat')
        pagina.pubsub.send_all(textou_entrou_chat)

        pagina.update()

    def abrir_popup(e):
        pagina.dialog = janela
        janela.open = True

        pagina.update()

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(e):
        #Usuario: Mensagem
        texto = f'{campo_nome_usuario.value}: {texto_mensagem.value}'

        pagina.pubsub.send_all(texto)

        texto_mensagem.value = ''
        pagina.update()


    titulo = ft.Text("Chat Online")
    botao_iniciar = ft.ElevatedButton('INICIAR CONVERSA', on_click=abrir_popup)   
    
    titulo_janela = ft.Text('Bem Vindo ao Chat')
    campo_nome_usuario = ft.TextField(label='Nome de Usuario')
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    texto_mensagem = ft.TextField(label='Digite sua mensagem', width=300, on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    chat = ft.Column()

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)