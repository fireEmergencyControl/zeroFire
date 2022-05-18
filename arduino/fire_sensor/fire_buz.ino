int fire = A0;
int buz = 12;
int val = 0;

void setup (){
  Serial.begin(9600);
  pinMode(fire, INPUT);
  pinMode(buz, OUTPUT);

//  pinMode(9, OUTPUT);
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
  } else {
    digitalWrite (buz, LOW);
  }
  delay (1000);

//  fire = analogRead(A1);
//    delay(100);
//    Serial.print("Fire =");
//    delay(500);
//
//    if(fire > 0) {
//      digitalWrite(9,HIGH);
//      tone(8,1000,50);
//      delay(100);
//
//      digitalWrite(9,LOW);
//      tone(8,200,50);
//      delay(100);
//
//    } else {
//      digitalWrite(9,LOW);
//      noTone(8);
//      delay(100);
//    }
}