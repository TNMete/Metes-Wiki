import datetime


def aktuelles_datum_und_uhrzeit():
    jetzt = datetime.datetime.now()
    jetzt.strftime("Heute ist der %d.%m.%Y und es ist %H:%M:%S")
    return jetzt


print(aktuelles_datum_und_uhrzeit())
