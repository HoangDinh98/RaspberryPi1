#include <wiringPi.h>
#include <stdio.h>

#define LED1 0 /* GPIO 17  BCM */
#define LED2 1 /* GPIO 18  BCM */
#define LED3 2 /* GPIO 27  BCM */
#define LED4 3 /* GPIO 22  BCM */
#define LED5 4 /* GPIO 23 BCM */
#define LED6 5 /* GPIO 24  BCM */
#define LED7 6 /* GPIO 25  BCM */
#define LED8 7 /* GPIO 4  BCM */

void bat_led(int led);
void tat_led(int led);

void bat_led(int led)
{
	digitalWrite(led, HIGH);
	delay(200);
}

void tat_led(int led)
{
	digitalWrite(led, LOW);
}

int main(void)
{
	if(wiringPiSetup()==-1)
	{
		printf("Setup wiringPi Failed\n");
		return -1;
	}

	/* cai dat su dung chan la OUTPUT */
	pinMode(LED1, OUTPUT);
	pinMode(LED2, OUTPUT);
	pinMode(LED3, OUTPUT);
	pinMode(LED4, OUTPUT);
	pinMode(LED5, OUTPUT);
	pinMode(LED6, OUTPUT);
	pinMode(LED7, OUTPUT);
	pinMode(LED8, OUTPUT);

	while(1)
	{
		printf(" Bat 1 LED \n");
		bat_led(LED1);
		printf(" Tat 1 LED \n");
		tat_led(LED1);
		printf(" Bat 2 LED \n");
		bat_led(LED2);
		printf(" Tat 2 LED \n");
		tat_led(LED2);
		printf(" Bat 3 LED \n");
		bat_led(LED3);
		printf(" Tat 3 LED \n");
		tat_led(LED3);
		printf(" Bat 4 LED \n");
		bat_led(LED4);
		printf(" Tat 4 LED \n");
		tat_led(LED4);
		printf(" Bat 5 LED \n");
		bat_led(LED5);
		printf(" Tat 5 LED \n");
		tat_led(LED5);
		printf(" Bat 6 LED \n");
		bat_led(LED6);
		printf(" Tat 6 LED \n");
		tat_led(LED6);
		printf(" Bat 7 LED \n");
		bat_led(LED7);
		printf(" Tat 7 LED \n");
		tat_led(LED7);
		printf(" Bat 8 LED \n");
		bat_led(LED8);
		printf(" Tat 8 LED \n");
		tat_led(LED8);

	}
	return 0;
}
