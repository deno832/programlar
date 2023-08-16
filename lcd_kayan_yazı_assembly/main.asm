.include "m328pdef.inc"
.Cseg
.org 0x0000

ldi r17, 0xFF
out DDRD, r17

ldi r17, 0xFF
out DDRB, r17

Main:   ldi r16, 0x38
		call Send_command


		ldi r16, 0x06
		call Send_command


		ldi r16, 0x0C
		call Send_command


		ldi r16, 0x01
		call Send_command
		; Lcd Initialize Sonu

		ldi r16, 0x80
		call Send_command ; 1. Sat�r 1. S�tuna Git

		call Isim_yaz

		call Delay_a

		ldi r24, 8
		call Ekrani_kaydir   ; B�t�n Ekran� Sa�a Kayd�rma

		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma




		ldi r16, 0x80
		call Send_command    ; 1.Sat�ra Ge�me
		
		ldi r26, 9
		call Imlec_kaydir

		call Isim_yaz
		call Delay_a

		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r26, 11
		call Imlec_kaydir

		call Isim_yaz
		

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me

		ldi r17, 0x33
		call Send_data       ; 3 Rakam�n� Yazd�rma

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma
		call Delay_a




		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r26, 12
		call Imlec_kaydir    ; �mleci Kayd�rma

		call Isim_yaz

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me


		ldi r17, 0x38
		call Send_data       ; 8 Rakam�n� Yazd�rma

		ldi r17, 0x33
		call Send_data       ; 3 Rakam�n� Yazd�rma

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma

		call Delay_a





		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r26, 13
		call Imlec_kaydir    ; �mleci Kayd�rma

		call Isim_yaz

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me

		ldi r17, 0x20
		call Send_data       ; 8 Rakam�n� Yazd�rma

		ldi r17, 0x38
		call Send_data       ; 8 Rakam�n� Yazd�rma

		ldi r17, 0x33
		call Send_data       ; 3 Rakam�n� Yazd�rma

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma

		call Delay_a



		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r26, 14
		call Imlec_kaydir    ; �mleci Kayd�rma

		call Isim_yaz

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me

		ldi r17, 0x4F
		call Send_data       ; Bo�luk Yazd�rma

		ldi r17, 0x20
		call Send_data       ; Bo�luk Yazd�rma

		ldi r17, 0x38
		call Send_data       ; 8 Rakam�n� Yazd�rma

		ldi r17, 0x33
		call Send_data       ; 3 Rakam�n� Yazd�rma

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma

		call Delay_a



		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r26, 15
		call Imlec_kaydir    ; �mleci Kayd�rma

		call Isim_yaz

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me

		ldi r17, 0x4E
		call Send_data       ; N Harfini Yazd�rma

		ldi r17, 0x4F
		call Send_data       ; O Harfini Yazd�rma

		ldi r17, 0x20
		call Send_data       ; Bo�luk Yazd�rma

		ldi r17, 0x38
		call Send_data       ; 8 Rakam�n� Yazd�rma

		ldi r17, 0x33
		call Send_data       ; 3 Rakam�n� Yazd�rma

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma

		call Delay_a
		


		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r26, 16
		call Imlec_kaydir    ; �mleci Kayd�rma

		call Isim_yaz

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me

		ldi r17, 0x45
		call Send_data       ; E Harfini Yazd�rma

		ldi r17, 0x4E
		call Send_data       ; N Harfini Yazd�rma

		ldi r17, 0x4F
		call Send_data       ; O Harfini Yazd�rma

		ldi r17, 0x20
		call Send_data       ; Bo�luk Yazd�rma

		ldi r17, 0x38
		call Send_data       ; 8 Rakam�n� Yazd�rma

		ldi r17, 0x33
		call Send_data       ; 3 Rakam�n� Yazd�rma

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma

		call Delay_a




		ldi r16, 0x01
		call Send_command    ; Ekran� Temizleme

		ldi r26, 17
		call Imlec_kaydir    ; �mleci Kayd�rma

		call Isim_yaz

		ldi r16, 0xC0      
		call Send_command    ; 2. Sat�ra Ge�me

        ldi r16, 0xC0
		call Send_command    ; 2. Sat�ra Ge�me

		ldi r17, 0x44
		call Send_data       ; E Harfini Yazd�rma

		ldi r17, 0x45
		call Send_data       ; E Harfini Yazd�rma

		ldi r17, 0x4E
		call Send_data       ; N Harfini Yazd�rma

		ldi r17, 0x4F
		call Send_data       ; O Harfini Yazd�rma

		ldi r17, 0x20
		call Send_data       ; Bo�luk Yazd�rma

		ldi r17, 0x38
		call Send_data       ; 8 Rakam�n� Yazd�rma

		ldi r17, 0x33
		call Send_data       ; 3 Rakam�n� Yazd�rma

		ldi r17, 0x32
		call Send_data       ; 2 Rakam�n� Yazd�rma

		ldi r24, 23
		call Ekrani_kaydir   ; B�t�n Ekran� Sa�a Kayd�rma
		
		rjmp Main

Delay:  ldi r23, 10
Loop3:  ldi r22, 20
Loop2:  ldi r21, 20
Loop1:  dec r21
		brne Loop1
		dec r22
		brne Loop2
		dec r23
		brne Loop3
		ret

Delay_a:  ldi r23, 50
Loop3_a:  ldi r22, 255
Loop2_a:  ldi r21, 255
Loop1_a:  dec r21
		brne Loop1_a
		dec r22
		brne Loop2_a
		dec r23
		brne Loop3_a
		ret

Send_data: out PORTD, r17
		   sbi PORTB, 4
		   cbi PORTB, 3
		   sbi PORTB, 2    
		   call Delay
		   cbi PORTB, 2
		   ret


Imlec_kaydir: ldi r16, 0x14
			  call Send_command
			  call Delay
			  dec r26
			  brne Imlec_kaydir
			  ret

Ekrani_kaydir: ldi r16, 0x1C
			   call Send_command
			   call Delay_a
			   dec r24
			   brne Ekrani_kaydir
			   ret

Send_command: out PORTD, r16
			  cbi PORTB, 4
		   	  cbi PORTB, 3
			  sbi PORTB, 2    
			  call Delay
			  cbi PORTB, 2
			  ret

Isim_yaz: ldi r17, 0x44
		  call Send_data   ; D harfi

		  ldi r17, 0x45
		  call Send_data   ; E harfi

	 	  ldi r17, 0x4E
		  call Send_data   ; N harfi

		  ldi r17, 0x4F
		  call Send_data   ; O harfi

		  ldi r16, 0x14
		  call Send_command

		  ldi r17, 0x38
		  call Send_data   ; 8 Rakam�

		  ldi r17, 0x33
		  call Send_data   ; 3 Rakam�

		  ldi r17, 0x32
		  call Send_data   ; 2 Rakam�

		  ret



No_reset: rjmp No_reset