from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista en memoria para guardar registros
registros = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        tipo = request.form["tipo"]  # Ingreso o Egreso
        concepto = request.form["concepto"]
        monto = float(request.form["monto"])

        registros.append({
            "tipo": tipo,
            "concepto": concepto,
            "monto": monto
        })
        return redirect(url_for("home"))

    # Cálculo rápido del balance
    ingresos = sum(r["monto"] for r in registros if r["tipo"] == "Ingreso")
    egresos = sum(r["monto"] for r in registros if r["tipo"] == "Egreso")
    balance = ingresos - egresos

    return render_template("index.html", registros=registros, balance=balance)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
