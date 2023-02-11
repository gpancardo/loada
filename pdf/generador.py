import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

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

#Get names from the DataFrame to an array
nameList=df['NOMBRE'].values
#Get event name to an array
eventList=df['ACTIVIDAD'].values

print(nameList)

#We will now create a function to generate a PDF file with the name of the attendee and an image file with the organization's or event's logo
def generate(nom, event, img):

    #Stablish filename (name+extension)
    filename=(nom+".pdf")

    #Create a PDF file with the previous filename
    c= canvas.Canvas(filename)

    #Create message string
    message=("Se entrega constancia de participación a "+nom+" en "+event)

    #Insert text to the file. We can add editable string content later
    c.drawString(80,800,message)

    #Save finished file
    c.save()

#Iterate throught the name list to create a file per person
for i in range (len(nameList)):
    #Assign nom value to the element on the row we are using
    nom=nameList[i]
    #img=ImageReader('logo.jpg')
    img=0
    #Event name from the row we are working with
    event=eventList[i]
    generate(nom,event,img)