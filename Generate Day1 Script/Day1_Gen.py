
name = input('What is your nickname? ')
monitor = input('What is your monitor number? ')
cam_6 = input('What is the MAC ADDRESS of the CAMERA on fa0/6? ')
cam_8 = input('What is the MAC ADDRESS of the CAMERA on fa0/8? ')
ephone_5 = input('What is the MAC ADDRESS of the EPHONE on fa0/5? ')
ephone_7 = input('What is the MAC ADDRESS of the EPHONE on fa0/7? ')

with open(f'day1-{name}-{monitor}.txt', 'w') as file:
    file.write(f'''

! Monitor Num:      {monitor}
! Cam6 Mac Add:     {cam_6}
! Cam8 Mac Add:     {cam_8}
! Ephone 1 Mac:     {ephone_5}
! Ephone 2 Mac:     {ephone_7}


Know the following commands:
 - SR:		show run
 - SS:		show start
 - CRS:		copy run start
 - SPI:		show power inline
 - SIIB:	show ip interface brief
 - SVB:		show vlan brief
 - SIDB:	show ip dhcp binding
 - SMAC:	show mac address-table
 - SVPS:	show voice port summary
 - SDPVS:	show dial-peer voice summary
 - CS:		csim start [potsnum]
 
************** Day 1 Configuration **************
 
!@coreTaas
conf t
 hostname coreTaas-{monitor}
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int vlan 1
  no shut
  ip add 10.{monitor}.1.2 255.255.255.0
  desc VLANMGMTDATA
 int vlan 10
  no shut
  ip add 10.{monitor}.10.2 255.255.255.0
  desc VLANMGMTWIFI
 int vlan 50
  no shut
  ip add 10.{monitor}.50.2 255.255.255.0
  desc VLANMGMTCCTV
 int vlan 100
  no shut
  ip add 10.{monitor}.100.2 255.255.255.0
  desc VLANMGMTVOICE
 end

!@coreBaba
conf t
 hostname coreBaba-{monitor}
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int gi 0/1
  no shut
  no switchport
  ip add 10.{monitor}.{monitor}.4 255.255.255.0
 int vlan 1
  no shut
  ip add 10.{monitor}.1.4 255.255.255.0
  desc VLANMGMTDATA
 int vlan 10
  no shut
  ip add 10.{monitor}.10.4 255.255.255.0
  desc VLANMGMTWIFI
 int vlan 50
  no shut
  ip add 10.{monitor}.50.4 255.255.255.0
  desc VLANMGMTCCTV
 int vlan 100
  no shut
  ip add 10.{monitor}.100.4 255.255.255.0
  desc VLANMGMTVOICE
 end

!@dhcp
conf t
 ip dhcp excluded-add 10.{monitor}.1.1 10.{monitor}.1.100
 ip dhcp excluded-add 10.{monitor}.10.1 10.{monitor}.10.100
 ip dhcp excluded-add 10.{monitor}.50.1 10.{monitor}.50.100
 ip dhcp excluded-add 10.{monitor}.100.1 10.{monitor}.100.100

 ip dhcp pool POOLDATA
  network 10.{monitor}.1.0 255.255.255.0
  default-router 10.{monitor}.1.4
  domain-name MGMTDATA.COM
  dns-server 10.{monitor}.1.10
 ip dhcp pool POOLWIFI
  network 10.{monitor}.10.0 255.255.255.0
  default-router 10.{monitor}.10.4
  domain-name WIFIDATA.COM
  dns-server 10.{monitor}.1.10
 ip dhcp pool POOLCCTV
  network 10.{monitor}.50.0 255.255.255.0
  default-router 10.{monitor}.50.4
  domain-name CCTVDATA.COM
  dns-server 10.{monitor}.1.10
 ip dhcp pool POOLVOICE
  network 10.{monitor}.100.0 255.255.255.0
  default-router 10.{monitor}.100.4
  domain-name VOICEDATA.COM
  dns-server 10.{monitor}.1.10
  option 150 ip 10.{monitor}.100.8
 end

!@switchport
conf t
 vlan 10
  name WIFIVLAN
 vlan 50
  name CCTVVLAN
 vlan 100
  name VOICEVLAN
 int fa 0/2
  switchport mode access
  switchport access vlan 10
 int fa 0/4
  switchport mode access
  switchport access vlan 10
 int fa 0/6
  switchport mode access
  switchport access vlan 50
 int fa 0/8
  switchport mode access
  switchport access vlan 50
 int fa 0/3
  switchport mode access
  switchport access vlan 100
 int fa 0/5
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
  mls qos trust device cisco-phone
 int fa 0/7
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
  mls qos trust device cisco-phone
 end

!@camera
conf t
 ip routing
 ip dhcp pool CAMERA6
  host 10.{monitor}.50.6 255.255.255.0
  client-identifier {cam_6}
 ip dhcp pool CAMERA8
  host 10.{monitor}.50.8 255.255.255.0
  client-identifier {cam_8}
 end

!@default route Corebaba
conf t 
ip routing
ip route 0.0.0.0 0.0.0.0 10.{monitor}.{monitor}.1 254
end

!@ospf routing corebaba
conf t
router ospf 1
router-id 10.{monitor}.{monitor}.4
network 10.{monitor}.0.0 0.0.255.255 area 0
int gi 0/1
ip ospf network point-to-point
end


!@CUCM
conf t
 hostname CUCM-{monitor}
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int fa 0/0
  no shut
  ip add 10.{monitor}.100.8 255.255.255.0
 end

!@alog & ephone
conf t
 dial-peer voice 1 pots
  destination-pattern {monitor}00
  port 0/0/0
 dial-peer voice 2 pots
  destination-pattern {monitor}01
  port 0/0/1
 dial-peer voice 3 pots
  destination-pattern {monitor}02
  port 0/0/2
 dial-peer voice 4 pots
  destination-pattern {monitor}03
  port 0/0/3
 end

conf t
 no telephony-service
 telephony-service
  no auto assign
  no auto-reg-ephone
  max-ephones 5
  max-dn 20
  ip source-address 10.{monitor}.100.8 port 2000
  create cnf-files
 ephone-dn 1
  number {monitor}11
 ephone-dn 2
  number {monitor}22
 ephone-dn 3
  number {monitor}33
 ephone-dn 4
  number {monitor}44
 ephone-dn 5
  number {monitor}55
 ephone-dn 6
  number {monitor}66
 ephone-dn 7
  number {monitor}77
 ephone-dn 8
  number {monitor}88
 ephone 1
  mac-address {ephone_5}
  type 8945
  button 1:1 2:2 3:3 4:4
  restart
 ephone 2
  mac-address {ephone_7}
  type 8945
  button 1:5 2:6 3:7 4:8
  restart
 end

!@video call
conf t
 ephone 1
  video
  voice service voip
  h323
  call start slow
 ephone 2
  video
  voice service voip
  h323
  call start slow
end

!@incoming and outgoing
conf t
 voice service voip
 ip address trusted list
 ipv4 0.0.0.0 0.0.0.0
 end

conf t
 dial-peer voice 11 Voip
  destination-pattern 11..
  session target ipv4:10.11.100.8
  codec g711ULAW
 dial-peer voice 12 Voip
  destination-pattern 12..
  session target ipv4:10.12.100.8
  codec g711ULAW
 dial-peer voice 21 Voip
  destination-pattern 21..
  session target ipv4:10.21.100.8
  codec g711ULAW
 dial-peer voice 22 Voip
  destination-pattern 22..
  session target ipv4:10.22.100.8
  codec g711ULAW
 dial-peer voice 31 Voip
  destination-pattern 31..
  session target ipv4:10.31.100.8
  codec g711ULAW
 dial-peer voice 32 Voip
  destination-pattern 32..
  session target ipv4:10.32.100.8
  codec g711ULAW
 dial-peer voice 41 Voip
  destination-pattern 41..
  session target ipv4:10.41.100.8
  codec g711ULAW
 dial-peer voice 42 Voip
  destination-pattern 42..
  session target ipv4:10.42.100.8
  codec g711ULAW
 dial-peer voice 51 Voip
  destination-pattern 51..
  session target ipv4:10.51.100.8
  codec g711ULAW
 dial-peer voice 52 Voip
  destination-pattern 52..
  session target ipv4:10.52.100.8
  codec g711ULAW
 dial-peer voice 61 Voip
  destination-pattern 61..
  session target ipv4:10.61.100.8
  codec g711ULAW
 dial-peer voice 62 Voip
  destination-pattern 62..
  session target ipv4:10.62.100.8
  codec g711ULAW
 dial-peer voice 71 Voip
  destination-pattern 71..
  session target ipv4:10.71.100.8
  codec g711ULAW
 dial-peer voice 72 Voip
  destination-pattern 72..
  session target ipv4:10.72.100.8
  codec g711ULAW
 dial-peer voice 81 Voip
  destination-pattern 81..
  session target ipv4:10.81.100.8
  codec g711ULAW
 dial-peer voice 82 Voip
  destination-pattern 82..
  session target ipv4:10.82.100.8
  codec g711ULAW
 end

!@default route CUCM
conf t
 ip routing
 ip route 0.0.0.0 0.0.0.0 10.{monitor}.100.4 254
 end

!@ospf routing cucm
conf t
router ospf 1
router-id 10.{monitor}.100.8
network 10.{monitor}.100.0 0.0.0.255 area 0
end


!@EDGE
conf t
 hostname EDGE-{monitor}
 enable secret pass
 service password-encryption
 no logging console
 no ip domain-lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int gi 0/0/0
  no shut
  ip add 10.{monitor}.{monitor}.1 255.255.255.0
  desc INSIDE
 int gi 0/0/1
  no shut
  ip add 200.0.0.{monitor} 255.255.255.0
  desc OUTSIDE
 int loopback 0
  ip add {monitor}.0.0.1 255.255.255.255
  desc VIRTUALIP
 end

!@static routing
conf t
 ip routing
 ip route 10.11.0.0 255.255.0.0 200.0.0.11 254
 ip route 10.12.0.0 255.255.0.0 200.0.0.12 254
 ip route 10.21.0.0 255.255.0.0 200.0.0.21 254
 ip route 10.22.0.0 255.255.0.0 200.0.0.22 254
 ip route 10.31.0.0 255.255.0.0 200.0.0.31 254
 ip route 10.32.0.0 255.255.0.0 200.0.0.32 254
 ip route 10.41.0.0 255.255.0.0 200.0.0.41 254
 ip route 10.42.0.0 255.255.0.0 200.0.0.42 254
 ip route 10.51.0.0 255.255.0.0 200.0.0.51 254
 ip route 10.52.0.0 255.255.0.0 200.0.0.52 254
 ip route 10.61.0.0 255.255.0.0 200.0.0.61 254
 ip route 10.62.0.0 255.255.0.0 200.0.0.62 254
 ip route 10.71.0.0 255.255.0.0 200.0.0.71 254
 ip route 10.72.0.0 255.255.0.0 200.0.0.72 254
 ip route 10.81.0.0 255.255.0.0 200.0.0.81 254
 ip route 10.82.0.0 255.255.0.0 200.0.0.82 254
 ip route 10.{monitor}.0.0 255.255.0.0 10.{monitor}.{monitor}.4 254
 end

!@ospf routing edge
conf t
router ospf 1
router-id {monitor}.0.0.1
network 200.0.0.0 0.0.0.255 area 0
network 10.{monitor}.{monitor}.0 0.0.0.255 area 0
network {monitor}.0.0.1 0.0.0.0 area 0
int gi 0/0/0
ip ospf network point-to-point
end

!@windowsCMD
route  add   10.0.0.0   mask   255.0.0.0    10.{monitor}.1.4
route  add  200.0.0.0   mask  255.255.255.0   10.{monitor}.1.4
 

************** OSPF Routing Only **************

!OSPF routing
!@edge
conf t
router ospf 1
router-id {monitor}.0.0.1
network 200.0.0.0 0.0.0.255 area 0
network 10.{monitor}.{monitor}.0 0.0.0.255 area 0
network {monitor}.0.0.1 0.0.0.0 area 0
int gi 0/0/0
ip ospf network point-to-point
end

!@coreBaba
conf t
router ospf 1
router-id 10.{monitor}.{monitor}.4
network 10.{monitor}.0.0 0.0.255.255 area 0
int gi 0/1
ip ospf network point-to-point
end

!@cucm
conf t
router ospf 1
router-id 10.{monitor}.100.8
network 10.{monitor}.100.0 0.0.0.255 area 0
end


************** Trunking and Etherchannel **************

!@coreBaba, coreTaas
conf t
 int range fa0/10-12
  switchport trunk encapsulation dot1q
  switchport mode trunk
  channel-group 1 mode active
  channel-protocol lacp
  end

************** VOIP Services **************

!@cucm - Interactive Voice Response System
config t
dial-peer voice 69 voip
 service rivanaa out-bound
 destination-pattern {monitor}69
 session target ipv4:10.{monitor}.100.8
 incoming called-number {monitor}69
 dtmf-relay h245-alphanumeric
 codec g711ulaw
 no vad
!
telephony-service
 moh "flash:/en_bacd_music_on_hold.au"
!
application
 service rivanaa flash:app-b-acd-aa-3.0.0.2.tcl
  paramspace english index 1        
  param number-of-hunt-grps 2
  param dial-by-extension-option 8
  param handoff-string rivanaa
  param welcome-prompt flash:en_bacd_welcome.au
  paramspace english language en
  param call-retry-timer 15
  param service-name rivanqueue
  paramspace english location flash:
  param second-greeting-time 60
  param max-time-vm-retry 2
  param voice-mail 1234
  param max-time-call-retry 700
  param aa-pilot {monitor}69
 service rivanqueue flash:app-b-acd-3.0.0.2.tcl
  param queue-len 15
  param aa-hunt1 {monitor}00
  param aa-hunt2 {monitor}77
  param aa-hunt3 {monitor}01
  param aa-hunt4 {monitor}33
  param queue-manager-debugs 1
  param number-of-hunt-grps 4
  end

               ''')

print(f'''
Script generation complete!
View the file \'day1-{name}-{monitor}.txt\'
''')
