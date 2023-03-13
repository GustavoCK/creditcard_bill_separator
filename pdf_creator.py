from fpdf import FPDF
from data_processing import class_list, buyers
from os import getcwd,path,mkdir

def draw_line():
    pdf.set_line_width(1)
    pdf.set_draw_color(r=0)
    pdf.line(x1=0, y1=(pdf.y + 1), x2=210, y2=(pdf.y + 1))
    pdf.cell(txt=' ', new_x='LMARGIN', new_y="NEXT")


def sum_total_price(buyer):
    total = 0
    for y in class_list:
        if y.buyer == buyer:
            total += float(y.bill)

    return round(total, 2)


for name in buyers:

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=18)
    pdf.set_fill_color(245)

    color = True

    for element_object in class_list:
        if name == element_object.buyer:
            color = not color
            pdf.cell(w=55, fill=color, txt=element_object.date, align='L')
            pdf.cell(w=100, fill=color, txt=element_object.store, new_y="LAST", align='L')
            pdf.cell(w=25, txt=element_object.bill.replace('.', ','), fill=color,
                     new_x='LMARGIN', new_y="NEXT", align='R')

    draw_line()
    pdf.cell(w=155, fill=color, txt=name, align='L')
    pdf.cell(w=25, txt=str(sum_total_price(name)).replace('.', ','), fill=color,
             new_x='LMARGIN', new_y="NEXT", align='R')

    directory = getcwd() + '/PDF_files'
    if not path.exists(directory):
        mkdir(directory)
    pdf.output(getcwd() + '/PDF_files/' + name + '_fatura.pdf')
