
/*============================================================================
Filename : datastreamer_UART_avr.c
Project : QTouch Modular Library
Purpose : Provides the datastreamer protocol implementation, transmission of
          module data to data visualizer software using UART port.

This file is part of QTouch Modular Library 7.4.1 application.

Important Note: Do not edit this file manually.
                Use QTouch Configurator within Atmel Start to apply any
                modifications to this file.

Usage License: Refer license.h file for license information
Support: Visit http://www.microchip.com/support/hottopics.aspx
               to create MySupport case.

------------------------------------------------------------------------------
Copyright (c) 2020 Microchip. All rights reserved.
------------------------------------------------------------------------------
============================================================================*/

/*----------------------------------------------------------------------------
  include files
----------------------------------------------------------------------------*/

#include <stdio.h>
#include <string.h>


#include "datastreamer.h"
#include "driver_init.h"

#if (DEF_TOUCH_DATA_STREAMER_ENABLE == 1u)

/*----------------------------------------------------------------------------
 *     defines
 *--------------------------------------------------------------------------*/

#define ACQ_MODULE_AUTOTUNE_OUTPUT 0u

#define FREQ_HOP_AUTO_MODULE_OUTPUT 1u

#define SCROLLER_MODULE_OUTPUT 1u

#define SURFACE_MODULE_OUTPUT 0u

/*----------------------------------------------------------------------------
  global variables
----------------------------------------------------------------------------*/
extern qtm_acquisition_control_t qtlib_acq_set1;
extern qtm_touch_key_control_t   qtlib_key_set1;
extern qtm_touch_key_config_t    qtlib_key_configs_set1[DEF_NUM_SENSORS];

extern qtm_freq_hop_autotune_control_t qtm_freq_hop_autotune_control1;

extern qtm_scroller_control_t qtm_scroller_control1;

extern uint8_t module_error_code;

uint8_t data[] = {
    0x5F, 0xB4, 0x00, 0x86, 0x4A, 0x03, 0xEB, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xAA, 0x55, 0x01, 0x6E, 0xA0};

/*----------------------------------------------------------------------------
  prototypes
----------------------------------------------------------------------------*/
void datastreamer_transmit(uint8_t data);

/*----------------------------------------------------------------------------
 *   function definitions
 *--------------------------------------------------------------------------*/

/*============================================================================
void datastreamer_init(void)
------------------------------------------------------------------------------
Purpose: Initialization for datastreamer module
Input  : none
Output : none
Notes  :
============================================================================*/
void datastreamer_init(void)
{
}

/*============================================================================
void datastreamer_transmit(uint8_t data_byte)
------------------------------------------------------------------------------
Purpose: Transmits the single byte through the configured UART port.
Input  : Byte to be transmitted
Output : none
Notes  :
============================================================================*/
void datastreamer_transmit(uint8_t data_byte)
{
	while (!USART_is_tx_ready())
		;

	USART_write(data_byte);

	while (USART_is_tx_busy())
		;
}


void byte_output(void);
void ascii_output(void);

/*============================================================================
void datastreamer_output(void)
------------------------------------------------------------------------------
Purpose: Forms the datastreamer frame based on the configured modules, Tranmits
         the frame as single packet through UART port.
Input  : none
Output : none
Notes  : The data visualizer scripts that are generated in the project should be
         set on the data visualizer software.
============================================================================*/

#define ASCII_OUTPUT 1
#define BYTE_OUTPUT 2

uint8_t data_tx_mode = ASCII_OUTPUT;

void datastreamer_output(void)
{

	if(data_tx_mode == ASCII_OUTPUT)
		ascii_output();
	else byte_output();


}

char tx_data[80];


void send_string(char *str_ptr)
{

	char *tx_ptr;

	tx_ptr = str_ptr;

	while(*tx_ptr)
	 datastreamer_transmit((uint8_t)(*tx_ptr++));

}

void ascii_output(void)
{

	static uint8_t	sequence = 0;
	int16_t			touch_signal,touch_reference,touch_delta,comp_caps;
	uint8_t			channel_index,touch_state;


	sprintf(tx_data,"%04d,",sequence);
	send_string(tx_data);

	for(channel_index = 0;channel_index <DEF_NUM_CHANNELS;channel_index++ )
	{
		// tx channel id
		// sprintf(tx_data,"ch:%04d ",channel_index);
		// send_string(tx_data);
		touch_signal = get_sensor_node_signal(channel_index);

		// tx signal value
		// sprintf(tx_data,"sig:%04d ",touch_signal);
		// send_string(tx_data);

		// tx reference
		touch_reference = get_sensor_node_reference(channel_index);
		// sprintf(tx_data,"ref:%04d ",touch_reference);
		// send_string(tx_data);

		// tx delta
		touch_delta = touch_signal - touch_reference;
		sprintf(tx_data,"%04d,",touch_delta);
		send_string(tx_data);


		// transmit state

		// touch_state = get_sensor_state(channel_index) & 0x80;
		// if(touch_state)
		// 	send_string("on\r\n");
		// else send_string("off\r\n");

	}
	sequence++;
	send_string("\n");


}





