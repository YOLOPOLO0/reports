from fpdf import FPDF
import requests


def text(x_pos:float,y_pos:float,width:int,height:int,text:str,font_size:int, font_style:str, align='L'):
    pdf.set_font("helvetica",font_style,font_size)
    pdf.set_xy(x_pos, y_pos)
    pdf.multi_cell(width,height,text,align=align)
    return

class CustomPDF(FPDF):
        def footer(self):
            self.set_y(-15)
            self.set_font('helvetica', '', 9)
            
            page = 'Page ' + str(self.page_no()) + ' of {nb}'

            self.set_x(19)
            self.cell(250, 10, "Copyright _ 2022 Corporate Invents Lahore, Pakistan", 0, 0, 'L')
            w = pdf.get_string_width(page) + 6
            self.set_x(-w -15)
            self.cell(20, 10, page, 0, 0)

pdf = CustomPDF("P", "px", "A4")

def certificatePDF(id):
    res = requests.get(f"http://192.168.1.11:5000/Certificates/getPararmeters/{id}")
    data = res.json()
    data = data.get("data")

    

            
    supplier = data.get("supplierName")
    address = """Shahrah-e-Roomi,P.O Walton Road, LAHORE, Lahore +924231234567 packagesmall.com"""
    fileLink = r"C:\Users\DELL\Desktop\Report\j_logo.jpg"
    fileLink2= r"C:\Users\DELL\Desktop\Report\tick.png"
    fileLink3=r"C:\Users\DELL\Desktop\Report\cross.png"


    pdf.alias_nb_pages()
    pdf.set_font("helvetica", size=18)
    pdf.add_page()
    text(19, 25,331,45, "Certificate of Analysis", 26,'B')
    text(19, 65,140,22, "Corrugated Box", 18,'')
    text(19,97,196,21,f"{supplier}",18,'B')
    text(19,120,196,16,f"{address}",14,'')
    pdf.image(fileLink,466,25
            ,109,50)
    pdf.rect(19,223,556,66)
    text(35,233,120,17, "Supplier = ",10,'')
    text(84,220,300,40, "Packages",10,'B')
    text(240,233,144,17,"Raw Material = ",10,'')
    text(310,233,120,17, "Laminates",10,'B')
    text(447,233,82,17,"Products = ",10,'')
    text(499,233,120,17, "Lays",10,'B')
    text(35,261,88,17, "SKU = ",10,'')
    text(66,249,300,40, "AG001DX",10,'B')
    text(240,261,78,17,"IGP = ",10,'')
    text(270,249,300,40, "3520132",10,'B')
    text(19,307,140,20, "Tested by:",12,'')
    text(78,307,170,20, "Abdul Raheem",12,'B')
    text(318,305,80,16, "User Remarks",10,'')
    text(19,332,148,20, "Tested on:",12,'')
    text(78,332,170,20, "08/10/2022",12,'B')
    text(20,357,212,20, "System Generated result =",12,'')
    text(169,357,212,20, "Failed",12,'B')
    text(20,383,243,20, "User Recommended result =",12,'')
    text(174,383,212,20, "Approved",12,'B')
    pdf.rect(322,323,253,81)
    text(334,331.1,231,15, "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.",8,'')
    pdf.rect(19,420,556,363)
    pdf.image(fileLink2,513,471,20.65,15.49)
    text(31,431,64,20, "Attributes",12,'B')
    text(162,431,34,20, "UOM",12,'B')
    text(214,431,91,20, "Specification",12,'B')
    text(323,431,96,20, "Supplier Result",12,'B')
    text(507,431,43,20, "Status",12,'B')

    text(31,469,52,14, "Moisture",12,'')
    text(31,501,113,14, "Internal case length",12,'')
    text(31,533,113,14, "Internal case width",12,'')
    text(31,565,113,14, "Internal case height",12,'')
    text(31,597,60,14, "Thickness",12,'')
    text(31,629,67,14, "Grammage",12,'')
    text(31,661,118,14, "Flat Crush Strength",12,'')
    text(31,693,118,14, "Edge Crush Strength",12,'')
    text(31,725,118,14, "Box Crush Strength",12,'')
    text(31,757,88,14, "Gap B/W Flaps",12,'')

    text(168,468,26,16, "mm",12,'')
    text(168,500,26,16, "mm",12,'')
    text(168,532,26,16, "mm",12,'')
    text(168,564,26,16, "mm",12,'')
    text(168,596,26,16, "mm",12,'')
    text(168,628,26,16, "mm",12,'')
    text(168,660,26,16, "mm",12,'')
    text(168,692,26,16, "mm",12,'')
    text(168,724,26,16, "mm",12,'')
    text(168,756,26,16, "mm",12,'')
    text(221,468,88,16, "10mm - 12mm",12,'')
    text(221,500,88,16, "10mm - 12mm",12,'')
    text(221,532,88,16, "10mm - 12mm",12,'')
    text(221,564,88,16, "10mm - 12mm",12,'')
    text(221,596,88,16, "10mm - 12mm",12,'')
    text(221,628,88,16, "10mm - 12mm",12,'')
    text(221,660,88,16, "10mm - 12mm",12,'')
    text(221,692,88,16, "10mm - 12mm",12,'')
    text(221,724,88,16, "10mm - 12mm",12,'')
    text(221,756,88,16, "10mm - 12mm",12,'')

    text(356,468,42,16, "11mm",12,'')
    text(356,500,42,16, "11mm",12,'')
    text(356,532,42,16, "11mm",12,'')
    text(356,564,42,16, "11mm",12,'')
    text(356,596,42,16, "11mm",12,'')
    text(356,628,42,16, "11mm",12,'')
    text(356,660,42,16, "11mm",12,'')
    text(356,692,42,16, "11mm",12,'')
    text(356,724,42,16, "11mm",12,'')
    text(356,756,42,16, "11mm",12,'')

    pdf.image(fileLink2,513,502,20.65,15.49)
    pdf.image(fileLink2,513,535,20.65,15.49)
    pdf.image(fileLink2,513,566,20.65,15.49)
    pdf.image(fileLink2,513,598.29,20.65,15.49)
    pdf.image(fileLink3,513,629,20.65,15.49) 
    pdf.image(fileLink2,513,663,20.65,15.49)
    pdf.image(fileLink2,513,695,20.65,15.49)
    pdf.image(fileLink2,513,727,20.65,15.49)
    pdf.image(fileLink2,513,759,20.65,15.49)


    pdf.output("simple_demo.pdf")