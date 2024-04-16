import pika
import psutil
import sys
import time

def get_cpu_temperature():
    # Utilize a função da biblioteca psutil para obter a temperatura da CPU
    temperature = psutil.sensors_temperatures()['coretemp'][0].current
    return temperature

def publish_temperature(channel, temperature):
    message = f'Temperature: {temperature:.2f}°C'
    channel.basic_publish(exchange='', routing_key='cpu_temperature', body=message)
    print(f" [x] Sent '{message}'")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cpu_temperature')

    while True:
        temperature = get_cpu_temperature()
        publish_temperature(channel, temperature)
        time.sleep(1)

    connection.close()

if __name__ == "__main__":
    main()
