import os
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader

from app import app

from flask import send_from_directory

UPLOAD_FOLDER = "/home/laws/abtms/app/static/comprovantes/"

months = ["Desconhecido",
          "Janeiro",
          "Fevereiro",
          "Março",
          "Abril",
          "Março",
          "Junho",
          "Julho",
          "Agosto",
          "Setembro",
          "Outubro",
          "Novembro",
          "Dezembro"]



class Print():
	def print(self, name, code, createdAt):
		filename = generate_password_hash("form_letter") + ".pdf"

		logo = app.static_folder + "/imgs/" + "background.png"
		type = "Pessoa Física"

		logo = ImageReader(logo)

		canvas = Canvas(UPLOAD_FOLDER + filename, pagesize=letter)
		canvas.drawImage(logo, 20, 20, mask='auto')

		canvas.setFont('Helvetica-Bold', 12)
		canvas.setFillColorRGB(0,0,1)

		canvas.drawString(220, 670, "COMPROVANTE DE PAGAMENTO")

		canvas.drawString(50, 600, "Prezado %s," % (name))

		canvas.drawString(400, 600, "%s" % (createdAt))

		canvas.drawString(50, 550, "Constatamos o pagamento referente a anuidade do ano de %s, " % (createdAt))

		canvas.drawString(50, 525, "na qualidade de associado como %s." % (type))

		canvas.drawString(50, 475, "Obrigado por inscrever-se e tornar-se associado da Associação Brasileira de ")

		canvas.drawString(50, 450, "Telemedicina e Telessaúde (ABTms).")

		canvas.drawString(50, 400, "Sinceramente,")

		canvas.drawString(50, 375, "Associação Brasileira de Telemedicina e Telessaúde")

		canvas.showPage()
		canvas.save()

		return filename
