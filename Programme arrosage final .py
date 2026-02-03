"""
Interface: microbit
Nom du projet: Nouveau projet
Description: 
Toolbox: vittascience
Mode: blocks

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="-138" y="-1887"><statement name="DO"><block type="controls_if" id="L3{4w.ipPk%6=(?[n.Q,"><mutation else="1"></mutation><value name="IF0"><block type="logic_operation" id="0)i.x)%^B[b@?f)#iTWA"><field name="OP">AND</field><value name="A"><block type="logic_compare" id="ewHQhuZ%~`=OAXrj^4im"><field name="OP">LT</field><value name="A"><block type="sensors_getGroveMoisture" id=";A7xQ0N70}2!9E*_AvJ,"><field name="PIN">pin1</field></block></value><value name="B"><shadow type="math_number" id="BIVqTIyb?Na17Q}Dlh2?"><field name="NUM">250</field></shadow></value></block></value><value name="B"><block type="logic_compare" id="1/w@8rRUn=hl_wpO0d^."><field name="OP">GT</field><value name="A"><block type="sensors_getWaterLevel" id="h~o6o2{^`0795zSfU8!^"></block></value><value name="B"><shadow type="math_number" id="J1pfYr0N,U0CRXhDv)lQ"><field name="NUM">20</field></shadow></value></block></value></block></value><statement name="DO0"><block type="actuators_setGroveRelayState" id="QB)#MZ3Yn|Ax!SM/7s4_"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="RqS5+Re:{sDfUe_F;_t2"><field name="BOOL">HIGH</field></shadow></value><next><block type="display_setGroveSocketLed" id="nF`|IA[e-z0DEmq$#n!e"><field name="PIN">pin0</field><value name="STATE"><shadow type="io_digital_signal" id="+];rrMC7ibI[|zWtT{=i"><field name="BOOL">HIGH</field></shadow></value><next><block type="io_waitUntil" id="q0g}cU-1Z($OSa]E4_=?"><value name="UNTIL"><block type="logic_compare" id="8gaeR_kl3n4qRD#0PB94"><field name="OP">GT</field><value name="A"><block type="sensors_getGroveMoisture" id="/7=GH3RS`CDaAoBBb8]0"><field name="PIN">pin1</field></block></value><value name="B"><shadow type="math_number" id="-n7kaLV^;TAc=#8pbx*/"><field name="NUM">325</field></shadow></value></block></value><next><block type="actuators_setGroveRelayState" id="oMT2NI)(bbo|I,Caj5Jj"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="L(,0n$R73Tx_%}e*Qcsm"><field name="BOOL">LOW</field></shadow></value></block></next></block></next></block></next></block></statement><statement name="ELSE"><block type="display_setGroveSocketLed" id="fncroIyy7YX/S8qSgsSd"><field name="PIN">pin0</field><value name="STATE"><shadow type="io_digital_signal" id="F1Zt+PgR!Td[Aa+f%ilf"><field name="BOOL">LOW</field></shadow></value><next><block type="display_setGroveSocketLed" id="IniI}WT#hnB_J3!8%$q@"><field name="PIN">pin14</field><value name="STATE"><shadow type="io_digital_signal" id=";$Dm?rLj*eAS@;?_V;j5"><field name="BOOL">HIGH</field></shadow></value><next><block type="io_waitUntil" id="LYriDT+Ox8CcoZ}UL+:*"><value name="UNTIL"><block type="logic_compare" id="gKa8G1xsu+bm2@oh0X?c"><field name="OP">GT</field><value name="A"><block type="sensors_getWaterLevel" id="XOQZ2@xk$lvz84JT0r]E"></block></value><value name="B"><shadow type="math_number" id="-ie@LoSqda`le;]qtE+j"><field name="NUM">80</field></shadow></value></block></value><next><block type="display_setGroveSocketLed" id="OB1DA3:5h_G!8/plL!L+"><field name="PIN">pin14</field><value name="STATE"><shadow type="io_digital_signal" id="wlxLf*A~eU[V,C@EO5L-"><field name="BOOL">LOW</field></shadow></value><next><block type="actuators_setGroveRelayState" id="o,[BEl%sSeWA380Tj,U%"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="8K5gnJ7eY,1[bDgjmCt4"><field name="BOOL">HIGH</field></shadow></value></block></next></block></next></block></next></block></next></block></statement></block></statement></block><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="-213" y="-1088"></block></xml>

Projet généré par Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/microbit

"""

from microbit import *
import water_level as waterLevelSensor

# Moisture Sensor on pin1
# LED Module on pin0
# LED Module on pin14

while True:
  if pin1.read_analog() < 250 and waterLevelSensor.check_water_level() > 20:
    pin2.write_digital(1)
    pin0.write_digital(1)
    while not (pin1.read_analog() > 325):
      pass
    pin2.write_digital(0)
  else:
    pin0.write_digital(0)
    pin14.write_digital(1)
    while not (waterLevelSensor.check_water_level() > 80):
      pass
    pin14.write_digital(0)
    pin2.write_digital(1)
