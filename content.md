# Robotics, Embedded Systems & Artificial Intelligence
Stage 1 & Stage 2 — Instructor handbook and student study material

**TEJEEL INNOVATIONS LLP · Learn. Build. Automate. Innovate.**

This learning portal follows pages 4–8 of the supplied 16-page curriculum. It covers 80 guided hours, ten modules and 33 activities. Stage 1 develops scientific foundations; Stage 2 converts those foundations into programmable physical systems. The student should learn the principle, build, measure, troubleshoot and independently modify a design. Examples use Arduino UNO R3 unless specified. Programs are instructional examples, not hardware-validated commercial firmware. The Zensin mechanism remains undefined in the source.

## Study pathway
| Stage | Module | Hours |
|---|---|---:|
| Explorer | 1. Introduction to robotics and technology | 4 |
| Explorer | 2. Basic electronics | 8 |
| Explorer | 3. Sensors and actuators | 6 |
| Explorer | 4. Motion and mechanical engineering | 10 |
| Explorer | 5. Introduction to controllers | 4 |
| Maker | 6. Programming fundamentals | 8 |
| Maker | 7. Arduino and sensor interfacing | 8 |
| Maker | 8. Motor control and robot construction | 12 |
| Maker | 9. ESP32 and IoT | 8 |
| Maker | 10. Interactive robotics and mini-project | 12 |

Primary references: OpenStax University Physics Volumes 1 and 2; All About Circuits; Lynch and Park, Modern Robotics; NASA Glenn; Arduino; Espressif; Raspberry Pi; Texas Instruments. See the linked reference library at the end. Photographs are extracted from the supplied curriculum; additional vector diagrams are original educational illustrations, not the exact chat image results.

# Stage 1 — Robotics Explorer
32 hours · School and absolute beginner · No prerequisites

![Electronics, mechanisms and motors from the supplied curriculum](assets/stage3-0.jpeg)

## Chapter 1. Introduction to robotics and technology
**4 hours**

A robot is a programmable physical machine designed to perform tasks by interacting with its environment. It may be remotely controlled, autonomous or combine both. Robotics combines mechanical engineering, electronics, computer science, control and sometimes AI. A robot does not need a human shape.

| Subsystem | Role | Human analogy |
|---|---|---|
| Sensors | Detect conditions | Eyes and skin |
| Controller | Process information | Brain |
| Actuators | Produce action | Muscles |
| Power | Supply energy | Food/metabolism |
| Structure | Support components | Skeleton |
| Software | Define behaviour | Instructions |
| Communication | Exchange information | Signalling |
| End effector | Interact with objects | Hand |

{{robot}}

### Robotics, automation and AI
Robotics concerns physical programmable machines. Automation performs tasks with reduced human intervention (e.g. bottle filling). Artificial intelligence uses computational methods for recognition, prediction, planning or learning (e.g. detecting defects in images). A robot may use fixed rules without AI; AI can also exist entirely in software. A threshold-based obstacle avoider is not necessarily an AI robot.

| Robot type | Applications |
|---|---|
| Industrial | Welding, painting, packaging, assembly |
| Humanoid | Research, interaction, experimental automation |
| Mobile | Wheels, tracks or legs; warehouse delivery |
| Aerial | Mapping, inspection, crop monitoring |
| Agricultural | Weeding, harvesting, monitoring, irrigation |
| Medical | Surgical assistance, rehabilitation, logistics |

{{types}}

### Input, process, output and feedback
A temperature sensor measures room temperature; the controller compares it with a target; a fan switches on; the temperature is measured again to correct the action. Open-loop control acts without measuring the result (motor runs five seconds). Closed-loop control measures the result and corrects it (encoder measures wheel motion until a target is reached). Feedback is not necessarily AI.

{{feedback}}

### Engineering design process
Identify problem → define requirements → generate alternatives → select feasible design → prototype → test → improve → document. Ask students to propose a robot for their school. For a dustbin, discuss detection, obstruction, low battery and mechanical improvements before coding.

### Laboratory safety
| Hazard | Rule |
|---|---|
| Short circuit | Disconnect power before rewiring; use current-limited low-voltage supplies |
| Mains | Never connect a breadboard to 230 V AC |
| Batteries | Approved chargers and protected packs; avoid damaged cells and shorts |
| Polarity | Verify supply and component orientation |
| Motors | Avoid prolonged stall, keep fingers and hair away |
| Soldering | Supervision, ventilation, eye protection |
| Capacitors | Safely discharge before handling |
| Water | Separate liquids and energized electronics |
| Flying mechanisms | Paper gliders/simulation, no unsupervised powered propellers |

**Review:** Define robotics, automation and AI. Name five robot types. Explain the robot subsystems, open/closed loop and design steps. Why should motors not be powered by GPIO? Propose a school robot.

## Chapter 2. Basic electronics and electrical engineering
**8 hours**

### Charge, voltage, current and resistance
Atoms contain positive protons, negative electrons and neutral neutrons. Conductors allow charge movement; insulators resist it; semiconductor conductivity is controllable. Conventional current is defined in the direction positive charge would move. In a metal, electrons drift oppositely.

| Quantity | Symbol | Unit | Definition |
|---|---|---|---|
| Charge | Q | C | Amount of charge |
| Voltage | V | V | Energy per charge, V = E/Q |
| Current | I | A | Rate of charge flow, I = Q/t |
| Resistance | R | Ω | Opposition to current, R = ρL/A |
| Power | P | W | Rate of energy transfer |
| Energy | E | J or Wh | Energy transferred |
| Capacitance | C | F | Charge per voltage |
| Inductance | L | H | Magnetic flux linkage per current (linear case) |

