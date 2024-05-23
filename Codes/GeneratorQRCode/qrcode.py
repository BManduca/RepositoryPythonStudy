import pyqrcode
import png

# Link desejado para o QRCode #
qrcode = pyqrcode.create("https://github.com/BManduca")


# Salva o QRCode gerado no local desejado #
qrcode.png("github_BManduca.png", scale=6)