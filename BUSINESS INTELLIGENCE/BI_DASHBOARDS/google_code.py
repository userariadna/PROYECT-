
#This code allows to collect the twitter data in real time 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from df2gspread import df2gspread as d2g


#define scope variable as well as the service credentrials to connect with the spreadsheet 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('myfile.json', scopes=scope)
gc = gspread.authorize(credentials)

spreadhsheet_key = '1rU2PaU_6cD6Dankr3mtzBr2J3Tnj3keGyYMl8h2tj9A'


#name of the database 
wks_name= "databases"

#upload the dataframe joined to the respective key 
d2g.upload(last_df, spreadhsheet_key, wks_name, credentials=credentials, row_names=True)

#if the data is gathered print Data upload sucess 

print("Data upload success")