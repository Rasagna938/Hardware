#include "Arduino.h"

#define PINS_COUNT 6 // Number of common anode control pins (for each display)
#define NO_SEGMENTS 7 // Number of segments per display (a to g)

// Defining control pins for each seven-segment display
int pins[PINS_COUNT] = {9, 10, 11, 12, 13, A0};

// Defining segment control pins (a to g)
int segPins[NO_SEGMENTS]={2,3,4,5,6,7,8};

void setup() {
	 for (int i = 0; i < 7; i++) {
    pinMode(segPins[i], OUTPUT);
  }

    for (int i = 0; i < PINS_COUNT; i++) {
        pinMode(pins[i], OUTPUT);
    }
}
void sevenseg(int a,int b, int c ,int d,int e ,int f,int g)
{
	digitalWrite(2,a);
	digitalWrite(3,b);
	digitalWrite(4,c);
	digitalWrite(5,d);
	digitalWrite(6,e);
	digitalWrite(7,f);
	digitalWrite(8,g);
}
// Function to display a digit (0-9) on the seven-segment display

void displayDigit(int digit) {
	switch(digit){
		case 0:sevenseg(0, 0, 0, 0, 0, 0, 1);break;
		case 1:sevenseg(1, 0, 0, 1, 1, 1, 1);break;
		case 2:sevenseg(0, 0, 1, 0, 0, 1, 0);break;
		case 3:sevenseg(0, 0, 0, 0, 1, 1, 0);break;
		case 4:sevenseg(1, 0, 0, 1, 1, 0, 0);break;
		case 5:sevenseg(0, 1, 0, 0, 1, 0, 0);break;
		case 6:sevenseg(0, 1, 0, 0, 0, 0, 0);break;
		case 7:sevenseg(0, 0, 0, 1, 1, 1, 1);break;
		case 8:sevenseg(0, 0, 0, 0, 0, 0, 0);break;
		case 9:sevenseg(0, 0, 0, 0, 1, 0, 0);break;		
}
}
void loop() {
    //Extracting individual digits for each display
    int h1 = 0;  // Tens place of hours
    int h2 = 0;  // Units place of hours
    int m1 = 0;  // Tens place of minutes
    int m2 = 0;  // Units place of minutes
    int s1 = 0;  // Tens place of seconds
    int s2 = -1;  // Units place of seconds
do{
//Loop to display time for 24 hours
for(int i=0;i<82;i++){

    // Multiplexing for six displays
    digitalWrite(pins[0], HIGH);
    displayDigit(h1);
    delay(2);
    
    digitalWrite(pins[0], LOW);
    digitalWrite(pins[1], HIGH);
    displayDigit(h2);
    delay(2);
    
    digitalWrite(pins[1], LOW);
    digitalWrite(pins[2], HIGH);
    displayDigit(m1);
    delay(2);
    
    digitalWrite(pins[2], LOW);
    digitalWrite(pins[3], HIGH);
    displayDigit(m2);
    delay(2);
    
    digitalWrite(pins[3], LOW);
    digitalWrite(pins[4], HIGH);
    displayDigit(s1);
    delay(2);
    
    digitalWrite(pins[4], LOW);
    digitalWrite(pins[5], HIGH);
    displayDigit(s2);
    delay(2);
    
    digitalWrite(pins[5], LOW);
}
//Modifying Display after each second.
    s2++;
    if(s2>=10){
	    s2=0;
	    s1++;
    }
    if(s1>=6){
	    s1=0;
	    m2++;
    }
    if(m2>=10){
	    m2=0;
	    m1++;
    }
    if(m1>=6){
	    m1=0;
	    h2++;
    }
    if(h2>=10){
	    h2=0;
	    h1++;
    }
    if(h1>=3){
	    h1=0;
    }
    if (h1 == 2 && h2 == 4) {  
    h1 = 0;
    h2 = 0;
}

}while(s2>=0);
}
