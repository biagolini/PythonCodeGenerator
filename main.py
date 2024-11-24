import qrcode

# Link para o QR Code
data = "https://www.linkedin.com/in/biagolini/"

# Gerar QR Code
qr = qrcode.make(data)

# Salvar em um arquivo
qr.save("qrcode.png")