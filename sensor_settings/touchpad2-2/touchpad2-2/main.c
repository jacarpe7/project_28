#include <atmel_start.h>

void touch_example(void);


int main(void)
{
	/* Initializes MCU, drivers and middleware */
	atmel_start_init();
	
	// debug port blip
	PORTF.DIRSET = (1 << 4);	// PF4 blip
	PORTF.OUTCLR = (1 << 4);

	/* Replace with your application code */
	while (1) 
	{
		
		touch_example();
	
	
	}
}
