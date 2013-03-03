import urllib, pickle

link_list = []

def get_first_link(page):
	page = urllib.urlopen(page)
	global page_contents
	page_contents = page.read()
	#page.close()
	link_tag = page_contents.find("<a href=")
	start_quote = page_contents.find('"', link_tag)
	#global end_quote
	end_quote = page_contents.find('"', start_quote + 1)
	url = page_contents[start_quote + 1:end_quote]
	link_list.append(url)
	#print link_list
	get_next_link("http://www.python.org", end_quote)

"""maybe pass page_contents as a perameter to get_next_link instead of making page_contents a global variable"""
def get_next_link(page, end_quote):
	link_tag = page_contents.find("<a href=", end_quote)
	while not link_tag == -1:
		start_quote = page_contents.find('"', link_tag)
		end_qoute = page_contents.find('"', start_quote)
		url = page_contents[start_quote + 1:end_quote]
		link_list.append(url)
		pickle.dump(link_list, open('links', 'wb'))
		#print link_list
		print url
		get_next_link("http://www.python.org", end_quote)
	

get_first_link("http://www.python.org") 
