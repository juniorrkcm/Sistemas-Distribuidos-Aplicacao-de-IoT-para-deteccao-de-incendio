import pika
import tkinter as tk
from tkinter import messagebox

def callback(ch, method, properties, body):
    message = body.decode('utf-8')  # Converte bytes para string
    print(message)  # Imprime a mensagem recebida

    # Verifica se a mensagem indica a detecção de incêndio
    if "Incêndio detectado!" in message:
        print("Incêndio detectado!")
        show_alert_popup()

def show_alert_popup():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    messagebox.showwarning("Alerta de Incêndio", "Um incêndio foi detectado!")
    root.destroy()  # Fecha a janela após a exibição da mensagem

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='fire_detection')

    channel.basic_consume(queue='fire_detection', on_message_callback=callback, auto_ack=True)

    print('Aguardando detecção de incêndio...')

    channel.start_consuming()

if __name__ == "__main__":
    main()
