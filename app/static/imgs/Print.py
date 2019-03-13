import os
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import date
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from flask import url_for 

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

		doc = SimpleDocTemplate(os.path.join(UPLOAD_FOLDER, filename), pagesize=letter,
		                rightMargin=72,leftMargin=72,
		                topMargin=72,bottomMargin=18)

		Story=[]

		logo = url_for("static", filename="imgs/background.png")
		full_name = name
		createdAt = createdAt
		type = "Pessoa Física"

		im = Image(logo, 8*inch, 9*inch)
		Story.append(im)

		styles=getSampleStyleSheet()
		styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
		ptext = '<font size=12>Comprovante gerado em %s.</font>' % (createdAt)
		Story.append(Paragraph(ptext, styles["Normal"]))

		Story.append(Spacer(1, 12))
		ptext = '<font size=12>Querido %s,</font>' % full_name
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))

		ptext = '<font size=12>Constatamos o pagamento referente a anuidade do ano de %s na qualidade de associado como %s.</font>' % (createdAt, type)
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))

		ptext = '<font size=12>Obrigado por inscrever-se e tornar-se associado da Associação Brasileira de Telemedicina e Telessaúde (ABTms).</font>'
		Story.append(Paragraph(ptext, styles["Justify"]))
		Story.append(Spacer(1, 12))
		ptext = '<font size=12>Sinceramente,</font>'
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 48))
		ptext = '<font size=12>Associação Brasileira de Telemedicina e Telessaúde</font>'
		Story.append(Paragraph(ptext, styles["Normal"]))
		Story.append(Spacer(1, 12))
		doc.build(Story)

		return "/comprovantes/" + filename
