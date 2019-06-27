import pandas

#put you csv file into the directory
#make sure that the files "html_top.html" and "html_bottom.html" are in the directory as well
#Input the name of your csv file as the argument for the function

def csv_to_web_table_converter(inputcsvname):
    
    #This makes a variable containing the csv data
    inputcsvdata = open(inputcsvname,"r")
    
    #This turns the csv file into an html formatted table
    csvcontenttable = pandas.read_csv(inputcsvdata)
    htmlversion = csvcontenttable.to_html()
    
    #This replaces the opening table tag with a tag containing the correct ID for the Jquery DataTables
    htmlversionidadded = htmlversion.replace(htmlversion[0:36],"<table id='myTable' class='display'>")
    
    #This grabs the top and bottom html code for the final file
    htmltop = open("html_top.html","r")
    htmlbottom = open("html_bottom.html","r")
    
    #This creates a filename for the new file based on the name of the csv file
    htmlfilename = inputcsvname[0:-3] + "html"
    
    #This creates a new file with the new file name and adds the content
    newfile = open(htmlfilename,"w+")
    newfile.write(htmltop.read() + htmlversionidadded + htmlbottom.read())
	
	
if __name__ == '__main__':
    csv_to_web_table_converter("YOUR_CSV_NAME_HERE.csv")