### Ohm's law and power
For an ohmic resistor at constant physical conditions, V = IR. A 9 V battery across 1 kΩ gives 9 mA. P = VI = I²R = V²/R for a resistor. A 5 V device drawing 0.2 A uses 1 W and in two hours consumes 2 Wh. Check resistor power ratings before applying voltage.

{{ohm}}

### Circuits
Open circuit: interrupted path. Closed circuit: continuous path. A short circuit is unintended low resistance; excessive current can cause damage. Never short a real battery as a demonstration. Series components carry equal current, Rtotal = R1 + R2 + …; 100 Ω + 200 Ω = 300 Ω. Parallel branches share voltage, 1/Rtotal = 1/R1 + 1/R2 + …; 100 Ω parallel 200 Ω gives 66.67 Ω.

{{circuits}}

### Kirchhoff's laws
KCL: total incoming current equals total outgoing current at a node in ordinary lumped circuit analysis (5 A = 2 A + 3 A). KVL: algebraic voltage sum around a closed lumped DC loop is zero (12 − 4 − 8 = 0). Use these to locate incorrect supply voltages and branch currents.

{{kirchhoff}}

### AC and DC
DC normally flows in one direction (batteries/USB). AC reverses periodically (power distribution). Beginner laboratory supplies must be isolated low-voltage DC.

{{waveforms}}

### Electronic components
| Component | Working principle and uses |
|---|---|
| Resistor | Limits current, divides voltage, establishes bias. Common 220 Ω, 330 Ω, 1 kΩ, 4.7 kΩ, 10 kΩ |
| Capacitor | Stores energy in electric field; Q=CV; filtering, timing, supply stabilization. Observe electrolytic polarity |
| Inductor | Magnetic energy storage, V=L dI/dt; opposes rapid current change; converters and filters |
| Potentiometer | Adjustable resistor, three terminals; voltage divider and control input |
| Diode | Predominantly one-way conduction, rectification and flyback protection; nonlinear semiconductor |
| LED | Emits light when forward biased; needs current limitation |
| Transistor | BJT/MOSFET switching or amplification; allows small signal to control externally supplied load current |
| IC | Multiple devices on a chip; timers, logic, drivers and controllers |

{{components}}

### Resistor colour codes
First two bands represent digits; third multiplier; fourth tolerance. Black 0, brown 1, red 2, orange 3, yellow 4, green 5, blue 6, violet 7, grey 8, white 9. The multiplier is 10 to the power of its digit; gold ×0.1, silver ×0.01. Gold ±5%, silver ±10% in tolerance position. Red-red-brown-gold = 220 Ω ±5%.

{{resistor}}

### LED current limiting
R = (Vs − Vf)/If. For 5 V, red LED Vf≈2 V, target 10 mA: R = 300 Ω; choose 330 Ω standard. Actual LED voltage varies. Anode commonly longer, cathode commonly shorter/flat side; verify datasheet or diode test. Connect supply → resistor → anode → cathode → ground.

{{led}}

### Capacitor charging and discharging
Time constant τ=RC. Charging from zero: Vc=Vs(1−exp(−t/τ)); discharge: Vc=V0 exp(−t/τ). At τ charging reaches 63.2%, at 5τ 99.3%. Applications include filtering, timing and debouncing. Use rated voltage and correct polarity.

{{rc}}

### Voltage divider
Vout=Vin R2/(R1+R2), for negligible output loading. Two 10 kΩ resistors across 5 V give 2.5 V. LDRs and thermistors can form variable dividers. A divider is not a suitable motor power supply.

{{divider}}

### Binary and Boolean logic
A digital value encodes discrete states. Logic HIGH/LOW voltage thresholds depend on the device. Binary 1011 = 8+2+1 = 11. Eight unsigned bits encode 0–255. Four-bit examples: 0=0000, 1=0001, 2=0010, 3=0011, 4=0100, 5=0101, 6=0110, 7=0111, 8=1000, 9=1001, 10=1010, 15=1111.

| A | B | AND | OR | NAND | NOR | XOR | XNOR |
|---|---|---|---|---|---|---|---|
|0|0|0|0|1|1|0|1|
|0|1|0|1|1|0|1|0|
|1|0|0|1|1|0|1|0|
|1|1|1|1|0|0|0|1|

NOT inverts one input. AND requires both conditions, OR any condition, XOR different states, XNOR equal states. NAND/NOR are universal gates. Examples: start AND safety; alarm OR sensor; NOT daylight; XOR discrepancy.

{{logic}}

### Power supplies and batteries
AA packs, USB, regulated bench supplies, rechargeable packs, buck (step down), boost (step up), linear regulators. Battery capacity 2000 mAh / 500 mA gives ideal 4 h; actual runtime varies. A 5 V system with controller 100 mA, sensors 50 mA, motors 600 mA, display 50 mA draws 800 mA normally; design for transient current and motor stall too. Voltage, discharge current, chemistry, protection and charger compatibility matter.

### Breadboard and multimeter
A breadboard connects groups of holes internally. Check the terminal strips and whether supply rails are split. Multimeter: voltage measured in parallel with energized circuit; current in series using correct fused port/range; resistance and continuity on disconnected, discharged circuit; diode mode checks forward voltage. Never place a meter in current mode directly across a supply.

{{breadboard}}

