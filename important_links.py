# find bold links or links with bold content 
# using BeautifulSoup
		
def isImportant(link):
    '''an important link contains a bold tag, or is contained within a bold tag'''
    return link.find('b') or link.find_parent('b')

def bold_links(page):
    soup = BeautifulSoup(page)
    links = soup('a')
    return set([link.get('href') for link in links if isImportant(link)])