//#include <WiFi.h>         //WIFI shield
#include <ESP8266WiFi.h>  //ESP8266
#include <PubSubClient.h>
 
char ssid[] = "KT_GiGA_2G_Wave2_72E6";
char password[] = "axc1kf9290";
const char* mqtt_server = "172.30.1.21"; //mqtt_server_IP
 
WiFiClient espClient;
PubSubClient client(espClient);


void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
  Serial.println(WiFi.status());
  Serial.println(WL_CONNECTED);
  while (WiFi.status() != WL_CONNECTED) {
    //for(int i = 0; i<500; i++){
      delay(500);
    //}
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
 
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ClientID")) { //change to ClientID
      Serial.println("connected");
       
      // ... and resubscribe
      client.subscribe("Topic");
 
      // Once connected, publish an announcement...
      client.publish("Topic", "test msg");
       
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
    }
  }
}
 
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  String msg = "";
  for (int i = 0; i < length; i++) {
    msg +=(char)payload[i];
  }
  Serial.print(msg);
  Serial.println();
}
 
void setup() {
  Serial.begin(115200);       //Arduino
  pinMode(A0, INPUT);   
  pinMode (12, OUTPUT);
  //Serial.begin(115200);   //ESP8266
  setup_wifi();                   // Connect to wifi 
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
   
}
 
void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  int x = analogRead (A0);
  Serial.println (x);
   
  if (x < 900)
  {    
   Serial.println(" FLAME DETECTED!");
   client.publish("alert:fire", "fire");    
   digitalWrite (12, HIGH);
  }  
  else  
  {    
    digitalWrite (12, LOW);
  }  
  delay (1000);
   
}
