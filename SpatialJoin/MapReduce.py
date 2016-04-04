import os, sys
from collections import defaultdict

class MapReduce(object):
    def __init__(self, M=None, R=None):
        self.Mapper=M()
        self.Reducer=R()
        self.M_res={}
        self.R_res=defaultdict(list)
        self.input_t=None
        self.input_i=None
        self.config={"traj_limit":None}

    def set_param(self,name,val):
        self.config[name]=val

    def set_input_traj(self,path):
        self.input_t=path

    def set_input_itsc(self,path):
        self.input_i=path

    def set_output(self,path):
        self.output=path

    def execute(self,verbose=0):
        if verbose:
            print "Mapper Start ..."
            _file_to_mapping_=len(os.listdir(self.input_t))+1
            count=0
        self.Mapper.setup(self)
        if not self.config["traj_limit"]: paths = os.listdir(self.input_t)
        else: paths = os.listdir(self.input_t)[:self.config["traj_limit"]]
        for path in paths:
            if verbose:
                print "\r__mapping__ %d/%d ..." % (count,_file_to_mapping_),
                sys.stdout.flush()
                count+=1
            with open(self.input_t+path,"rb") as ft:
                for i in ft:
                    self.Mapper.map(None,i.strip(),self.M_res)
        if verbose:
                print "\r__mapping__ %d/%d ..." % (count,_file_to_mapping_),
                sys.stdout.flush()
                count+=1
        with open(self.input_i,"rb") as fi:
            for i in fi:
                self.Mapper.map(None,i.strip(),self.M_res)
        self.Mapper.cleanup(self)
        if verbose:
            print "\r__mapping__ %d/%d ..." % (count,_file_to_mapping_)
            print "Mappper Done!\n\nReducer Start ..."
            _vals_to_reducing_=len(self.M_res)
            count=0
        self.Reducer.setup(self)
        for key in self.M_res:
            if verbose:
                print "\r__reducing__ %d/%d ..." % (count,_vals_to_reducing_),
                sys.stdout.flush()
                count+=1
            self.Reducer.reduce(key,self.M_res[key],self.R_res)
        self.Reducer.cleanup(self)
        if verbose:
            print "\r__reducing__ %d/%d ..." % (count,_vals_to_reducing_)
            print "Reducer Done!\n\nWriting to files ..."
            _files_to_write_ = len(self.R_res)
            count=1
        for i in self.R_res:
            with open(self.output+i.split(",")[0],"wb") as f:
                f.write(i+"\n")
                for j in self.R_res[i]:
                    f.write(j+"\n")
            if verbose:
                print "\r__writing__ %d/%d ..." % (count,_files_to_write_),
                sys.stdout.flush()
                count+=1
        print ''


class Mapper(object):
    def setup(self,config):
        pass

    def map(self,key,value,context):
        pass

    def cleanup(self,config):
        pass

class Reducer(object):
    def setup(self,config):
        pass

    def reduce(self,key,values,context):
        pass

    def cleanup(self,config):
        pass
