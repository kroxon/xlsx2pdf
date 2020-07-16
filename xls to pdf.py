import pandas as pd
import pdfkit

df = pd.read_excel("file.xlsx")
df.to_html("file.html")
pdfkit.from_file("file.html", "file.pdf")