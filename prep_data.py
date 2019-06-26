import pandas as pd

###
# Makes an HTML table from a CSV file
# Suitable for Datatable
# need to manually add it to HTML table
# until pandas 0.23 is out and can do it directly
def make_html_from_csv(fileName,columns):
	f = open(fileName,"r")
	data = pd.read_table(f)
	data.columns = columns
	html_filename = fileName[0:-3] + "html"
	data.to_html(html_filename, classes = "display")
	#data.to_html(html_filename, classes = "display",table_id="search_table")


if __name__ == "__main__":

	make_html_from_csv("welland_use.tab",["date","doi","Pub_code","User_code","country","city","lat","long"])


