# import pandas package
import pandas as pd

data = {'Name':['Jai','Princi','Gaurav','Anuj'],
        'Age':[27,24,22,32],
        'Adress':['Delhi','Kanpur','Allahabad','Kannauj'],
        'Qualification':['Msc','MA','MCA','Phd']
        }

df = pd.DataFrame(data)

print(df.loc[1:3, ['Name', 'Qualification']])