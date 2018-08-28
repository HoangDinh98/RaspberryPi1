#include <wiringPi.h>
#include <stdio.h>

#define ObstaclePin 0
#define LED1 2

int i = 0;

void setup (void)
{
	pinMode(LED1, OUTPUT);
	/* pinMode(ObstaclePin, INPUT); */
	pinMode(ObstaclePin, INPUT);
	digitalWrite(LED1, LOW);
}

void myISR(void)
{
	pinMode(LED1, OUTPUT);
	pinMode(ObstaclePin, INPUT);
	
	while ( digitalRead(ObstaclePin) == HIGH ) {
		digitalWrite(LED1, HIGH);
	}

	digitalWrite(LED1, LOW);
}

int main(void)
{
	if(wiringPiSetup()==-1)
	{
		printf("Setup wiringPi Failed\n");
		return -1;
	}

	setup();
	if(wiringPiISR(ObstaclePin, INT_EDGE_FALLING, &myISR) < 0){
		printf("Unable to setup ISR !!!\n");
		return 1;
	}

	
	while(1){
		;
	}

	return 0;
}
