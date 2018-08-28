#include <wiringPi.h>
#include <stdio.h>

#define LED1 19 /* GPIO 19  BCM */

void bat_led(int led);
void tat_led(int led);

void bat_led(int led)
{
	digitalWrite(led, HIGH);
}

void tat_led(int led)
{
	digitalWrite(led, LOW);
}

int main(void)
{
	if(wiringPiSetupGpio()==-1)
	{
		printf("Setup wiringPi Failed\n");
		return -1;
	}

	/* cai dat su dung chan la OUTPUT */
	pinMode(LED1, OUTPUT);

	while(1)
	{
		bat_led(LED1);
		delay(1000);

		tat_led(LED1);
		delay(100);

	}
	return 0;
}
