int trig = 12;                   //超音波發送腳位
int echo = 11;                   //超音波接收腳位
int ir1 = 2;                     //紅外線1接收腳位 (左邊)
int ir2 = 3;                     //紅外線2接收腳位 (右邊)       
//  int irv1,irv2=1;                 //設定紅外線初始值      (紅外線讀值:白為0，黑為1)
int velocity;                    //車輛速度
long dur,cm,obs;                 //接收間段(us)，公分，障礙
long temp=18;                    //溫度C(聲速受溫度影響)
long w=(331.5+0.607*temp)/1000;  //每微秒幾公分
void setup()
{
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(ir1,INPUT);
  pinMode(ir2,INPUT);
  pinMode(echo, INPUT);
  pinMode(13,OUTPUT);
}
void loop() 
{
  digitalWrite(trig, HIGH);    //超音波發送訊號
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  pinMode(echo, INPUT);        // 讀取 echo 的電位
  dur = pulseIn(echo, HIGH);   // 收到高電位時的時間(接到訊號的間隔)
  cm = (dur/2)*w;              // 將時間換算成距離 cm 
  //  irv1=digitalRead(ir1);
  //  irv2=digitalRead(ir2);

  Serial.print("Distance : ");  // 監控讀值
  Serial.print(cm);
  Serial.print("cm    ");
  Serial.print(w);
  Serial.print("us/cm");
  Serial.println();             //監控讀值

  obs= 15+velocity*1;                 //預估轉彎點(15只是預設，velocity*1也是)
  if(cm<=obs)
  {
    digitalWrite(13,HIGH);          //避障指令
  }

  if(cm>obs)
  {
    if(ir1==HIGH && ir2==LOW)  // 左黑右白
    {
      digitalWrite(11,HIGH);   //左轉指令
    }
    if(ir1==LOW && ir2==HIGH)  // 左白右黑
    {
      digitalWrite(11,LOW);    //右轉指令
    }
   if(ir1==LOW && ir2==LOW)    //雙白(迷途狀況)
   {
      digitalWrite(10,HIGH);   //搜尋路跡指令  
   }
  }
  delay(250);
}
