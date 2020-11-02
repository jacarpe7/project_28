/*
 * AVR128-rawblink.c
 *
 * Created: 2020-09-28 17:02:18
 * Author : bobm
 */ 

#define F_CPU 4000000

#include <avr/io.h>
#include <util/delay.h>

#define LED_BUTTON0	5	//port A
#define LED_BUTTON1	3	// port C


int main(void)
{
	
	PORTA.DIR = (1 << LED_BUTTON0);
	PORTA.OUTSET = (1 << LED_BUTTON0);
	
	PORTC.DIR = (1 << LED_BUTTON1);
	PORTC.OUTSET = (1 << LED_BUTTON1);
	
	
	while (1)
	{
		
		
		
		PORTA.OUTSET = (1 << LED_BUTTON0);
		PORTC.OUTCLR = (1 << LED_BUTTON1);
		_delay_ms(500);
		PORTA.OUTCLR = (1 << LED_BUTTON0);
		PORTC.OUTSET = (1 << LED_BUTTON1);
		_delay_ms(500);
		
	}
}


