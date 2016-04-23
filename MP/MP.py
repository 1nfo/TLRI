from multiprocessing import Process
import time,sys

class Timer():
    def __init__(self,msg_last="elasped time:",verbose=0):
        self.msg=""
        self.msg_last=msg_last
        self.verbose=verbose
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        if self.verbose:
            self.end = time.time()
            self.interval = self.end - self.start
            print self.msg+self.msg_last,"%.1f"%self.interval
            sys.stdout.flush()

class p_exit:
    def __init__(self,quene):
        self.quene=quene
    def __enter__(self):
        for q in self.quene:
            q.start()
    def __exit__(self,*arg):
        for q in self.quene:
            q.terminate()
        
            
class MP():
    def __init__(self,func,nthread):
        self.func=func
        self.nthread=nthread
        self.args=[]
        self.kargs={}
    def set_args(self,*args,**kargs):
        self.args=args
        self.kargs=kargs
    def set_jobs(self,jobs):
        avg=len(jobs)/self.nthread
        joblist=[]
        for i in range(self.nthread):
            if i+1==self.nthread:joblist.append(jobs[avg*i:])
            else:joblist.append(jobs[avg*i:avg*(i+1)])
        self.joblist=joblist
    def execute(self,verbose=0):
        quene=[]
        for i in range(self.nthread):
            target=self.WrapperGenerator(self.func,self.joblist[i],verbose=verbose,thread_id=i,*self.args,**self.kargs)
            p=Process(target=target)
            quene.append(p)
        with p_exit(quene):
            for q in quene:
                q.join()
    def WrapperGenerator(self,executor,joblist,verbose,*args,**kargs):
        def func():
            thread_id=kargs.pop("thread_id")
            for job in joblist:
                with Timer(verbose=verbose) as t:
                    executor(job,*args,**kargs)
                    t.msg+=("Job: "+str(job)+" executed by %d, "%thread_id)
        return func