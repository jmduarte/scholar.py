
import os
import time
import random

def execme(command,dryrun=False):    
    '''Wrapper for executing commands.
    '''
    if dryrun:
        print command
    else:
        print " * Executing: %s..."%command
        os.system(command)
        print " * Executed!"


        
def getInput(default, prompt = ''):
    '''Like raw_input() but with a default and automatic strip().
    '''

    answer = raw_input(prompt)
    if answer:
        return answer.strip()

    return default.strip()


if __name__ == "__main__":
    dryrun = False

    url = getInput('https://scholar.google.com/scholar?q=allintitle%3A%28%22oppositional+defiant+disorder%22+OR+%22ODD%22+OR+%22ADHD%22+OR+%22attention+deficit+hyperactivity+disorder%22+OR+%22CD%22+OR+%22conduct+disorder%22%29%28%22borderline+personality+disorder%22+OR+%22BPD%22%29&hl=en&as_sdt=0%2C5&as_ylo=1994&as_yhi=2016', '\nWhat is the url you want?: ')

    
    iref = int(getInput('0', '\nStart from?: '))

    url += '&num=20&start=%i'%iref
    
    #execme('python scholar.py  --override "%s" --txt-globals > globals.txt'%url,dryrun)
    
    execme('python scholar.py  --override "%s" --csv-header > blah.csv'%url,dryrun)
    while True:
        url = url.replace('start=%i'%iref,'start=%i'%(iref+20))
        iref += 20
        time.sleep(3+random.uniform(0,3))
        execme('python scholar.py  --override "%s" --csv > tmp.csv'%url,dryrun)
        if os.stat("tmp.csv").st_size == 0:
            break
        else:
            execme('cat tmp.csv >> blah.csv',dryrun)
        
    execme('rm tmp.csv',dryrun)
        
    



