# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:52:48 2022

@author: renzo
"""

from flask import Flask
import os
from twilio.rest import Client
from flask import request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)


@app.route("/")
def inicio():
    test = os.environ.get("Test")
    return test


@app.route("/mensajetxt")
def mensajetxt():
    try:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Hola amigos que onda',
            from_='+13465455006',
            to='+573173522435'
        )

        print(message.sid)
        return "Funcionando al pelo"
    except Exception as e:
        return "Error que embarrada"


@app.route("/email")
def enviarCorreo():
    
   destino = request.args.get('correo_destino')
   asunto = request.args.get('asunto')
   contenido = request.args.get('contenido')
    
   message = Mail(
       from_email='rgaravitoc@unal.edu.co',
       to_emails=destino,
       subject=asunto,
       html_content=contenido)
   try:
       sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
       response = sg.send(message)
       print(response.status_code)
       print(response.body)
       print(response.headers)
       print("Parece que si se envió")
       return "Parece que se envió el correo"
   except Exception as e:
       print("error amigos"+e.message)
       return "Que embarrada no se envió el correo"


if __name__ == "__main__":
    app.run()