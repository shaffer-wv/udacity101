

def crawl_web(seed_page):
	tocrawl = [seed_page]
	crawled = []
	index = {}
	graph = {}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			#update tocrawl
			content = get_page(page)
			add_page_to_index(index,page,content)
			outlinks = get_all_links(content)
			graph[page] = outlinks
			union(tocrawl, outlinks)
			#and update crawled	
			crawled.append(page)
	return index, graph
	
	############################
	# computing the page ranks
	def compute_ranks(graph):
    # graph is dictoinary where key is webpage and value is list of links on that page
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
		# go through each page (key) in graph and give it an
		# initial popularity ranking
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
				# go through each webpage(key) in graph
        for page in graph:
            newrank = (1 - d) / npages            
            #go through each webpage(key) in graph
            for node in graph:
							# if page in graph[node] then node(webpage) has a link to page
              if page in graph[node]:
								# add to newrank now based on the popularity of node (the webpage that links to page)
                # ranks[node] is the rank of the page which contains the link
                # len(graph[node]) is the amount of links on that previous page 
                newrank = newrank + d*(ranks[node] / len(graph[node]))            
            newranks[page] = newrank
        ranks = newranks
    return ranks

		
	