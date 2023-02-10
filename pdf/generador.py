import pandas as pd
import pdfkit
import jinja2

#DataFrame from Excel (it should be connected to the DB) and assign row 0 as header
df=pd.read_excel('ejemploRegistro.xlsx', header=0)

#Print DataFrame
print (df)

#Remove rows that don't require PDF generation
df=df[df['PDF']==1]

#Remove rows where ASISTENCIA != 1, the 1 value means they attended the event.
df=df[df['ASISTENCIA']==1]

#Print working DataFrame 
print(df)