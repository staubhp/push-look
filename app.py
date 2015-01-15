from github import Github
from datetime import datetime,timedelta
from urllib.request import urlretrieve
import uuid
import sys


def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        print(s)
        if readsofar >= totalsize: # near the end
            print("\n")
    else: # total size is unknown
        print("read %d\n" % (readsofar,))

def getRecentRepos(searchTerm):
        return ghub.search_repositories(searchTerm, "updated", "desc")

def getRecentCommits(repo):
        d1 = datetime.today() - timedelta(days=20)
        d2 = datetime.today()
        return repo.get_commits(since=d1, until=d2)

def downloadCommitFiles(commit):
        #TODO: handle this in different module
        commitFiles = commit.files
        for i in range(0, len(commitFiles)):
                print("Downloading " + commitFiles[i].raw_url)
                filename = 'downloads/' + str(uuid.uuid4()) + ".txt"
                urlretrieve(commitFiles[i].raw_url, filename, reporthook)
                if (i>1):#TODO: parameteriz
                        break

def search(searchTerm):
        print("Searching for term '" + searchTerm + "'")
        repos = getRecentRepos(searchTerm)
        print("Getting commits from repo named '" + repos[0].full_name + "'")
        commits = getRecentCommits(repos[0]) 
        print("Downloading commits")
        i = 0
        for commit in commits:
                downloadCommitFiles(commit)
                i += 1
                if(i>1): #TODO: parameterize
                        break
def getRateResetTime():
        resetTime = ghub.rate_limiting_resettime
        print ("Rate Reset Time " + str(resetTime))
        return resetTime

def getRateLimit():
        print("Checking rate limit...")
        rateLimit = ghub.rate_limiting;
        reqRemaining = rateLimit[0]
        reqLimit = rateLimit[1]
        print("Requests Remaining: " + str(reqRemaining))
        print("Request Limit: " + str(reqLimit))
        return rateLimit

def main(args):
        rateLimit = getRateLimit()
        for arg in sys.argv:
                if (arg == "app.py"):
                        continue
                if (rateLimit[0] <= 0):
                        #out of requests. wait until rate reset time
                        foo = "foo"
                search(arg)
                rateLimit = getRateLimit()
                rateResetTime = getRateResetTime()

if __name__ == "__main__":        
        ghub = Github()
        #TODO: take search terms and repo freshness as args
        if (len(sys.argv) > 1):
                main(sys.argv)
        else:
                print("Provide search terms as arguments")


#TODO: limit on file size of commits willing to download
#TODO: target specific file types
#TODO: use code search if rate is up, otherwise download files for manual search
#TODO: make sure most recent commits are download
#TODO: create logging
#TODO: think of program flow. run search in infinite loop, pull from a list of keywords
        #provided as main input

