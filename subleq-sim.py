#!/usr/bin/python

import sys
from numpy import int32

# Data structures
mem = {}
lab = {}
reg = {}
pc = 0

def hex2dec(s):
  return unsigned(s,16)
def dec2hex(n):
  return "%X" %n

def file_open(fname):
  f = open(fname, 'r+')
  return f

def init_labels():
  lab['EXIT'] = -1;

def init_reg():
  reg['0'] = 0
  reg['1'] = 0
  reg['2'] = 0
  reg['3'] = 0
  reg['4'] = 0
  reg['5'] = 0
  reg['6'] = 0

def is_opcode(s):
  if s == "sl" or s == "ri":
    return True	
  else:
  	return False

def add_line(l):
  print len(l)
  # Check if first entry is reserved
  if (is_opcode(l[0])):
    if (len(l)) == 3:
    	op = l[0]
    	a = l[1]
    	b = l[2]
    	c = ''
    if (len(l)) == 4:
      op = l[0]
      a = l[1]
      b = l[2]
      c = l[3]
  # Not an opcode -> must be label
  else: 
    label = l[0]
    lab[label] = len(mem)
    if (is_opcode(l[1])):
    	if (len(l)) == 4:
    		op = l[1]
    		a = l[2]
    		b = l[3]
    		c = ''
    	if (len(l)) == 5:
    		op = l[1]
    		a = l[2]
    		b = l[3]
    		c = l[4]

  mem[len(mem)] = (op,a,b,c)

def dump():
  s = ''
  for i in range(len(reg)):
    s = s + 'u' + str(i) + ':' + (hex(reg[str(i)])) + '  '
#print i,':',hex(reg[str(i)])
  print s

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def set_reg(i,v):
  reg[i] = int(v)

def do_subleq():
  global pc
  global mem
  global lab
  global reg

  s = 'pc: ' + str(pc)
#print "pc: ",pc
  (op,a,b,c) = mem[pc]
  s = s + ' ' + str(op) + ' ' + str(a) + ' ' + str(b) + ' ' + str(c)
#print "op,a,b,c: ",op,a,b,c
  print s

	# Register initialization
  if op == "ri": 
    set_reg(a,b)
    pc = pc + 1
  else:		
    # b = b - a
    reg[b] = reg[b] - reg[a]
    if reg[b] <= 0:
      if is_number(c) == True:
        pc = reg[c]
      elif c != '': 
        pc = lab[c]
      else:
        pc = pc + 1
    else:
      pc = pc + 1
  dump()
  if c == 'EXIT':
    pc = -1

  return pc

def start_program():
  while 1:
    do_subleq()
    if pc == -1:
      print 'End of program'
      sys.exit() 


# start program
if (len(sys.argv) <2):
  print 'Usage: subleq-sim.py <filename>'
  sys.exit()

f = file_open(str(sys.argv[1]))
init_reg()
init_labels()

for line in f:
  print 'line:', line
  l = line.strip('\n')
  l = l.split()
  print l
  if len(l) > 0 and l[0] != "#":
    add_line(l)

print mem
print 'Start program'
start_program()

dump(mem,lab)
f.close()
