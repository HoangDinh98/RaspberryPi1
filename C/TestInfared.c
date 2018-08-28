#include <wiringPi.h>
#include <stdio.h>

#define SOURCE 0 /* GPIO 17 */
#define RECEIVER 1 /* GPIO 18  */

int cnt = 0;

void myISR(void)
{
	printf("Recevied infrared. cnt = %d\n", ++cnt); 
}

int main(void)
{
	int i = 0;
	if(wiringPiSetup()==-1)
	{
		printf("Setup wiringPi Failed\n");
		return -1;
	}

	if(!wiringPiISR(RECEIVER, INT_EDGE_FALLING, &myISR) == -1){
		printf("setup ISR failed !");
		return 1;
	}

	pinMode(SOURCE, OUTPUT);
	pinMode(RECEIVER, INPUT);
	
	digitalWrite(SOURCE, HIGH);

	while(1) {
		if(!wiringPiISR(RECEIVER, INT_EDGE_FALLING, &myISR) == -1){
			printf("setup ISR failed !");
			return 1;
		}
	}

}