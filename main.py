from db import connect_db
from extract import extract_prest_sin_pa
from transform import export_excel, enviar_correo

def main():

  conn = connect_db()
  cursor = conn.cursor()
  data_prest = extract_prest_sin_pa(cursor)
  archivo = export_excel(data_prest)
  enviar_correo(archivo)

if __name__ == "__main__":
  main()