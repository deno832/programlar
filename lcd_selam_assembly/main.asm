.include "m328pdef.inc"
.Cseg
.org 0x0000

ldi r17, 0xFF
out DDRD, r17

ldi r17, 0xFF
out DDRB, r17

Main:   ldi r20, 0x38
		out PORTD, r20
		cbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2



		ldi r20, 0x06
		out PORTD, r20

		cbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2



		ldi r20, 0x0C
		out PORTD, r20

		cbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2


		
		ldi r20, 0x01
		out PORTD, r20

		cbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2


		ldi r20, 0x80
		out PORTD, r20

		cbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2

		




		ldi r20, 0x53
		out PORTD, r20

		sbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2


		ldi r20, 0x65
		out PORTD, r20

		sbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2


		ldi r20, 0x6C
		out PORTD, r20

		sbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2



		ldi r20, 0x61
		out PORTD, r20

		sbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2

		ldi r20, 0x6D
		out PORTD, r20

		sbi PORTB, 4
		cbi PORTB, 3
		sbi PORTB, 2    ; 0x38 komudunu gönder
		call Delay
		cbi PORTB, 2

		call Delay_2
		call Delay_2

		call Delay_2

		call Delay_2

		call Delay_2

		call Delay_2

		call Delay_2

		call Delay_2


Delay:  ldi r23, 35
Loop3:  ldi r22, 50
Loop2:  ldi r21, 100
Loop1:  dec r21
		brne Loop1
		dec r22
		brne Loop2
		dec r23
		brne Loop3
		ret

Delay_2:  ldi r23, 200
Loop31:  ldi r22, 255
Loop21:  ldi r21, 255
Loop11:  dec r21
		brne Loop11
		dec r22
		brne Loop21
		dec r23
		brne Loop31
		ret