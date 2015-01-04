from github import Github
from datetime import datetime,timedelta
from urllib.request import urlretrieve
import uuid


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
        d1 = datetime.today() - timedelta(days=1)
        d2 = datetime.today()
        return repo.get_commits(since=d1, until=d2)

def downloadCommitFiles(commit):
        #TODO: handle this in different module
        commitFiles = commit.files
        for i in range(0, len(commitFiles)):
                print("Downloading " + commitFiles[i].raw_url)
                filename = 'downloads/' + str(uuid.uuid4()) + ".txt"
                urlretrieve(commitFiles[i].raw_url, filename, reporthook)

def search():
        repos = getRecentRepos("tetris")
        commits = getRecentCommits(repos[0]) 
        for commit in commits:
                downloadCommitFiles(commit)



if __name__ == "__main__":        
        ghub = Github()
        search()


#TODO: limit on number of commits downloadable
#TODO: limit on file size of commits willing to download
#TODO: target specific file types
#TODO: use code search if rate is up, otherwise download files for manual search
#TODO: make sure most recent commits are download
#TODO: move downloader into separate module
#TODO: create logging
#TODO: think of program flow. run search in infinite loop, pull from a list of keywords
        #provided as main input

