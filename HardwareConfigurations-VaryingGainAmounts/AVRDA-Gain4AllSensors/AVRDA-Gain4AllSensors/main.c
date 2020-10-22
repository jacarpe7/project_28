#include <atmel_start.h>
/*----------------------------------------------------------------------------
 *   Extern variables
 *----------------------------------------------------------------------------*/
extern volatile uint8_t measurement_done_touch;

/*----------------------------------------------------------------------------
 *   Global variables
 *----------------------------------------------------------------------------*/
uint8_t key_status1 = 0;

uint8_t  scroller_status1   = 0;
uint16_t scroller_position1 = 0;

/*----------------------------------------------------------------------------
 *   prototypes
 *----------------------------------------------------------------------------*/
void touch_status_display1(void);

int main(void)
{
	/* Initializes MCU, drivers and middleware */
	atmel_start_init();

	/* Replace with your application code */
	while (1) {
		touch_process();

		if (measurement_done_touch == 1) {
			measurement_done_touch = 0;
			touch_status_display1();
		}
	}
}

/*============================================================================
void touch_status_display(void)
------------------------------------------------------------------------------
Purpose: Sample code snippet to demonstrate how to check the status of the
         sensors
Input  : none
Output : none
Notes  : none
============================================================================*/
void touch_status_display1(void)
{
	key_status1 = get_sensor_state(0) & 0x80;
	if (0u != key_status1) {
		LED_6_set_level(false);
	} else {
		LED_6_set_level(true);
	}
	key_status1 = get_sensor_state(1) & 0x80;
	if (0u != key_status1) {
		LED_7_set_level(false);
	} else {
		LED_7_set_level(true);
	}

	scroller_status1   = get_scroller_state(0);
	scroller_position1 = get_scroller_position(0);

	LED_0_set_level(true);
	LED_1_set_level(true);
	LED_2_set_level(true);
	LED_3_set_level(true);
	LED_4_set_level(true);
	LED_5_set_level(true);

	if (0u != scroller_status1) {

		LED_5_set_level(false);

		if (scroller_position1 > 43) {
			LED_4_set_level(false);
		}
		if (scroller_position1 > 85) {
			LED_3_set_level(false);
		}
		if (scroller_position1 > 120) {
			LED_2_set_level(false);
		}
		if (scroller_position1 > 165) {
			LED_1_set_level(false);
		}
		if (scroller_position1 > 213) {
			LED_0_set_level(false);
		}
	}
}
