subleq-sim
==========

Simulator for subleq (OISC)

This is a simple simulator for the one instruction set computer.  The syntax is limited, and restricted! =)

* Registers are just numbers.  For example u1 would be 1.
* Labels are allowed.  There is a special EXIT label that terminates the program.

Instructions
------------
* r1 1 33:  load the value 33 in register u1
* sl 1 2 3: perform subleq with a, b, c being u1, u2, u3
** Note that the third operand can be a label too. 
