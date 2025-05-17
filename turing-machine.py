# global variables reset and initialised every time run_program is run
tape = []
head = 0
program = ""
points = {}

bit_gap = 2 # the number of bits between each one-space-wide gap
print_each_state = False # whether to print each state as program runs

# prints the current tape contents as well as the head's position and next instructions.
def print_state(head,instruction):
  for i in tape:
    b = 0
    if i: b = 1
    print(b,end="")
  print("\n"+head*' '+"^ " + instruction+"\n")


# a function to run each instruction
def run_instruction(i:int):
  global tape
  global head
  c = program[i]
  new_i = i+1
  if c == '0': tape[head] = False
  elif c == '1': tape[head] = True
  elif c == '<': head-=1
  elif c == '>': head+=1
  elif c == ';': return 0,True,False
  elif c == '?':
    ni,halt,keep_new_i = run_instruction(i+1+tape[head])
    if halt: return 0,True,False
    if keep_new_i: new_i = ni
    else: new_i = i+3
  elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    return points[c.lower()],False,True
  return new_i,False,False

# initialises data from inputs
def run_program(stape:str,prog:str):
  global program
  global tape
  global head
  global points
  # removes spaces and newlines from program 
  prog = prog.replace("\n","")
  prog = prog.replace(" ","")
  program = prog
  
  # does a first pass of the program to find all jump-to point definitions
  points = {}
  for i in range(len(program)):
    if program[i] in "abcdefghijklmnopqrstuvwxyz":
      points[program[i]] = i
  
  # converts the string tape into an array of booleans
  tape = []
  for i in stape:
    if i == '0':
      tape.append(False)
    elif i == '1':
      tape.append(True)

  i = 0
  head = 0
  # the main loop for running the program
  while i < len(program) and head<len(tape):
    if print_each_state: print_state(head,program[i:])
    i,halt,_ = run_instruction(i)
    if halt: break
  
  # printing the output tape as a string of one's and zero's with a gap
  counter = 1
  for i in tape:
    b = 0
    if i: b = 1
    print(b,end="")
    if counter == bit_gap:
      print(" ",end="")
      counter = 0
    counter+=1
  print()

# a small set of example programs
AND_program = "Ay>1;x>?;Ya?;X" # and gate
OR_program = "Ay>>1;z>1;x>?;Za?XY" # or gate
XOR_program = "Ab>?Z;c>?;Zz>1;a?CB" # xor gate
HA_program = "?XAa>?YBb>1;x>?;Yy>>1;" # half adder
COPY_4_program = "?ABa>>>>0<<<?CDb>>>>1<<<?CDc>>>>0<<<?EFd>>>>1<<<?EFe>>>>0<<<?GHf>>>>1<<<?GHg>>>>0<<<;h>>>>1<<<;" # copy 4 bits

bit_gap = 2

# run each program with test tapes
print("AND gate:")
run_program("000",AND_program)
run_program("010",AND_program)
run_program("100",AND_program)
run_program("110",AND_program)

print("\nOR gate:")
run_program("000",OR_program)
run_program("010",OR_program)
run_program("100",OR_program)
run_program("110",OR_program)

print("\nXOR gate:")
run_program("000",XOR_program)
run_program("010",XOR_program)
run_program("100",XOR_program)
run_program("110",XOR_program)

print("\nHalf Adder:")
run_program("00 00",HA_program)
run_program("01 00",HA_program)
run_program("10 00",HA_program)
run_program("11 00",HA_program)

bit_gap = 4

print("\nCopy 4 Bits:")
run_program("0101 0000",COPY_4_program)
run_program("1010 0000",COPY_4_program)
run_program("1100 0000",COPY_4_program)
run_program("1011 0000",COPY_4_program)
