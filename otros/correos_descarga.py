import imaplib

# Conectarse al servidor de correo electrónico
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('tu_correo_electronico', 'tu_contraseña')
mail.select('inbox')

import email

# Buscar correos electrónicos con archivos adjuntos
status, messages = mail.search(None, '(BODY[TEXT] "has:attachment")')

# Leer los correos electrónicos
messages = messages[0].split(b' ')

for num in messages:
    status, msg = mail.fetch(num, '(RFC822)')
    raw_message = msg[0][1]

    # Parsear el correo electrónico
    message = email.message_from_bytes(raw_message)

    # Buscar archivos adjuntos
    for part in message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        # Descargar el archivo adjunto
        filename = part.get_filename()
        with open(filename, 'wb') as f:
            f.write(part.get_payload(decode=True))


# Cerrar la conexión
mail.close()
mail.logout()