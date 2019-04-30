int r = 1;

void setup(){
  Serial.begin(9600);
}

void loop(){
  if(Serial.available()){
    r = Serial.read();
    Serial.println(char(r));
  }
}
