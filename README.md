# A Turing Machine made in Python
This is a very minimalistic, eso-lang like Turing machine I made in Python. It simulates a single tape (array of booleans) with some simple instructions.

As far as i know, this isn't a faithful recreation of a Turing machine. It does have a few exceptions and limitations:
- The tape has a finite size.
- You can have 26 jump-to points, one for each letter.
- The program stops upon the head reaching the end of the tape.
- probably (definitely) some bugs.
  
## Syntax:
- `a` create jump to point
- `?` ask for state at head, 0 runs next instruction, 1 runs instruction after next
- `1` set bit at head to 1
- `0` set bit at head to 0
- `A` jump to point
- `;` halt
- `<` move head to left
- `>` move head to right

## How to use:
Run the function `run_program(tape,program)` with a string of zero's and ones' as the tape and the program as a string. Each argument can include other characters such as whitespace or newlines for readability, and they wont be counted.
- The `run_program()` function prints out the output tape with gaps between every n bits, the gap can be changed with the `bit_gap` variable.
- Changing `print_each_state` to true prints out where the head is and the current and following instructions that will run.


## Examples of Programs with pseudo code explanations:

### AND gate:
- program: `Ay>1;x>?;Ya?;X`

- pseudo code:
  ```
  goto A
  Y:
    step right
    set @head to 1
    halt
  X:
    step right
    if @head == 0: halt
    else: goto Y
  A:
    if @head == 0: halt
    else: goto X
  ```

### OR gate:
- program: `Ay>>1;z>1;x>?;Za?XY`
- pseudo code:
  ```
  goto A
  Y:
    step right
    step right
    set @head to 1
    halt

  Z:
    step right
    set @head to 1

  X:
    step right
    if @head==0: halt
    else: goto Z


  A:
    if @head==0: goto X
    else: goto Y
  ```
### XOR gate
- program: `Ab>?Z;c>?;Zz>1;a?CB`
- pseudo code:
  ```
  goto A
  B:
    step right
    if @head==0: goto Z
    else: halt

  C:
    step right
    if @head==0: halt
    else: goto Z

  Z:
    step right
    set @head to 1
    halt

  A:
    if @head==0: C
    else: goto B
  ```

### Half Adder
- program: `?XAa>?YBb>1;x>?;Yy>>1;`
- pseudo code:
  ```
  if @head == 0: goto XOR_A
  else: goto AND_A

  AND_A:
    step right
    if @head == 0: goto XOR_B
    else: goto AND_B

  AND_B: # if 11 then xor is 0
    step right
    @head = 1
    halt

  XOR_A:
    step right
    if @head == 0: halt
    else: goto XOR_B

  XOR_B:
    step right
    step right
    @head = 1
    halt
  ```
### Copy 4 bits to next 4 bits
- program: `?ABa>>>>0<<<?CDb>>>>1<<<?CDc>>>>0<<<?EFd>>>>1<<<?EFe>>>>0<<<?GHf>>>>1<<<?GHg>>>>0<<<;h>>>>1<<<;`
- expanded program:
  ```
  ?AB
  a >>>> 0 <<< ?CD
  b >>>> 1 <<< ?CD

  c >>>> 0 <<< ?EF
  d >>>> 1 <<< ?EF

  e >>>> 0 <<< ?GH
  f >>>> 1 <<< ?GH

  g >>>> 0 <<< ;
  h >>>> 1 <<< ;
  ```

###### No AI was used for writing this project except for a draft of the introduction to this README file.
