# import pandas to create dataframe
import pandas as pd
# import pdfkit to convert the file into pdf
import pdfkit

def converting_to_pdf():
    df = pd.read_csv('output.csv', index_col=0)
    df.head()
    f = open('output.html','w')
    a = df.to_html()
    f.write(a)
    f.close()
    pdfkit.from_file('output.html', 'output.pdf')
    
converting_to_pdf()    