### Laboratory: verify Ohm's law
Use a current-limited supply, 1 kΩ resistor, meter, breadboard and leads. Apply 1–5 V, measure across resistor and in series. Expected currents: 1, 2, 3, 4, 5 mA respectively. Record real readings and plot voltage against current. Discuss tolerance, reference accuracy and uncertainty.

## Chapter 3. Sensors and actuators
**6 hours**

A sensor converts a physical quantity into a measurable signal. An actuator converts energy into physical action.

| Property | Meaning |
|---|---|
| Range | Measurable minimum to maximum |
| Accuracy | Closeness to true value |
| Precision | Repeatability of readings |
| Resolution | Smallest measurable change |
| Sensitivity | Output change per input change |
| Response time | Time to respond |
| Noise | Unwanted variations |
| Calibration | Compare and adjust against reference |
| Hysteresis | Response depends on direction/history |

{{accuracy}}

### Analog and digital signals
Analog outputs vary continuously; digital outputs encode states or measurements. LDR dividers produce analog voltages; DHT sensors transmit digital measurements. Sampling and quantization convert analog values to numeric codes.

{{signals}}

### Sensors and principles
| Sensor | Principle and applications |
|---|---|
| LDR | Light decreases resistance; streetlights, light followers. LDR to supply and fixed resistor to ground gives higher voltage in bright light |
| HC-SR04 | Ultrasonic time-of-flight: d=vt/2, speed of sound ≈343 m/s at 20°C. Angled/soft surfaces and temperature affect results |
| IR reflectance/proximity | Emits IR and senses reflection; line tracking and obstacle detection, calibrate actual materials |
| DHT11/DHT22 | Digital temperature and relative humidity; greenhouse/weather station |
| LM35 | Analog 10 mV/°C nominal; 250 mV ≈25°C within conditions |
| NTC thermistor | Resistance decreases as temperature increases |
| Capacitive touch | Finger changes capacitance; touch lamps and interaction |
| PIR | Changing infrared radiation from moving warm objects; alarms |
| Hall-effect | Magnetic field sensing; speed and position |
| IMU | Accelerometer measures specific force; gyro measures angular velocity; orientation estimation |
| Soil moisture | Capacitive sensing; irrigation, requires soil calibration |
| Microphone | Sound pressure signal or intensity threshold, not speech recognition |
| Pressure sensor | Measures pressure via transduction |

{{ultrasonic}}

### Actuators and motors
LED produces light; buzzer sound; relay switches contacts; DC motor rotation; servo controlled position; stepper discrete rotation; solenoid linear movement; electromagnet magnetic force; pneumatic cylinder compressed-air motion.

A brushed DC motor has stator, rotor/armature, brushes, commutator and shaft. Current in a magnetic field generates force and torque; polarity reversal reverses direction. Back EMF opposes supply, V=IR+Eb in simplified steady state. Startup and stall current may be much greater than running current. Select driver and supply accordingly; do not deliberately stall a motor for prolonged periods.

A positional hobby servo integrates DC motor, gears, position sensor and feedback controller. Typical wires red power, brown/black ground, orange/yellow/white signal (verify actual data). Many use repeating pulses around 20 ms and 1–2 ms pulse width; limits vary. Continuous-rotation servos instead command speed/direction.

{{servo}}

Stepper motor: full step angle = 360°/steps per revolution; 200 steps → 1.8°. Used for printers and positioning; open-loop systems can miss steps without detecting it. Driver must match motor windings and current.

| Motor | Control | Application |
|---|---|---|
| DC | Continuous speed, direction; feedback needed for position | Wheels |
| Servo | Internal closed-loop position, typically limited travel | Joints |
| Stepper | Incremental rotation; often open-loop | Precision positioning |

{{motors}}

Relays have COM, NO and NC contacts. Solenoids move a plunger with a coil. Electromagnets create magnetic fields. Use appropriate driver and flyback diode for unidirectional inductive coils. Pneumatics use regulator, valve, tubing and cylinder; ideal force F=PA, pressure difference times effective area. Demonstrate with air-filled linked syringes, not high-pressure equipment.

Speed (RPM), torque (turning effect), load (mechanical demand), power P=τω. Motor speed generally falls as load increases. Never confuse stall torque with safe continuous torque.

## Chapter 4. Motion and mechanical engineering
**10 hours**

Linear motion follows a line; rotary motion turns about an axis; oscillation repeats angular motion; reciprocation repeats back-and-forth linear motion.

{{motion}}

### Motion equations
Average speed v=d/t; average acceleration a=(v−u)/t; F=ma for constant mass. Angular velocity ω=2πN/60, N in RPM. Rolling without slip gives v=rω. Wheel diameter 65 mm, 100 RPM: circumference 0.2042 m, speed 0.340 m/s ideal. Load and slip affect actual speed.

### Torque
τ=rF sinθ; for perpendicular force τ=rF. For a horizontal arm lifting a mass, F=mg. Arm, gripper, acceleration and friction also contribute. Use continuous torque ratings and safety margins, not stall torque alone.

{{torque}}

### Gears and mechanical transmission
Spur gears for parallel shafts; helical for smoother engagement; bevel for intersecting axes; worm for large reductions; rack and pinion converts rotation to translation; planetary compact reduction. Gear ratio G=driven teeth/driver teeth; output RPM=input RPM/G; output torque≈input torque×G×efficiency. Gears do not create energy. Belt/pulley uses flexible transmission; chain/sprocket engages teeth; lead screw converts rotary to linear motion.

{{gears}}

