from fpdf import FPDF
from panchoVilla import *
from Wolkoff import *
from CafeHullu import *


env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


pdf = FPDF('P', 'mm','Letter')

pdf.add_page()

pdf.set_font('Helvetica', "", 16)


pdf.multi_cell(0, 10, kaava1, 0,ln=True)
pdf.multi_cell(0, 10, kaava2, 0,ln=True)
pdf.multi_cell(0, 10, kaava3, 0,ln=True)
pdf.output('pdf_1.pdf')


def lähetäTiedot():
    client.files_upload(
         channels="#lunch-bot",
         title="ruokalistaData",
         file="./pdf_1.pdf",
         initial_comment="Päivän ruokalistat:",
     )
lähetäTiedot()