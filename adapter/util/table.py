import camelot


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
        if "alkohol" in table_data[step][2]:
            offset = step - 1
            break

    for key in keys:
        wine = {}

        wine["vino"] = table_data[offset][key]
        wine["Alkohol %"] = table_data[offset + 1][key]
        wine["Ukupna kiselost"] = table_data[offset + 2][key]
        wine["Hlapiva kiselost kao octena g/L"] = table_data[offset + 3][key]
        wine["Gustoca g/cm3"] = table_data[offset + 4][key]
        wine["pH"] = table_data[offset + 5][key]
        wine["Reducirajuci secer g/L"] = table_data[offset + 6][key]
        wine["Ekstrakt mg/mL"] = table_data[offset + 7][key]
        wine["Jabucna kiselina g/L"] = table_data[offset + 8][key]
        wine["Mlijecna kiselina g/L"] = table_data[offset + 9][key]
        wine["Sukcinska kselina g/L"] = table_data[offset + 10][key]
        wine["Antocijalni mg/L"] = table_data[offset + 11][key]
        wine["Metanol mg/L"] = table_data[offset + 12][key]
        wine["SO2 slobodni mg/L"] = table_data[offset + 13][key]
        wine["Polifenoli mg/L"] = table_data[offset + 14][key]
        wine["Glukoza g/L"] = table_data[offset + 15][key]
        wine["Fruktoza g/L"] = table_data[offset + 16][key]

        wines.append(wine)

    return wines


def get_date(table_data):
    for key in list(table_data.keys()):
        for value in list(table_data[key].values()):
            if "Date" in value:
                return value.split(" : ")[1].strip()
    return ""
