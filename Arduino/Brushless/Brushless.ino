#include <Servo.h>

Servo Brushless1;
boolean initializeState = 0;
int speed;

void setup(){
	// Attach brushless motor 
	Brushless1.attach(9);
	Serial.begin(9600);
	Brushless1.write(0);
	Serial.print("Ready for setting up Brushless Motor.");
}

void motorinit(){
	Serial.print("Start initailizing Brushless Motor.\n");
	Serial.print("Setting high speed! Wait 2 second! ");
	Brushless1.write(180);
	delay(2000);
	Serial.print("Setting low speed! Wait 4 sec! ");
	Brushless1.write(5);
	delay(4000);
	Serial.print("MOTOR IS READY! ");
}

void setspeed(int val){
	Serial.print('Arduino Setspeed!');
	Brushless1.write(val);
}

void loop(){
	String ans;
	char com[20];
	Serial.print("Please Provide Some Instructions.");
	while(Serial.available()==0){}
	ans = Serial.readString();
	ans.toCharArray(com, 20);
	switch(com[0]){
		case 'i':
			motorinit();
			break;
		case 's':
			int val;
			val = atoi(&com[1]);
			setspeed(val);
			break;
		default:
		Serial.println('Invalid command.');
	}
}
