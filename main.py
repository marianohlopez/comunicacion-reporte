from db import connect_db
from extract import extract_prest_sin_pa, extract_sin_pa_public
from transform import export_excel, enviar_correo

def main():

  conn = connect_db()
  cursor = conn.cursor()
  data_prest = extract_prest_sin_pa(cursor)
  data_prest_public = extract_sin_pa_public(cursor)
  archivo = export_excel(data_prest, data_prest_public)
  enviar_correo(archivo)

if __name__ == "__main__":
  main()