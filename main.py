import reportlab
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
#    Year  Month   Predicted    High   Low
    (2019, 10,     3.4,       10.4, 0.0),
    (2019, 11,     3.2,       11.2, 0.0),
    (2019, 12,     3.1,       12.1, 0.0),
    (2020, 1,      3.3,       12.3, 0.0),
    (2020, 2,      3.4,       13.4, 0.0),
    (2020, 3,      3.4,       13.4, 0.0),
    (2020, 4,      3.0,       13.0, 0.0),
    (2020, 5,      2.8,       12.8, 0.0),
    (2020, 6,      2.6,       12.6, 0.0),
    (2020, 7,      2.4,       12.4, 0.0),
    ]

draw = Drawing(200, 150)

format_x = 18
format_y = 6.7

margin_x = 10
margin_y = 10

pred = [row[2]*format_y+margin_y for row in data]
high = [row[3]*format_y+margin_y for row in data]
low = [row[4]*format_y+margin_y for row in data]
times = [200*((row[0] + row[1]/12.0) - 2019 ) -150 for row in data]

draw.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
draw.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
draw.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))

renderPDF.drawToFile(draw, 'test1.pdf', 'sunspots')