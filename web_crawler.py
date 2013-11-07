# method to extract url's from text like a web page
# python way

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1: end_quote]
	return url, end_quote
	
# def print_all_links(page):
	# while True:
		# url, endpos = get_next_target(page)
		# if url:
			# print url
			# page = page[endpos:}
		# else:
			# break
			
def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links
	
def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)
	
def crawl_web(seed_page, max_pages):
	to_crawl = [seed_page]
	crawled = []
	#changed from list to Dictionary
	index = {}
	while to_crawl:
		if len(crawled) == max_pages:
			break
		#Depth-First Search - not ideal for production web crawler
		page = to_crawl.pop()
		if page not in crawled:
			#update to_crawl
			content = get_page(page)
			add_page_to_index(index,page,content)
			union(tocrawl, get_all_links(content))
			#and update crawled	
			crawled.append(page)
	return index
			
# Creating Index
# Changed to use Dictionary instead of List
def add_to_index(index, keyword, url):
	if keyword in index:
		index[keyword].append(url)
	else:
		# not found, add new keyword to index
		index[keyword] = [url]

# Updated to use Dictionary for index instead of list
def lookup(index, keyword):
	if keyword in index:
		return index[keyword]
	return None
	
def add_page_to_index(index,url,content):
	keywords = content.split()
	for word in keywords:
		add_to_index(index,word,url)
		
		
# simulate a user click on link
def record_user_click(index,keyword,url):
    url_list = lookup(index, keyword)
    for entry in url_list:
        if entry[0] == url:
            entry[1] += 1
			
			
			
# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    total = 0
    for e in keyword:
        total += ord(e)
    return total % buckets
	
	
def make_hashtable(nbuckets):
	table = []
	for e in range(0,nbuckets):
		table.append([])
	return table
	
def hashtable_get_bucket(htable,keyword):
    bucket_number = hash_string(keyword,len(htable))
    return htable[bucket_number]
	
def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable, key).append([key,value])
	
def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_update(htable,key,value):
    # Your code here
    if hashtable_lookup(htable, key):
        # if it returns a value then update that value
        bucket = hashtable_get_bucket(htable,key)
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
				break
    else:
        hashtable_add(htable,key,value)
    return htable	
		

