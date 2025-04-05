#include <WiFi.h>
#include <HTTPClient.h>

String URL = "http://192.168.100.6:5000/sensor";

const char* ssid = "ssid";
const char* password = "password";

int temperature;
int humidity;

String postData;

void setup() {
  Serial.begin(115200);
  connectWiFi();
}

void loop() {
  temperature = random(200);
  humidity = random(30);

  if(WiFi.status() != WL_CONNECTED) {
    connectWiFi();
  }

  postData = "{\"temperature\":\"" + String(temperature) + "\",\"humidity\":\"" + String(humidity) + "\"}";

  HTTPClient http;
  http.begin(URL);
  http.addHeader("Content-Type", "application/json");

  int httpCode = http.POST(postData);
  String payload = http.getString();

  Serial.print("URL : "); Serial.println(URL);
  Serial.print("Data: "); Serial.println(postData);
  Serial.print("httpCode: "); Serial.println(httpCode);
  Serial.print("payload : "); Serial.println(payload);
  Serial.println("--------------------------------------------------");

  delay(5000);
}

void connectWiFi() {
  WiFi.mode(WIFI_OFF);
  delay(1000);
  //This line hides the viewing of ESP as wifi hotspot
  WiFi.mode(WIFI_STA);
  
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
    
  Serial.print("connected to : "); Serial.println(ssid);
  Serial.print("IP address: "); Serial.println(WiFi.localIP());
}