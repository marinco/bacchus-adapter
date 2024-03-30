import camelot

wine_properties = [
    "vino",
    "Alkohol %",
    "pH",
    "Ukupna kiselost",
    "Hlapiva kiselost kao octena g/L",
    "Reducirajuci secer g/L",
    "Gustoca g/cm3",
    "Ekstrakt mg/mL",
    "Jabucna kiselina g/L",
    "Mlijecna kiselina g/L",
    "Vinska kiselina g/L",
    "Limunska kiselina mg/L",
    "Sukcinska kiselina g/L",
    "Pepeo g/L",
    "Glukoza g/L",
    "Fruktoza g/L",
    "Glicerol g/L",
    "Antocijalni mg/L",
    "Polifenoli mg/L",
    "Metanol mg/L",
    "Glukonska kiselina mg/L",
]


def get_table_data(input_pdf):
    tables = camelot.read_pdf(input_pdf, flavor='stream', pages='1')

    # Assuming there's only one table on the page, you can access it using index 0
    if tables:
        table_data = tables[0].df.to_dict()
        return table_data
    else:
        raise Exception("No tables found in the PDF.")


def get_dict_from_table(table_data):
    wines = []
    keys = list(table_data[0].keys())[5:]

    # Alcohol sometimes starts from index 1, sometimes from 2 :(
    offset = 0
    for step in (list(table_data.keys())):
        if "Alkohol" in table_data[step][2]:
            offset = step - 1
            break

    for key in keys:

        # sometimes there is "Spectra folder" instead of wine, skip
        if "Spectra" in table_data[0][key]:
            continue

        wine = {}

        # iterator for wine properties
        i = 0
        # iterator for table data
        j = 0

        while True:
            if i >= len(wine_properties) or j >= len(table_data):
                break
            if "\n" in table_data[offset + j][key]:
                parts = table_data[offset + j][key].split("\n")
                k = 0
                while k < len(parts) and i < len(wine_properties):
                    wine[wine_properties[i]] = parts[k]
                    k = k + 1
                    i = i + 1
                j = j + 1
            else:
                wine[wine_properties[i]] = table_data[offset + j][key]
                i = i + 1
                j = j + 1

        wines.append(wine)

    return wines


def get_date(table_data):
    for key in list(table_data.keys()):
        for value in list(table_data[key].values()):
            if "Date" in value:
                return value.split(" : ")[1].strip()
    return ""
