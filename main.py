import src.apis_functions as af

#Importo el csv:
df = af.load_csv()

#Elimino columas:
df.drop(["Startups", "Venture Capital", "Travel Connectivity", "Business Freedom", "Tolerance"], axis=1, inplace=True)

#Cambio nombre de 3 columnas por "City", "Country" y "Continent":
for_city = {'UA_Name': 'City'}
df.rename(columns=for_city,inplace=True)
for_country= {'UA_Country': 'Country'}
df.rename(columns=for_country,inplace=True)
for_continent= {'UA_Continent': 'Continent'}
df.rename(columns=for_continent,inplace=True)


#Creo una columna nueva con la media de todas las columnas:
df["Average Score"]=df.mean(axis=1)

#Amplío la información de mi df con la api que me da información sobre la calidad del aire:
df['Air Quality']=df.City.apply(af.getquality)
df['Air Quality Level']=df["Air Quality"].apply(af.quality_level)
print(df)

#guardo en un csv :
df.to_csv("data/final.csv")

