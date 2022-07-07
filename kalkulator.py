import bottle
from bottle import run, route, template, post, request
import model

bottle.TEMPLATE_PATH.insert(0, "C:/Users/Maja/Documents/Programiranje/UVP/projektna/matricni-kalkulator/views")


# Domača stran, kjer uporabnik izbere željeno matrično operacijo
@route("/")
def index():
    return template("domaca_stran")

# Stran, kjer uporabnik izbere velikost matrik s katerimi operira ter, če je potrebno še dodaten parameter (eksponent za potenciranje 
# ali skalar za množenje)
@route("/vnos/<operacija>")
def vnos(operacija):
    if operacija == "sestevanje":
        return template("vnos_sestevanje")
    if operacija == "odstevanje":
        return template("vnos_odstevanje")
    if operacija == "mnozenje_s_skalarjem":
        return template("vnos_mnozenje_s_skalarjem")
    if operacija == "matricno_mnozenje":
        return template("vnos_matricno_mnozenje")
    if operacija == "potenciranje":
        return template("vnos_potenciranje")
    if operacija == "transponiranje":
        return template("vnos_transponiranje")
    if operacija == "sled":
        return template("vnos_sled")
    if operacija == "determinanta":
        return template("vnos_determinanta")


# Stran, kjer uporabnik vnese matriko oz. njene elemente
@post("/vpis_vrednosti/<operacija>")
def vpis_vrednosti(operacija):
    if operacija == "sestevanje":
        st_matrik = 2
        st_vrstic = [int(request.forms.get("y")), int(request.forms.get("y"))]
        st_stolpcev = [int(request.forms.get("x")), int(request.forms.get("x"))]
        parameter = ""
    elif operacija == "odstevanje":
        st_matrik = 2
        st_vrstic = [int(request.forms.get("y")), int(request.forms.get("y"))]
        st_stolpcev = [int(request.forms.get("x")), int(request.forms.get("x"))]
        parameter = ""
    elif operacija == "mnozenje_s_skalarjem":
        st_matrik = 1
        st_vrstic = [int(request.forms.get("y"))]
        st_stolpcev = [int(request.forms.get("x"))]
        parameter = request.forms.get("n")
    elif operacija == "matricno_mnozenje":
        st_matrik = 2
        st_vrstic = [int(request.forms.get("y")), int(request.forms.get("x1"))]
        st_stolpcev = [int(request.forms.get("x1")), int(request.forms.get("x2"))]
        parameter = ""
    elif operacija == "potenciranje":
        st_matrik = 1
        st_vrstic = [int(request.forms.get("y"))]
        st_stolpcev = [int(request.forms.get("y"))]
        parameter = request.forms.get("p")
    elif operacija == "transponiranje":
        st_matrik = 1
        st_vrstic = [int(request.forms.get("y"))]
        st_stolpcev = [int(request.forms.get("x"))]
        parameter = ""
    elif operacija == "sled":
        st_matrik = 1
        st_vrstic = [int(request.forms.get("y"))]
        st_stolpcev = [int(request.forms.get("y"))]
        parameter = ""
    elif operacija == "determinanta":
        st_matrik = 1
        st_vrstic = [int(request.forms.get("y"))]
        st_stolpcev = [int(request.forms.get("y"))]
        parameter = ""
    data = {"st_matrik": st_matrik,
            "operacija": operacija,
            "st_vrstic": st_vrstic,
            "st_stolpcev": st_stolpcev,
            "parameter": parameter
            }
    return template("vpis_vrednosti", data)


# Stran, kjer se uporabniku izpiše rezultat
@post("/izracunaj")
def izracunaj():
    operacija = request.forms.get("operacija")
    st_matrik = int(request.forms.get("st_matrik"))
    st_stolpcev = request.forms.get("st_stolpcev")[1:-1].split(", ")
    st_vrstic = request.forms.get("st_vrstic")[1:-1].split(", ")
    parameter = request.forms.get("parameter")
    
    seznam_matrik = []
    for i in range(st_matrik):
        matrika = []
        for y in range(int(st_vrstic[i])):
            vrstica = []
            for x in range(int(st_stolpcev[i])):
                ime = f"polje:{i}-{y}-{x}" 
                vrstica.append(float(request.forms.get(ime)))
            matrika.append(vrstica)
        seznam_matrik.append(matrika)

    if operacija == "sestevanje":
        rezultat = model.vsota(seznam_matrik[0], seznam_matrik[1])
    elif operacija == "odstevanje":
        rezultat = model.razlika(seznam_matrik[0], seznam_matrik[1])
    elif operacija == "mnozenje_s_skalarjem":
        rezultat = model.mnozi_s_skalarjem(seznam_matrik[0], float(parameter))
    elif operacija == "matricno_mnozenje":
        rezultat = model.zmnozek(seznam_matrik[0], seznam_matrik[1])
    elif operacija == "potenciranje":
        rezultat = model.potenca(seznam_matrik[0], float(parameter))
    elif operacija == "transponiranje":
        rezultat = model.transponiraj(seznam_matrik[0])
    elif operacija == "sled":
        rezultat = model.sled(seznam_matrik[0])
    elif operacija == "determinanta":
        rezultat = model.determinanta(seznam_matrik[0]) 

    data = {"seznam_matrik": seznam_matrik,
            "operacija": operacija,
            "rezultat": rezultat}
    return template("prikazi_rezultat", data)


bottle.run(reloader=True, debug=True)