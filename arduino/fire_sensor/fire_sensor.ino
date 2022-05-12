int flame = A1;     //센서 연결
int LED = 10;       //LED 연결
 
void setup() {
  Serial.begin(9600);
  pinMode(flame, INPUT);
  pinMode(LED, OUTPUT);
}
 
void loop() {
  int val = analogRead(flame);
  Serial.print("flame_sensor : ");
  Serial.println(val);
 
  if(val<1023) {     //값이 1023미만이면 LED 불이 켜집니다.
    digitalWrite(LED, HIGH);
    Serial.println("FIRE!!!!");
  }
  else{
    digitalWrite(LED, LOW);
    Serial.println("NO FIRE");
  }
  delay(200);
}
