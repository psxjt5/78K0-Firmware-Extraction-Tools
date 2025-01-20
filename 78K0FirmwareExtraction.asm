	nop
	nop
	di			; Disable Interrupts
	mov 0xff25,#0		; Set Port 5 as an Output (4-Bit Wide).
	nop
	mov 0xff2c,#0		; Set Port 12 as an Output (1-Bit Wide).
	nop
	nop
	nop
	mov 0xff98, #0x77	; Disable the watchdog
	movw HL, #0		; Clear the HL Register

ByteLoop:
	nop
	nop
	nop
	nop
	nop
	nop
	mov A, [HL]		; Get the contents of the next memory location.
	mov B, #0		; Clear the B register.
	nop
	nop
	incw HL			; Increment the address counter.

BitLoop:
	set1 0xff0c.0		; Clock HIGH.
	mov E, A		; E = A.
	mov A, B		; A = B.
	nop
	nop
	mov 0xff05, A		; Output the bit position on Port 5.
	nop
	nop
	nop
	mov B, A		; B = A.
	mov A, E		; A = E.
	ror A, 1		; Get the LSB into CY and rotate A once.
	nop
	nop
	mov1 0xff05.3, CY	; Output the bit on port 5 (as MSB).
	clr1 0xff0c.0		; Clock LOW.
	mov D,A			; D = A
	mov A,B			; A = bit position (B).
	inc A			; Increment the bit position for next time.
	cmp A, #8		; Loop condition (check if all bits have been outputted).
	bz ByteLoop		; Branch to ByteLoop if all bits have been outputted.
	mov B,A			; B = A (B = position counter).
	mov A,D			; A = D
	br BitLoop		; Get the next bit and output.