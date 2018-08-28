#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define IR 0
#define SENSOR 1

int cnt = 0;

void myISR(void)
{
	printf("Recevied infrared. cnt = %d\n", ++cnt); 
}

void readIR(void) {
	uint8_t laststate = HIGH;
	pinMode(IR, INPUT);

	if ( digitalRead(IR) == laststate ){
		printf("Recived OK \n");
	}
}


int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}
	pinMode(IR, INPUT);
	pinMode(SENSOR, OUTPUT);
	digitalWrite(SENSOR, HIGH);
	while(1) {
		readIR();
		delay(100);
	};

	return 0;
}
