char msg[3];
int pins[] = {2, 3, 4, 5, 8, 9, 10, 11};
int states[] = {0, 0, 0, 0, 0, 0, 0, 0};


void switcher(int pin){
  if (states[pin]){
    states[pin] = 0;
    digitalWrite(pins[pin], LOW);
  }
  else{
    states[pin] = 1;
    digitalWrite(pins[pin], HIGH);
  }
}


void setup() {
  Serial.begin(9600);
  for(int i=0; i<8; i++){
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
 
}

void loop() {
  if(Serial.available()){
    Serial.readBytes(msg, 2);
    switch(msg[1]){
    case '0':
      if (!states[msg[0]]){
        digitalWrite(pins[msg[0]], HIGH);
        delay(500);
        digitalWrite(pins[msg[0]], LOW);
      }
      else{
         digitalWrite(pins[msg[0]], LOW);
        delay(500);
        digitalWrite(pins[msg[0]], HIGH);
      }
      break;
    
    case '1':
      switcher(msg[0]);
      
    }
    Serial.println("ok");
  }

}
