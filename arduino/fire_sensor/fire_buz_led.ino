int fire = A0;
int buz = 12;
int val = 0;
int led = 8;

void setup (){
  Serial.begin(9600);
  pinMode(fire, INPUT);
  pinMode(buz, OUTPUT);

  pinMode(led, OUTPUT);
}

void loop (){
  val = analogRead(fire);
  Serial.print ("Sensor Value: ");
  Serial.println(val);

//  int x = analogRead (A0);
//  Serial.println (x);

  if (val > 0) {
    Serial.println("FLAME DETECTED!");
    digitalWrite (buz, HIGH);
//    tone(8,1000,50);
    digitalWrite(8,HIGH);
  } else {
    digitalWrite (buz, LOW);
    noTone(8);
    digitalWrite(8,LOW);
  }
  delay (1000);
}