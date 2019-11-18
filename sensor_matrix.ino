const byte s0 = 26;//selection pins for bigmat columns (O/p section)
const byte s1 = 27;// EF
const byte s2 = 28;//port A
const byte s3 = 29;

const byte bc0 = 45;//o/p section for  small mat
const byte bc1 = 44;//port L
const byte bc2 = 43;
const byte bc3 = 42;

const byte t0 = 53;//big mat i/p section 1
const byte t1 = 52;// port b
const byte t2 = 51;//ip1
const byte t3 = 50;

const byte br0 = 33;//small mat ip section
const byte br1 = 32;
const byte br2 = 31;
const byte br3 = 30;//port C

int mu = 0;
int t = 0;
int star = 0;
float ttemp = 0;
//op variables
int a = 0;
int b = 0;
int c = 0;
int d = 0;
int ca=0,cb=0,cc=0,cd=0;

//mat ''op  analog " pin default for arduino mega
#define SIG_pin A7
#define SIG_pin2 A2

// input to mux" pin default for arduino mini pro
const byte OUT_pin1 = 7;//ip pins for big mat 1
const byte OUT_pin3=9;//small mat i/p



byte p3[16]={B00000000,B00010000,B00100000,B00110000,B01000000,B01010000,B01100000,B01110000,B10000000,B10010000,B10100000,B10110000,B11000000,B11010000,B11100000,B11110000};
byte p2[16]={B00000000,B00000001,B00000010,B00000011,B00000100,B00000101,B00000110,B00000111,B00001000,B00001001,B00001010,B00001011,B00001100,B00001101,B00001110,B00001111};

int valor = 0;//variable for sending bytes to processing
int valorback=0;
int tt2=0;
//matrix for mat
int calibra[15][12]; //big
int calibra_b[12][9];//back
int maxsensor[15][12];//Calibration array for the min values of each od the 225 sensors.
int maxsensor_b[12][9];
int minsensor_b=1000;
int temp=0;
int temp2=0;
int rw=0;
int cl=0;
int ttemp2=0;
int star2=0;  //Variable for staring the min array
void setup()
{
pinMode(s0, OUTPUT);
pinMode(s1, OUTPUT);
pinMode(s2, OUTPUT);
pinMode(s3, OUTPUT);

pinMode(t0, OUTPUT);
pinMode(t1, OUTPUT);
pinMode(t2, OUTPUT);
pinMode(t3, OUTPUT);

pinMode(bc0, OUTPUT);
pinMode(bc1, OUTPUT);
pinMode(bc2, OUTPUT);
pinMode(bc3, OUTPUT);

pinMode(br0, OUTPUT);
pinMode(br1, OUTPUT);
pinMode(br2, OUTPUT);
pinMode(br3, OUTPUT);

pinMode(OUT_pin1, OUTPUT);
pinMode(OUT_pin3, OUTPUT);

digitalWrite(s0, LOW);
digitalWrite(s1, LOW);
digitalWrite(s2, LOW);
digitalWrite(s3, LOW);

digitalWrite(t0, LOW);
digitalWrite(t1, LOW);
digitalWrite(t2, LOW);
digitalWrite(t3, LOW);

digitalWrite(bc0, LOW);
digitalWrite(bc1, LOW);
digitalWrite(bc2, LOW);
digitalWrite(bc3, LOW);

digitalWrite(br0, LOW);
digitalWrite(br1, LOW);
digitalWrite(br2, LOW);
digitalWrite(br3, LOW);

digitalWrite(OUT_pin1, HIGH);
digitalWrite(OUT_pin3, HIGH);

Serial.begin(115200);
sbi(ADCSRA, ADPS2);
cbi(ADCSRA, ADPS1);
cbi(ADCSRA, ADPS0);

// Full of 0's of initial matrix
for(byte j = 0; j < 15; j ++)
{

for(byte i = 0; i < 12; i ++)
{calibra[j][i] = 0;
maxsensor[j][i]=0;

}
}
backscreendefine();

for(byte k = 0; k < 50; k++){
for(byte j = 0; j < 15; j ++){

writeMux1(j);
for(byte i = 0; i < 12; i ++)
{ temp=readMux(i);
calibra[j][i] = calibra[j][i]+temp;
if( temp>maxsensor[j][i])
{maxsensor[j][i]=temp;
}
}
}
}

for(byte j = 0; j < 15; j ++)
{
writeMux1(j);
for(byte i = 0; i < 12; i ++){
calibra[j][i] = calibra[j][i]/50;
}
}
backscreen_calib();

}
void loop()
{
sensing();
}

int readMux(byte channel){
PORTA=p3[channel];
int val = analogRead(SIG_pin);

//return the value
return val;
}
int readMux2(byte channel){
PORTL=p3[channel];
int val = analogRead(SIG_pin2);

//return the value
return val;
}


void writeMux1(byte channel){
PORTB=p2[channel];
}

void writeMux3(byte channel){
PORTC=p3[channel];
}


void backscreendefine()
{

for(byte p = 0; p < 12; p ++)
{
for(byte q = 0; q < 9; q ++)
{
calibra_b[p][q] = 0;
maxsensor_b[p][q]=0;

}
}
}
void backscreen_calib()
{
for(byte k = 0; k < 70; k++){
for(byte p = 0; p < 12; p ++){
writeMux3(p);
for(byte q = 0; q < 9; q ++){
temp2=readMux2(q);
calibra_b[p][q] = calibra_b[p][q]+temp2;
if( temp2>maxsensor_b[p][q])
{maxsensor_b[p][q]=temp2;
}}}}

for(byte j = 0; j < 12; j ++){
writeMux3(j);
for(byte i = 0; i < 9; i ++){
calibra_b[j][i] = calibra_b[j][i]/70;
}}}
