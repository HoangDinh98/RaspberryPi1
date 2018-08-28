#include <wiringPi.h>
#include <stdio.h>

#define BtnPin    9
#define LedPin    10

int main(void)
{
	if(wiringPiSetupGpio() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(BtnPin, INPUT);
	pinMode(LedPin, OUTPUT);

	while(1){
		if(0 == digitalRead(BtnPin)){
			delay(10);
			if(0 == digitalRead(BtnPin)){
				while(!digitalRead(BtnPin));
				digitalWrite(LedPin, !digitalRead(LedPin));	
				printf("Button is pressed\n");	
			}
		}
	}

	return 0;
}