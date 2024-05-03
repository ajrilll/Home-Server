#include <WiFi.h>
#include <WebSocketsServer.h>
//#include <Servo.h>

//Servo servo;
const char* ssid = "user";
const char* password = "pass";
const int webSocketPort = 80;
const int relayPin = 10; 
//const int servoPin = 26; // Pin untuk servo
//const int lightPin = 25; // Pin untuk sensor cahaya
//int lightValue = 0; // Variabel untuk menyimpan nilai sensor cahaya

int status = 0;

WebSocketsServer webSocket = WebSocketsServer(webSocketPort);

void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t length) {
  switch(type) {
    case WStype_DISCONNECTED:
      Serial.printf("[%u] Koneksi terputus!\n", num);
      break;
    case WStype_CONNECTED: {
        IPAddress ip = webSocket.remoteIP(num);
        Serial.printf("[%u] Koneksi dari %d.%d.%d.%d\n", num, ip[0], ip[1], ip[2], ip[3]);
      }
      break;
    case WStype_TEXT:
      Serial.printf("[%u] Menerima pesan: %s\n", num, payload);
       if (strcmp((char*)payload, "1") == 0) {
          if (status == 0) {
            digitalWrite(relayPin, HIGH); // Nyalakan LED jika status mati
            status = 1; // Update status menjadi menyala
          } else {
            digitalWrite(relayPin, LOW); // Matikan LED jika status menyala
            status = 0; // Update status menjadi mati
          }
       }
//       if (strcmp((char*)payload, "2") == 0) {
//        lightValue = analogRead(lightPin); // Baca nilai sensor cahaya
//            Serial.print("Nilai Sensor Cahaya: ");
//            Serial.println(lightValue);
//      
//            if (lightValue < 512) {
//              servo.write(0); // Gerakkan servo ke posisi 0 derajat jika cahaya kurang dari 512
//              Serial.println("Cahaya Kurang dari 512, Servo Bergerak ke 0 Derajat");
//            } else {
//              servo.write(180); // Gerakkan servo ke posisi 180 derajat jika cahaya lebih dari atau sama dengan 512
//              Serial.println("Cahaya Lebih dari atau Sama dengan 512, Servo Bergerak ke 180 Derajat");
//            }
//       }
      break;
  }
}


void setup() {
  Serial.begin(115200);
 // servo.attach(servoPin); // Pasang servo ke pin servoPin
  //servo.write(90); // Inisialisasi posisi servo pada 90 derajat
  //pinMode(lightPin, INPUT); // Atur pin sensor cahaya sebagai input
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW); // Matikan LED awal
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Koneksi ke WiFi...");
  }

  Serial.println("WiFi Terhubung!");
  Serial.println("IP Address: ");
  Serial.println(WiFi.localIP());

  webSocket.begin();
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  webSocket.loop();
}