### Mechanisms
Cam and follower converts rotation into prescribed follower motion. Crank-slider converts rotation into reciprocation (pumps/engines). Four-bar linkage consists of four rigid links including the frame and pivot joints; creates controlled motion in grippers and walking mechanisms. Build with cardboard and pivots first.

{{crank}}
{{linkages}}

### Walking and flight
Walking mechanisms alternate stance (support) and swing (move); gait coordinates legs. For quasi-static stability the centre-of-mass projection should remain within the support polygon. Study Klann/Jansen-style linkages and quadruped motion. For aircraft: lift acts perpendicular to relative airflow, drag opposes it, thrust propels, weight acts downward. In steady level flight lift balances weight and thrust balances drag in a simplified model. Roll, pitch and yaw are rotations about longitudinal, lateral and vertical axes. Use gliders/simulation in beginner labs.

{{flight}}

### Stability, friction and load distribution
A lower centre of mass generally resists tipping. Static friction maximum Fs=μsN; traction enables wheels to move the robot. Weight distribution affects normal forces and traction. Test wheel materials on different surfaces.

{{stability}}

### Robot anatomy
Link: rigid member; joint: relative motion connection; revolute: rotary; prismatic: linear; end effector: tool; workspace: reachable region; payload: designed load; degrees of freedom: independent configuration variables. A base, shoulder and elbow with independent rotary joints give three joint DOF.

{{arm}}

## Chapter 5. Introduction to controllers
**4 hours**

A microprocessor is a programmable processing unit typically requiring external system components. A microcontroller integrates CPU, memory and peripherals for embedded control. CPU fetches, decodes and executes instructions; ALU performs arithmetic/logic; flash stores firmware; RAM temporary data; GPIO inputs/outputs; ADC converts voltage; timers schedule events; clock coordinates timing; communication peripherals exchange data.

{{controller}}

| Board | Type | Logic | Network | Typical use |
|---|---|---|---|---|
| Arduino UNO R3 | ATmega328P MCU | 5 V | No built-in Wi-Fi/Bluetooth | Basic C/C++ embedded control |
| Classic ESP32 DevKit | MCU | 3.3 V | Wi-Fi, Classic Bluetooth, BLE | Wireless IoT and control |
| Raspberry Pi 5 | Single-board computer | 3.3 V GPIO | Wi-Fi, Bluetooth | Linux, Python, vision |

Pi 5 has no built-in general-purpose analog input; add ADC. GPIO is not 5 V tolerant. Raspberry Pi Pico is an MCU, not a Linux SBC. ESP32 variants differ.

Algorithm = defined steps to solve a problem; flowchart represents them graphically. Example: read temperature; if above 30°C turn fan on, otherwise off; repeat. Begin in natural language, translate to pseudocode and then code.

{{flowchart}}

## Stage 1 — 18 practical activities
These are a demonstration bank, not 18 compulsory independent builds. Use low-voltage, supervised experiments. Record aim, components, diagram, principle, procedure, observations, calculations, result, precautions, faults and improvements.

| # | Activity | Components, method and expected result |
|---|---|---|
|1|Fire alarm|Thermistor, comparator, transistor, buzzer; warm sensor safely and verify threshold; not life-safety equipment|
|2|Burglar alarm|Reed switch/button and buzzer; model door opening triggers alarm|
|3|Logic gates|Compatible logic ICs, switches with pull resistors, LEDs/resistors; verify AND OR NOR NAND XOR truth tables|
|4|Metal detection|Low-voltage inductive detector module; move metal near coil and compare response|
|5|Light intensity control|Potentiometer input and PWM module/LED resistor; vary brightness|
|6|Traffic signal|Red/yellow/green LEDs with separate resistors; sequence lights manually or with controller demo|
|7|Touch light|Capacitive touch module and LED; test touch/release|
|8|Night lamp|LDR divider and comparator/transistor; cover LDR and observe threshold|
|9|Water level|Float switches or low-voltage sensor; test levels with isolated power and no wet wiring|
|10|Gear motion|Count teeth and revolutions, compare predicted and observed ratio|
|11|Circular motion|Hand crank/disc and axle; observe rotation and radius|
|12|Flying mechanism|Paper aircraft/foam glider; compare balance and flight distances|
|13|Walking mechanism|Cardboard links, pivots, hand crank; trace foot path|
|14|Aarti mechanism|Unlit model plate; compare circular and oscillatory movement|
|15|Pulley lift|Fixed/movable pulley, light loads; compare effort and travel|
|16|Crank-slider|Disc, connecting rod, slider; measure stroke|
|17|Four-bar linkage|Frame and three moving links; observe range and transmission|
|18|Mechanical gripper|Cardboard/printed links and pivots; test light objects and grip geometry|

# Stage 2 — Robotics Maker
48 hours · Theory, programming and practical application

![Arduino robotics, embedded systems and interactive robots from the supplied curriculum](assets/stage6-0.jpeg)

## Chapter 6. Programming fundamentals
**8 hours**

