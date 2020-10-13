import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

class PandasClass:

    """
    __init__ -> constructor
    function readAllFilePandas(self) -> lire tout le fichier csv
    function readFilePandas(self,valueHead) valueHead:4 -> lire le ficher csv et permet de choisir le nombe de ligne (1ière) à display
    function readFileFunctionTypePandas(self,typeValue,headValue=None) typeValue:"Pariod",headValue:2 -> lire le fichier csv en précisant le columns et le nombre de ligne (1ière ) à display
    function readFileFunctionOnlyLinePandas(self,typeLineValue=None,lineValue=None): typeLineValue:"Period", lineValue:2 -> cette function affiche en function de la columns et la line une value precise
    function readFileFunctionRowsSelectedPandas(self,valueRows) : valueRows=2 -> lire en function de valueRows toute la line d'un fichier
    function readFileColmunsPandas(self) -> affiche toutes les columns du fichier
    function readFileFunctionsRowsSearchPandas(self,typeValueIterr) : typeValueIterr:"Period" -> faire une boucle sur une columns precise du fichier
    function readFileFunctionsRowsDisplayTypeEqual(self,typeValuePrecis,elementValue) : typeValuePrecis:"UNITS", elementValue:"Dollars" ell affiche toute les elements qui ont un UNITS comme Dollars
    function readFileDescribe(self) -> elle donne une description generale (min,max,count...) sur le fichier

    """
    file_csv = pd.read_csv("electronic-card/ect-Aug-2020-csv.csv")
    #constructore
    def __init__(self):
        pass

    # read all file lines
    def readAllFilePandas(self):
        pokes = PandasClass.file_csv
        return pokes

    #read only valueHead lines
    def readFilePandasLimit(self,valueHead):
        poke = PandasClass.file_csv
        return poke.head(valueHead)

    def readFileFunctionTypePandas(self,typeValue,headValue=None):
        pok = PandasClass.file_csv
        return pok[typeValue].head(headValue)

    def readFileFunctionOnlyLinePandas(self,typeLineValue=None,lineValue=None):
        readP = PandasClass.file_csv
        return readP[typeLineValue][lineValue]

    def readFileFunctionRowsSelectedPandas(self,valueRows):
        rowsPandas = PandasClass.file_csv
        return rowsPandas.iloc[valueRows]

    def readFileFunctionsRowsSearchPandas(self,typeValueIterr):
        rowsAll = PandasClass.file_csv
        for indexRow,row in rowsAll.iterrows():
            print(indexRow,row[typeValueIterr]) #

    def readFileFunctionsRowsDisplayTypeEqual(self,typeValuePrecis,elementValue):
        filePans = PandasClass.file_csv
        return filePans.loc[filePans[typeValuePrecis] == elementValue]

    def readFileDescribe(self):
        des = PandasClass.file_csv
        return des.describe()

    #read head columns
    def readFileColmunsPandas(self):
        col = pd.read_csv('electronic-card/ect-Aug-2020-csv.csv')
        return col.columns

    def groupByPandas(self):
        pass

    def filteringPandas(self):
        pass

    def filteringByGroupPandas(self):
        pass

    def fileMatplotPandas(self):
        pass
    def filePlotLibPandas(self):
        pass
    def readFileSortingPandas(self,value):
        fi = PandasClass.file_csv
        return fi.sort_values("Period", ascending=False)




"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html #doc

https://pandas.pydata.org/pandas-docs/stable/reference/api/ #doc

https://github.com/pandas-dev/pandas

https://www.stats.govt.nz/large-datasets/csv-files-for-download/ # file csv


https://docs.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/implement-api-gateways-with-ocelot

"""
