import urllib, pickle

page = urllib.urlopen("http://www.python.org")

page_contents = page.read()

link_list = []
	
def get_first_link(page_contents):
	link_tag = page_contents.find("<a href=")
	start_quote = page_contents.find('"', link_tag)
	end_quote = page_contents.find('"', start_quote + 1)
	url = page_contents[start_quote + 1:end_quote]
	link_list.append(url)
	pickle.dump(link_list, open('links', 'wb'))
	get_next_link(page_contents, end_quote)
	    
def get_next_link(page_contents, end_quote):
	link_tag = page_contents.find("<a href=", end_quote)
	while not link_tag == -1:
		link_tag = page_contents.find("<a href=", end_quote)
		start_quote = page_contents.find('"', link_tag)
		end_quote = page_contents.find('"', start_quote + 1)
		if link_tag == -1:
			page_contents = urllib.urlopen(link_list)
			get_first_link(page_contents)
		else:	
			url = page_contents[start_quote + 1:end_quote]
			link_list.append(url)
			pickle.dump(link_list, open('links', 'wb'))
			# test purposes
			print url
	    
get_first_link(page_contents) 
