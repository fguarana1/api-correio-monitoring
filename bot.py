import requests
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuração de e-mail
email_sender = 'vinxxxxxx06@gmail.com'
email_password = 'xxxxxxxxxx'  # Senha do App
email_receivers = ['felipe.guarana@xxxxx.com.br','sergio@xxxxxx.com.br','guilherme.ferreira@xxxxx.com.br', 'mmicalli@xxxxxx.com.br']
smtp_server = 'smtp.gmail.com'
smtp_port = 587

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = ", ".join(email_receivers)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_sender, email_password)
            text = msg.as_string()
            server.sendmail(email_sender, email_receivers, text)
        log_message("E-mail enviado com sucesso.")
    except Exception as e:
        log_message(f"Falha ao enviar e-mail: {e}")

def check_correios_api():
    url = "https://api.correios.com.br/token/v3/api-docs"
    while True:
        current_hour = datetime.now().hour
        if 6 <= current_hour < 22:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    log_message("API dos Correios está funcionando.")
                    time.sleep(300)  # Dormir por 5 minutos (300 segundos)
                else:
                    error_message = f"API dos Correios não está funcionando, voltarei a checar em 1 hora. Código de status: {response.status_code}"
                    log_message(error_message)
                    send_email("Alerta API dos Correios", error_message)
                    time.sleep(3600)  # Dormir por 1 hora (3600 segundos)
            except requests.RequestException as e:
                error_message = f"Erro ao acessar API dos Correios: {e}"
                log_message(error_message)
                send_email("Alerta API dos Correios", error_message)
                time.sleep(3600)  # Dormir por 1 hora (3600 segundos)
        else:
            log_message("Fora do horário de funcionamento. Encerrando...")
            break

def log_message(message):
    print(f"{datetime.now()}: {message}")

if __name__ == "__main__":
    check_correios_api()
