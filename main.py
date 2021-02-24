#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Ray Tan>
#Group Name: <ILovePython>
#Class: <PN2004K>
#Date: <10/2/2021>
#Version: <1.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd

#import graphics
import matplotlib.pyplot as pit
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):
    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
    #show top 3 countries in Graphic mode
    showGraphic()

#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  
  #intialize variables
  time_list = ["1980-1990"]
  country_list = ["a","b","c","d","e","f","g"]
  country_name =""
  visitor = []
  countries = []
  total_visitor = []
  visitor_dict = {}


print("CHOOSE AN ALPHABET THAT CORRESPONDS TO THE COUNTRY FROM THE SEA REGION:","\n","a-Brunei Darussalam","\n","b-Indonesia","\n","c-Malaysia","\n","d-Philippines","\n","e-Thailand","\n","f-Viet Nam","\n","g-Myanmar","\n")

print("The only time period avaiable is from 1980-1990")

while True:
    
   Country = input("PLEASE SELECT AN ALPHABET THAT CORRESPONDS WITH THE SELECTED COUNTRY")
   country = str(country)

   if not country in country_list:
     print("ERROR! PLEASE ENTER ONLY THE ALPHABETS SPECIFIED ABOVE!!!)
     
   elif country in country_list:
     break

SEA = (df[['Year','Month',' Brunei Darussalam ',' Indonesia ',' Malaysia ',' Philippines ',' Thailand ','Viet Nam ',' Myanmar ']][0:8])
 
  print(SEA)
  #CALCULATE THE TOTAL NUMBER OF PEOPLE IN THE COUNTRY 
  #drop the colume to take out the year and months
  sorted = dfasia.drop(['Year','Month'], axis=1)
  #AND TAKE OUT THE TOP THREE COUNTRY THAT HAVE CAME TO SINGAPORE FROM 1985 TO 1995
  total = sorted.sum() 


 #########################################################################
 #find the coutry that have the highest people
 #print the coutry
  sortvalue = total.sort_values(ascending=False)


  #Sort to top 3
  top3 = print(sortvalue.head(n=3))
  return

  
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def showGraphic():

  activities = ['Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Viet Nam', 'Myanmar', 'Brunei Darussalam']
  slices = [25610369, 10691646, 6129847, 4591720, 3711397, 977880, 665636]
  #colours = ['r', 'g', 'm', 'b', 'y', 'o', 'b']

  pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.2, 0.2, 0.2, 0, 0, 0, 0),
        autopct='%1.2f%%')

  pit.legend()

  pit.show()
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('####################################################')
  print('# Data Analysis App - PYTHON PROJECT               #')
  print('####################################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #Project Title
  print('####################################################')
  print('# Data Analysis App - PROGRAM TERMINATED           #')
  print('####################################################')
  
#########################################################################
#Main Branch: End of Code
#########################################################################