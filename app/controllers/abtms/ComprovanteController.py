
from app.models.abtms.Payment import Payment
from app.models.abtms.ComprovantePF import ComprovantePF
from app import app

from flask import send_from_directory

@app.route("/abtms/comprovantes/<charge_id>/")
def get_comprovante(charge_id):
    comprovante = ComprovantePF().getComprovanteByCharge(charge_id)

    return send_from_directory(app.static_folder + "/comprovantes/", comprovante["path"])
