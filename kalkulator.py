import bottle
from bottle import run, route, template, post, request
import model

bottle.TEMPLATE_PATH.insert(0, "C:/Users/Maja/Documents/Programiranje/UVP/projektna/matricni-kalkulator/views")


# Domača stran, kjer uporabnik izbere željeno matrično operacijo
@route("/")
def index():
    return template("seznam_operacij")

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


bottle.run(reloader=True, debug=True)