Install [Arduino IDE](https://www.arduino.cc/en/software), connect USB, select correct board and port, write, verify, upload and observe. Sketch `setup()` executes once after reset, `loop()` repeats. Flowcharts and pseudocode help plan before implementation.

### Blink LED
```cpp
void setup() { pinMode(LED_BUILTIN, OUTPUT); }
void loop() {
  digitalWrite(LED_BUILTIN, HIGH); delay(1000);
  digitalWrite(LED_BUILTIN, LOW); delay(1000);
}
```
`pinMode` configures direction; `digitalWrite` sets state; `delay` pauses in milliseconds. Modify timing and explain each line.

### Variables, types and operators
```cpp
int temperature = 25;
float distance = 15.5;
bool objectDetected = false;
char command = 'F';
const int ledPin = 13;
unsigned long lastTime = 0;
```
`int` integer (typically 16 bits on UNO R3, 32 on ESP32), `float` decimal, `bool` true/false, `char` character, `unsigned long` nonnegative timing value, `const` not modifiable through that name. Arithmetic + − * / %, comparisons == != > < >= <=, logical && || !, assignment = += -=, increments ++ --. Do not confuse assignment and equality.

### Conditions, loops, functions and arrays
```cpp
int temperature = 35;
void setup() { Serial.begin(9600); }
void loop() {
  if (temperature > 30) Serial.println("Fan ON");
  else Serial.println("Fan OFF");
  delay(1000);
}
```
`else if` tests further conditions. `for (int i=0; i<10; i++)` repeats a fixed number; `while (condition)` repeats until false. Uncontrolled loops block responsiveness. Functions isolate reusable behaviour; arrays collect same-type values.
```cpp
const int pins[] = {2, 3, 4};
void blinkLED(int pin, int duration) {
  digitalWrite(pin, HIGH); delay(duration);
  digitalWrite(pin, LOW); delay(duration);
}
void setup() {
  for(int i=0; i<3; i++) pinMode(pins[i], OUTPUT);
}
void loop() {
  for(int i=0; i<3; i++) blinkLED(pins[i], 300);
}
```
Each external LED needs its own current-limiting resistor.

### Serial and debugging
```cpp
void setup() { Serial.begin(9600); }
void loop() {
  Serial.print("Sensor Value: ");
  Serial.println(analogRead(A0));
  delay(500);
}
```
Serial Monitor shows values; Serial Plotter shows changing measurements. Compile errors: syntax/library. Upload errors: board/port/cable. Incorrect sensor: wiring/calibration/reference. Resets: power/noise. Unexpected motor: polarity or control logic. Slow response: blocking code.

### Non-blocking timing
```cpp
unsigned long previousTime=0;
const unsigned long interval=500;
bool ledState=false;
void setup(){pinMode(LED_BUILTIN,OUTPUT);}
void loop(){
  unsigned long now=millis();
  if(now-previousTime>=interval){
    previousTime=now;
    ledState=!ledState;
    digitalWrite(LED_BUILTIN,ledState);
  }
  // Read other sensors here.
}
```
Use unsigned subtraction to tolerate timer rollover. AI-assisted workflow: generate → read → explain → verify hardware and libraries → compile → test → modify. Never upload unreviewed motor code.

## Chapter 7. Arduino and sensor interfacing
**8 hours**

UNO R3: ATmega328P, 16 MHz, 14 digital pins, six analog inputs, PWM pins 3/5/6/9/10/11, 10-bit ADC, 32 KB flash, 2 KB SRAM, 1 KB EEPROM, 5 V logic. Recommended 20 mA per I/O, aggregate limits apply. See [UNO R3 documentation](https://docs.arduino.cc/hardware/uno-rev3/). Motors/pumps need a driver.

### Digital input, pull-ups and debounce
D2 to button to ground; internal pull-up prevents floating state. Open reads HIGH, pressed reads LOW.
```cpp
const int buttonPin=2, ledPin=13;
void setup(){pinMode(buttonPin,INPUT_PULLUP);pinMode(ledPin,OUTPUT);}
void loop(){digitalWrite(ledPin,digitalRead(buttonPin)==LOW);}
```
Mechanical switch contacts bounce. Accept a new state only after it remains stable for a chosen time, e.g. 20–50 ms, calibrated to the switch. [Official debounce example](https://docs.arduino.cc/built-in-examples/digital/Debounce/).

### ADC
10-bit ADC has 1024 codes, 0–1023; ideal step 5/1024≈4.88 mV for 5 V reference. Endpoint approximation voltage=raw×5/1023. Reference voltage, noise and ADC characteristics affect accuracy.
{{adc}}
```cpp
void setup(){Serial.begin(9600);}
void loop(){
  int raw=analogRead(A0);
  Serial.println(raw*5.0/1023.0);
  delay(500);
}
```
### PWM
Duty cycle = Ton/T ×100%. UNO analogWrite produces switching, not a true analog voltage. A value 0–255 controls duty; 127≈50%. LED brightness and motor output depend on circuit dynamics.
{{pwm}}
```cpp
const int ledPin=9;
void setup(){pinMode(ledPin,OUTPUT);}
void loop(){
  for(int b=0;b<=255;b++){analogWrite(ledPin,b);delay(10);}
  for(int b=255;b>=0;b--){analogWrite(ledPin,b);delay(10);}
}
```
### Automatic streetlight and calibration
LDR from 5 V to A0 junction; 10 kΩ from A0 to GND; D9 to 330 Ω resistor to LED anode, cathode to GND. Record dark/bright values, choose threshold between them. If darkness=200 and bright=800, 500 is starting point. Use hysteresis: switch on below 350 and off above 450 to avoid chatter.
```cpp
bool lightOn=false;
void setup(){pinMode(9,OUTPUT);Serial.begin(9600);}
void loop(){
  int value=analogRead(A0); Serial.println(value);
  if(value<350)lightOn=true;
  else if(value>450)lightOn=false;
  digitalWrite(9,lightOn);delay(100);
}
```
### Ultrasonic distance
HC-SR04 VCC→5V, GND→GND, TRIG→D7, ECHO→D8 on UNO. ESP32 requires level reduction on conventional 5 V Echo. Invalid echo must not be treated as a valid distance.
```cpp
const int trigPin=7,echoPin=8;
float readDistance(){
  digitalWrite(trigPin,LOW);delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  unsigned long duration=pulseIn(echoPin,HIGH,30000);
  if(duration==0)return -1;
  return duration*0.0343/2.0;
}
void setup(){pinMode(trigPin,OUTPUT);pinMode(echoPin,INPUT);Serial.begin(9600);}
void loop(){Serial.println(readDistance());delay(100);}
```
### Displays
16×2 LCD displays two lines of characters; SSD1306 OLED draws pixels and text. I2C SDA data, SCL clock; UNO A4/A5. Verify voltage and address; 0x3C common for OLED but not universal. Install Adafruit GFX and SSD1306 libraries. LCD I2C backpacks often use different addresses/libraries.
```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
Adafruit_SSD1306 display(128,64,&Wire,-1);
void setup(){
  if(!display.begin(SSD1306_SWITCHCAPVCC,0x3C)){while(true){}}
  display.clearDisplay();display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);display.setCursor(0,0);
  display.println("TEJEEL");display.display();
}
void loop(){}
```

## Chapter 8. Motor control and robot construction
**12 hours**

### Motor drivers and H-bridge
L298N works for demos but has significant conduction losses. DRV8833 or TB6612FNG are often efficient for suitable small motors. ULN2003 is suitable for compatible unipolar steppers; A4988 for bipolar motors with current limiting. Check motor voltage, stall current, driver thermal ratings and module enable/sleep configuration. H-bridge reverses motor current by switching diagonal pairs; never switch both devices in one leg together. Use commercial protected drivers.
{{hbridge}}

### DC motor and differential drive
DRV8833 compatible module: AIN1 D5, AIN2 D6, BIN1 D9, BIN2 D10; motors to output pairs, VM to suitable external motor supply, common ground with UNO. Enable as required. Test on blocks before floor operation. `drive` values are PWM commands, not measured wheel velocity. Motor orientation may need reversal.
```cpp
const int L1=5,L2=6,R1=9,R2=10;
void setMotor(int p1,int p2,int speedValue){
  speedValue=constrain(speedValue,-255,255);
  if(speedValue>=0){digitalWrite(p2,LOW);analogWrite(p1,speedValue);}
  else{digitalWrite(p1,LOW);analogWrite(p2,-speedValue);}
}
void drive(int left,int right){setMotor(L1,L2,left);setMotor(R1,R2,right);}
void stopRobot(){drive(0,0);}
void setup(){pinMode(L1,OUTPUT);pinMode(L2,OUTPUT);pinMode(R1,OUTPUT);pinMode(R2,OUTPUT);stopRobot();}
void loop(){
  drive(150,150);delay(1500);stopRobot();delay(300);
  drive(-120,120);delay(500);stopRobot();delay(300);
}
```
One motor alone: use setMotor(5,6,150), then stop with zero and reverse with −150. A positional servo uses external regulated supply, common ground, signal D9, verified safe travel.
```cpp
#include <Servo.h>
Servo arm;
void setup(){arm.attach(9);}
void loop(){arm.write(30);delay(1000);arm.write(90);delay(1000);arm.write(150);delay(1000);}
```
Stepper example: compatible 28BYJ-48 and ULN2003; external rated power and common ground; IN1–IN4 to 8,9,10,11. Effective steps per revolution vary with gearbox, calibrate.
```cpp
#include <Stepper.h>
const int stepsPerRevolution=2048;
Stepper motor(stepsPerRevolution,8,10,9,11);
void setup(){motor.setSpeed(8);}
void loop(){motor.step(stepsPerRevolution);delay(1000);motor.step(-stepsPerRevolution);delay(1000);}
```
Differential-drive equations v=(vR+vL)/2 and ω=(vR−vL)/L where L is track width. Equal forward velocities give forward; left slower gives left turn; opposite velocities rotate on spot. Build a chassis with two driven wheels and caster; place battery low and secure wires.
{{drive}}

### Obstacle avoidance
Combine `readDistance()` and its pin setup from Chapter 7 with the motor functions and pin setup above. Replace the original loop. Invalid readings stop the robot. This is reactive rule-based autonomy, not mapping or AI.
```cpp
void loop(){
  float d=readDistance();
  if(d<0)stopRobot();
  else if(d<20){stopRobot();delay(150);drive(-120,120);delay(350);stopRobot();}
  else drive(140,140);
  delay(50);
}
```
### Line follower
Two IR reflectance sensors at D2/D3, configured INPUT; calibrate output polarity. Assumes both see wide black line when centred. Both black → forward; left only → left; right only → right; neither → stop/search. Adjust speed, sensor spacing, track width and ambient lighting.
```cpp
// Combine with motor functions and pin setup above.
void loop(){
  bool l=digitalRead(2)==LOW,r=digitalRead(3)==LOW;
  if(l&&r)drive(140,140);
  else if(l)drive(50,140);
  else if(r)drive(140,50);
  else stopRobot();
}
```

## Chapter 9. ESP32 and Internet of Things
**8 hours**

ESP32 chips integrate CPU, memory, GPIO, ADC, PWM, timers and interfaces such as UART, SPI and I2C. Classic ESP32 has Wi-Fi, Bluetooth Classic and BLE. C3 has Wi-Fi/BLE and RISC-V; S3 has Wi-Fi/BLE; C3/S3 do not support Classic BluetoothSerial. Verify exact board pinout, boot pins and voltage. ESP32 logic is normally 3.3 V, not 5 V tolerant.

Install Espressif boards package via Arduino Boards Manager and select exact board. [Official getting started](https://docs.espressif.com/projects/arduino-esp32/en/latest/getting_started.html).

### Wi-Fi
Station mode joins a router; access point mode provides a local network. Never expose robot commands publicly without protection. Connection example:
```cpp
#include <WiFi.h>
const char* ssid="YOUR_WIFI";
const char* password="YOUR_PASSWORD";
void setup(){
  Serial.begin(115200);WiFi.begin(ssid,password);
  unsigned long start=millis();
  while(WiFi.status()!=WL_CONNECTED && millis()-start<15000){delay(250);Serial.print(".");}
  if(WiFi.status()==WL_CONNECTED)Serial.println(WiFi.localIP());
  else Serial.println("Connection failed");
}
void loop(){}
```
### Bluetooth and ESP-NOW
Bluetooth Classic supports serial-like exchange on compatible chips; BLE uses services and characteristics. RC phone command F/B/L/R/S maps to movement; validate commands and stop if valid messages cease. ESP-NOW exchanges packets directly without conventional router association. Register peers using MAC, match radio channels, validate length/source/range, use callbacks and a timeout. API signatures vary by board-package version; use [official ESP-NOW examples](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/espnow.html).
```cpp
struct ControlPacket { uint8_t command; uint8_t speedValue; };
// Receiver: after validating a packet, update lastValidPacket.
// In loop, if (millis()-lastValidPacket > 500) stopRobot();
```
Start with a stopped receiver; stop after lost connection and require a fresh valid command. Do not treat an uninitialized timestamp as a command.
{{wireless}}

### IoT architecture and protocols
Sensor → ESP32 → network/server → dashboard → authorized control → actuator. HTTP request-response; HTTPS adds TLS; MQTT lightweight publish-subscribe broker; WebSocket bidirectional persistent connection; BLE short-range; ESP-NOW direct device packets. MQTT publisher sends to topics, subscriber receives, broker routes. Example topics `tejeel/lab/robot01/temperature`, `/distance`, `/command`, `/status`. Use Serial Plotter, local web dashboards, Node-RED and MQTT. A dashboard visualizes readings; it does not automatically make a system secure.
{{iot}}
{{dashboard}}

Security: authentication, protect credentials, validate data, avoid public unrestricted interfaces, use encryption where supported, stop on communication timeout. Do not publish passwords in repositories.

## Chapter 10. Interactive robotics and mini-projects
**12 hours**

Animatronics reproduces lifelike movement with mechanisms, motors, electronics and software. Begin with hand and neck, not full humanoid locomotion. Use calibrated servo limits and suitable external power with common ground. Servo library on UNO can interfere with timer-based PWM on D9/D10.
```cpp
#include <Servo.h>
Servo hand,neck;
void setup(){hand.attach(9);neck.attach(10);hand.write(90);neck.write(90);}
void loop(){
  neck.write(60);delay(500);
  for(int i=0;i<3;i++){hand.write(60);delay(350);hand.write(120);delay(350);}
  hand.write(90);neck.write(90);delay(2000);
}
```
### State machines and sequential motion
A state machine defines distinct operating modes and transitions. Greeting: idle → detect → wave → return → idle. Dustbin: closed/opening/open/closing. Traffic: red/green/yellow. Robot: idle/forward/turn/stop. Irrigation: monitoring/watering/fault. Prefer non-blocking timers when safety or sensors must be checked continuously.
{{states}}

### Smart dustbin
Combine the complete `readDistance()` function from Chapter 7 with this example (remove its original setup/loop). Use lightweight model lid, safe endpoints, external servo supply and common ground. Invalid distance leaves lid unchanged; production needs obstruction sensing and fault handling.
```cpp
#include <Servo.h>
Servo lid;
// Include trigPin, echoPin and readDistance() from Chapter 7.
bool lidOpen=false;
unsigned long lastDetection=0;
void setup(){pinMode(trigPin,OUTPUT);pinMode(echoPin,INPUT);lid.attach(9);lid.write(20);}
void loop(){
  float d=readDistance();
  if(d>0 && d<20){lastDetection=millis();if(!lidOpen){lid.write(100);lidOpen=true;}}
  else if(lidOpen && d>=20 && millis()-lastDetection>3000){lid.write(20);lidOpen=false;}
  delay(60);
}
```
### Sound/light and integration
Microphone modules detect intensity/threshold, not speech understanding. RGB LED combines red/green/blue channels, each with suitable current limiting; verify common anode/cathode. Test power first, sensors individually, actuators, communication and finally integration. Record faults and improvements.

| Symptom | Investigate |
|---|---|
| Servo shakes | Supply transients, binding, commands |
| Controller resets | Voltage drop, noise, wiring |
| ESP32 connection fails | Credentials, radio channel, board selection |
| Moves backwards | Polarity/direction mapping |
| Line lost | Calibration, speed, spacing, lighting |
| Ultrasonic fluctuates | Angled surfaces, interference, invalid echo |
| Driver hot | Stall, excessive current, thermal limits |
| RC keeps moving | Missing timeout or stale packets |
| Slow response | Blocking delay or processing |

## Stage 2 — 15 practical projects
Four guided builds and one independently modified mini-project are mandatory. The following are choices, not 15 mandatory full builds. For each, document circuit, code, BOM, observations, test results and one independently implemented improvement.

| # | Project | Hardware / implementation / test |
|---|---|---|
|1|Sensor monitoring|UNO, LDR and temperature sensor; log and calibrate readings; compare references|
|2|Motor and motion|DC, servo and stepper with appropriate drivers; test direction, speed, safe positions|
|3|Automatic streetlight|LDR divider, LED, thresholds and PWM; test light/dark and hysteresis|
|4|Smart dustbin|Ultrasonic, lightweight servo lid; test opening, timing and invalid readings|
|5|Line follower|Two reflectance sensors, chassis and driver; tune threshold/speed and measure track completion|
|6|Obstacle avoider|Ultrasonic and chassis; test safe stopping and turning; invalid readings stop|
|7|Bluetooth/Wi-Fi RC car|ESP32 and smartphone control; validate command and stop on lost link|
|8|ESP-NOW RC car|Two ESP32s, buttons/joystick, matching packets; test link timeout|
|9|Smart irrigation|Capacitive soil probe, low-voltage pump and driver; calibrate dry/wet, limit run time, keep water isolated|
|10|IoT weather station|ESP32, DHT22 and OLED; publish temperature/humidity; verify dashboard and offline behaviour|
|11|Automatic Aarti|Geared motor and unlit plate; timed circular motion and stable mount|
|12|Waving robot|Hand/neck servos, proximity trigger; verify endpoints, sequence and power|
|13|Zensin mechanism|Undefined in source; require drawing, purpose and motion description before design or code|
|14|Password door lock|Keypad, controller, servo model lock; validate entries, incorrect codes and timeout; not a real security system|
|15|Railway gate model|Two train sensors, warning LEDs, servo barrier and state logic; simulated model only, never real railway operation|

{{projects}}

## Teaching schedule — 80 hours
| Session | Hours | Topic |
|---|---:|---|
|1|4|Robotics, applications, safety and engineering design|
|2|4|Voltage, current, resistance, Ohm's law|
|3|4|Components, circuits, logic, instruments|
|4|4|Sensors and measurement|
|5|4|Actuators and introduction to motion|
|6|4|Torque, gears, transmission|
|7|4|Linkages, walking, flight and anatomy|
|8|4|Controllers and algorithms|
|9|4|IDE, variables, basic programs|
|10|4|Conditions, loops, arrays, functions, debugging|
|11|4|Digital input/output, ADC and PWM|
|12|4|Sensors, calibration and displays|
|13|4|DC motors, drivers and H-bridge|
|14|4|Servos, steppers and chassis|
|15|4|Line-following and obstacle avoidance|
|16|4|ESP32, Wi-Fi and Bluetooth|
|17|4|ESP-NOW, dashboards and security|
|18|4|Animatronics and multiple servos|
|19|4|State machines and integration|
|20|4|Independent project, testing and assessment|

## Assessment and viva
{{quiz}}

| Stage 1 descriptive | Stage 2 descriptive |
|---|---|
|Explain Ohm's law and example|Explain setup and loop|
|Series vs parallel|ADC vs PWM|
|KCL and KVL|Pull-ups and debounce|
|Resistor colours|Blink LED code|
|Transistor switching|Ultrasonic calculation|
|Capacitor charging|H-bridge control|
|DC vs servo vs stepper|Differential drive|
|Gear ratio and torque|Wi-Fi vs BLE vs ESP-NOW|
|Four-bar linkage|State machines|
|Flight forces|Calibration and hysteresis|
|Degrees of freedom|Communication fail-safe|
|MCU vs processor|Troubleshoot a robot|

## Reference library
Recommended books for deeper instructor study (not reproduced): Paul Horowitz and Winfield Hill, *The Art of Electronics*; Paul Scherz and Simon Monk, *Practical Electronics for Inventors*; R. S. Khurmi and J. K. Gupta, *Theory of Machines*; Michael Margolis et al., *Arduino Cookbook*.

| Source | Link and purpose |
|---|---|
|OpenStax University Physics 1|[Mechanics](https://openstax.org/details/books/university-physics-volume-1)|
|OpenStax University Physics 2|[Electricity and magnetism](https://openstax.org/details/books/university-physics-volume-2)|
|All About Circuits|[Electrical engineering textbook](https://www.allaboutcircuits.com/textbook/)|
|Lynch & Park|[Modern Robotics book resources](https://modernrobotics.northwestern.edu/nu-gm-book-resource/)|
|NASA|[Four Forces of Flight](https://www.nasa.gov/stem-content/four-forces-of-flight/)|
|Arduino|[Hardware and tutorials](https://docs.arduino.cc/)|
|Arduino|[Language reference](https://docs.arduino.cc/language-reference/)|
|Arduino|[Built-in examples](https://docs.arduino.cc/built-in-examples/)|
|Espressif|[Arduino ESP32 documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/)|
|Espressif|[ESP-NOW API](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/espnow.html)|
|Raspberry Pi|[Official documentation](https://www.raspberrypi.com/documentation/)|
|Texas Instruments|[DRV8833 datasheet](https://www.ti.com/product/DRV8833)|
|Wokwi|[Virtual electronics lab](https://wokwi.com/)|
|Tinkercad|[Circuits simulation](https://www.tinkercad.com/circuits)|

## Final competency checklist
Demonstrate independently before Stage 3. Your progress is saved on this browser. Completion of this checklist is not an official certification assessment.
{{checklist}}

Instructor note: maintain separate theory, laboratory and programming resources as the course grows. The material covers all ten modules and addresses all 33 activities; complete project-specific schematics, hardware-tested firmware and validated laboratory procedures are still required for an institutional laboratory manual.
