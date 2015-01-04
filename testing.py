from github import Github
from datetime import datetime,timedelta
import urllib.request

ghub = Github()
repos = ghub.search_repositories("tetris", "updated", "desc")
d1 = datetime.today() - timedelta(days=1)
d2 = datetime.now()
commits = repos[0].get_commits(since=d1, until=d2)
c = commits[0]
commitDate = c.commit.author.date
commitFiles = c.files
for i in range (0,len(commitFiles)):
        wp = urllib.request.urlopen(commitFiles[i].raw_url)
        outFile = open('12345.txt', 'wb')
        outFile.write(wp.read())
        outFile.close()
	

        
#d = x[0].description
#dl = x[0].downloads_url
#n = x[0].full_name
#gl = x[0].git_url
#_id = x[0].id
#owner = x[0].owner #returns a NamedUser object
#updt = x[0].updated_at
#url = x[0].url


#c = x[0].get_commits()
#c[0] #returns a Commit object

#this rate limiting stuff is different for search
#the lib doesn't seem to support seeing your search rate limit
#might consider adding it
#https://developer.github.com/v3/rate_limit/
#rl = g.get_rate_limit() #returns a RateLimit object
#r = rl.rate #returns a Rate object
#r.remaining #remaining calls
#r.reset #date time of reset? 
#r.limit #limit of calls


