

#include <atmel_start.h>
#include "touch_example.h"

extern volatile uint8_t measurement_done_touch;
uint8_t key_status = 0;

void touch_status_display(void);




int main(void)
{
	/* Initializes MCU, drivers and middleware */
	atmel_start_init();

	/* Replace with your application code */
	while (1) 
	{
	
		touch_process();
		if (measurement_done_touch == 1)
		 {
			measurement_done_touch = 0;
			touch_status_display();
		 }
	}
	
}


void touch_status_display(void)
{
	key_status = get_sensor_state(0) & KEY_TOUCHED_MASK;
	if (0u != key_status) {
		// LED_ON
		} else {
		// LED_OFF
	}
	key_status = get_sensor_state(1) & KEY_TOUCHED_MASK;
	if (0u != key_status) {
		// LED_ON
		} else {
		// LED_OFF
	}
	key_status = get_sensor_state(2) & KEY_TOUCHED_MASK;
	if (0u != key_status) {
		// LED_ON
		} else {
		// LED_OFF
	}
	key_status = get_sensor_state(3) & KEY_TOUCHED_MASK;
	if (0u != key_status) {
		// LED_ON
		} else {
		// LED_OFF
	}
}