void byte_output(void)
{
	int16_t           temp_int_calc;
	static uint8_t    sequence = 0u;
	uint16_t          u16temp_output;
	uint8_t           u8temp_output;
	volatile uint16_t count_bytes_out;

/*

	send_header = sequence & (0x0f);
	if (send_header == 0) {
		for (i = 0; i < sizeof(data); i++) {
			datastreamer_transmit(data[i]);
		}
	}
*/




	// Start token
	datastreamer_transmit(0x55);

	// Frame Start
	datastreamer_transmit(sequence++);
	for (count_bytes_out = 0u; count_bytes_out < DEF_NUM_CHANNELS; count_bytes_out++) {

		/* Signals */
		u16temp_output = get_sensor_node_signal(count_bytes_out);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* Reference */
		u16temp_output = get_sensor_node_reference(count_bytes_out);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* Touch delta */
		temp_int_calc = get_sensor_node_signal(count_bytes_out);
		temp_int_calc -= get_sensor_node_reference(count_bytes_out);
		u16temp_output = (uint16_t)(temp_int_calc);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		/* Comp Caps */
		u16temp_output = get_sensor_cc_val(count_bytes_out);
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

/*

#if (ACQ_MODULE_AUTOTUNE_OUTPUT == 1)
#if (DEF_PTC_CAL_OPTION == CAL_AUTO_TUNE_CSD)
		// CSD
		u8temp_output = qtlib_acq_set1.qtm_acq_node_config[count_bytes_out].node_csd;
		datastreamer_transmit(u8temp_output);
#else
		// Prescalar
		u8temp_output = NODE_PRSC(qtlib_acq_set1.qtm_acq_node_config[count_bytes_out].node_rsel_prsc);
		datastreamer_transmit(u8temp_output);
#endif
#endif

*/


		/* State */
		u8temp_output = get_sensor_state(count_bytes_out);
		if (0u != (u8temp_output & 0x80)) {
			datastreamer_transmit(0x01);
		} else {
			datastreamer_transmit(0x00);
		}

		/* Threshold */
		datastreamer_transmit(qtlib_key_configs_set1[count_bytes_out].channel_threshold);
	}

/*

	for (count_bytes_out = 0u; count_bytes_out < qtm_scroller_control1.qtm_scroller_group_config->num_scrollers;
	     count_bytes_out++) {

		// Slider State
		u8temp_output = qtm_scroller_control1.qtm_scroller_data[count_bytes_out].scroller_status;
		if (0u != (u8temp_output & 0x01)) {
			datastreamer_transmit(0x01);
		} else {
			datastreamer_transmit(0x00);
		}

		// Slider Delta
		u16temp_output = qtm_scroller_control1.qtm_scroller_data[count_bytes_out].contact_size;
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		// Slider Threshold
		u16temp_output = qtm_scroller_control1.qtm_scroller_config[count_bytes_out].contact_min_threshold;
		datastreamer_transmit((uint8_t)u16temp_output);
		datastreamer_transmit((uint8_t)(u16temp_output >> 8u));

		// filtered position
		u16temp_output = qtm_scroller_control1.qtm_scroller_data[count_bytes_out].position;
		datastreamer_transmit((uint8_t)(u16temp_output & 0x00FFu));
		datastreamer_transmit((uint8_t)((u16temp_output & 0xFF00u) >> 8u));
	}


*/

/*
#if (FREQ_HOP_AUTO_MODULE_OUTPUT == 1)

	datastreamer_transmit(qtlib_acq_set1.qtm_acq_node_group_config->freq_option_select);

	for (uint8_t count = 0u; count < qtm_freq_hop_autotune_control1.qtm_freq_hop_autotune_config->num_freqs; count++) {
		datastreamer_transmit(qtm_freq_hop_autotune_control1.qtm_freq_hop_autotune_config->median_filter_freq[count]);
	}
#endif
*/


	/* Other Debug Parameters */
	datastreamer_transmit(module_error_code);

	/* Frame End */
	// datastreamer_transmit(sequence++);

	/* End token */
	datastreamer_transmit(~0x55);
}

#endif
