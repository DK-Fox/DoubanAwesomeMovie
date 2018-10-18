#!/usr/bin/env python3
import sys
import csv
from multiprocessing import Process
import queue
tbl=((0,0.03,0),(1500,0.1,105),(4500,0.2,555),(9000,0.25,1005),(35000,0.3,2755),(55000,0.35,5505),(80000,0.45,13505))

class UserData():
	def __init__(self,Userfile):
		self._data=[]
		with open(Userfile) as f:
			for data in csv.reader(f):
				self._data.append(list(map(int,data)))

	@property
	def data(self):
		return self._data

	def calculate(self,shb):
		for user in self._data:
			if user[1]>shb["JiShuH"]:
				m1=shb["JiShuH"]
			elif user[1]<shb["JiShuL"]:
				m1=shb["JiShuL"]
			else:
				m1=user[1]
			m1*=shb["YangLao"]+shb["YiLiao"]+shb["ShiYe"]+shb["GongJiJin"]
			m2 = user[1]-m1-3500 if user[1]-m1-3500>0 else 0
			for i in tbl[::-1]:
				if m2 > i[0]:
					break
			m2=m2*i[1]-i[2]
			m3=user[1]-m1-m2
			user=user+["%.2f"%m1,"%.2f"%m2,"%.2f"%m3]
			yield user

	def Output(self,Outfile,result):
		with open(Outfile,'w') as f:
			csv.writer(f).writerows(list(result))

class Shb():
	def __init__(self,Shbfile):
		self._shb={}
		with open(Shbfile) as f:
			for line in f:
				key,value=line.split('=')
				self._shb[key.strip()]=float(value.strip())

	@property
	def shb(self):
		return self._shb

def p1(q1,q2,opt):
	q1.put(UserData(opt))
    q2.put(UserData(opt))

def p2(q1,q2,opt):
	s=Shb(opt).shb
	try:
		result=q1.get(timeout=5.0).calculate(s)
	except queue.Empty:
		sys.exit(0)
	q2.put(result)

def p3(q1,q2,opt):
	try:
		q1.get(timeout=5.0).Output(opt,q2.get(timeout=5.0))
	except queue.Empty:
		sys.exit(0)
if __name__=='__main__':
	opt={}
	args=sys.argv[1:]
	opt['-d']=args[args.index('-d')+1]
	opt['-c']=args[args.index('-c')+1]
	opt['-o']=args[args.index('-o')+1]

	q1=queue.Queue()
	q2=queue.Queue()
    q3=queue.Queue()

	s1=Process(target=p1,args=(q1,q3opt['-d']))
	s2=Process(target=p2,args=(q1,q2,opt['-c']))
	s3=Process(target=p3,args=(q3,q2,opt['-o']))

	for s in [s1,s2,s3]:
		s.start()
	for s in [s1,s2,s3]:
		s.join()
