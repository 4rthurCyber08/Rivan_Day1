
<!-- Your monitor number = #$34T# -->

# 👋 Welcome to Rivan
*"There's no better teacher than experience"*


&nbsp;
## 💡 Approach to Network Programmability
*"A new era for Cisco Certifications"*

Cisco Certified Network Automation

- Powershell, Bash
- Python, Ruby, TCL
- JSON, YAML
- REST APIs
- Ansible, Terraform, Chef, Puppet, etc.
- Collaboration Platforms (GitHub)

<br>
<br>

---
&nbsp;

## 📋 Prove what you are doing.
 - Create a Github account: https://github.com/
 - Create a Postman account: https://www.postman.com/

Import the repositories.
 - Rivan_Day1 : https://github.com/art-stacks/Rivan_Day1

<br>
<br>

---
&nbsp;

## 📂 Create your own folder in the desktop
~~~
@cmd
cd Desktop
mkdir _name-#$34T#
cd _name-#$34T#
dir
~~~

<br>
<br>

# 💻 Build your network. 

![Day1](img/Day1_100.png)

<br>
<br>

---
&nbsp;

## 🧱 Hierarchical Network Design
  *What is the most important part of a network? __The Core__*

<br>

Most common kinds of network architectures.
 - 2-tier                 __Cisco Collapsed Campus Core__
 - 3-tier                 __Enterprise Network Design__
 - Spine-leaf             __Data Center Fabric__

<br>

CORE Layer (__CoreTAAS__ & __CoreBABA__) - High Speed and Availability
  > [!NOTE]
  >*"A Network Engineer MUST avoid a single point of failure.
   __Always have a backup.__"*

<br>

Examples:
  | __Protocol__                 | __Supported Devices__    |
  | ---                          | ---                      |
  | Etherchannel                 | Cisco Catalyst..and more |
  | FlexStack (Master Switch)    | Cisco 2960 & 6500 Series |
  | VSS (Single logical switch)  | NXOS 9k                  |
  | SSO (Stateful Switchover)
  | NSF (Non-stop Forwarding)

<br>
<br>

---
&nbsp;

## 🔌 Wired and wireless network.
*How many devices do you have right now that can connect to the internet?*

<br>

> [!NOTE]
> A network must be Flexible. Reliable. __AVAILABLE__.

<br>

### 📶 PLDT AP vs Wireless Controller & Autonomous AP

<br>

Wifi Mesh
 - Wired Backhaul
 - Wireless Backhaul

<br>

Wifi standards | [IEEE (Institute of Electrical and Electronics Engineers)](https://standards.ieee.org/beyond-standards/the-evolution-of-wi-fi-technology-and-standards/)

  - WiFi 6     IEEE 802.11ax
  - WiFi 7     IEEE P802.11be

<br>
<br>

---
&nbsp;

## In-house vs MSP
On-Prem Devices vs RSTHayup Labs (3-tier Enterprise)

![3Tier](img/3Tier.png)

<br>

~~~
!@CoreTAAS
conf t
 hostname CoreTAAS-#$34T#
 enable secret pass
 service password-encryption
 no ip domain lookup
 no logging cons
 line cons 0 
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int vlan 1
  ip add 10.#$34T#.1.2 255.255.255.0
  no shut
  end
~~~

<br> 

~~~
!@CoreBABA
conf t
 hostname CoreBABA-#$34T#
 enable secret pass
 service password-encryption
 no ip domain lookup
 no logging cons
 line cons 0 
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int vlan 1
  ip add 10.#$34T#.1.4 255.255.255.0
  no shut
  end
~~~

<br>
<br>

---
&nbsp;

## DISCOVERY PROTOCOL
### 🎯 Exercise 01: [3-Tier] Identify port connections between switches.
~~~
!@Switches
show cdp neighbor
~~~

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;

### [3-Tier] SECURITY Best Practice 
Task 1.
- Disable CDP on Access Switches
- Enable LLDP on Access Switches but only transmit LLDP traffic to D1 & D2

Task 2.
- Disable CDP on Distribution Switches towards access switches
- Enable LLDP on D1 & D2, but only allow recieving traffic from A1,A2,A3

<br>
<br>

__SOLUTION__  

<br>

Task 1.
- Disable CDP on Access Switches
~~~
!@A1,A2,A3,A4
conf t
 no cdp run
 end
~~~

<br>

- Enable LLDP on Access Switches but only transmit LLDP traffic to D1 & D2
~~~
!@A1,A2,A3
conf t
 lldp run
 int range e1/1-2,e2/1-2
  lldp transmit
  no lldp receive
  end
~~~

<br>

Task 2.
- Disable CDP on Distribution Switches towards access switches
~~~
!@D1,D2
conf t
 int range e1/1-2,e2/1-2,e3/1-2
  no cdp enable
  end
~~~

- Enable LLDP on D1 & D2, but only allow receiving traffic from A1,A2,A3
~~~
!@D1,D2
conf t
 lldp run
 int range e1/1-2,e2/1-2,e3/1-2
  no lldp transmit
  lldp receive
  end
~~~

&nbsp;
---
&nbsp;

### Remote Access

~~~
!@cmd
ping 10.#$34T#.1.2
ping 10.#$34T#.1.4

nmap -v 10.#$34T#.1.2
nmap -v 10.#$34T#.1.4
~~~

Telnet the following
- 10.#$34T#.1.2
- 10.#$34T#.1.4

&nbsp;
---
&nbsp;

### Frame Forwarding
*What is the source MAC address of the Telnet session when it is received by CoreTAAS?*

Structure of an Ethernet Frame

| Layer  | Preamble | SFD | MAC Destination | MAC Source | 802.1Q TAG | Ethertype | Payload | FCS | IGP |
| ---    | ---      | --- | ---             | ---        | ---        | ---       | ---     | --- | --- |
| Length | 7        | 1   | 6               | 6          | 4          | 2         | 42-1500 | 4   | 12  |

<br>

### Error Handling
1. __Giants__ - Ethernet Frame received is larger than the maximum allowed size. Misconfigured MTU
2. __Runts__ - Ethernet Frame received is smaller than the maximum allowed size. Collisions in half-duplex
3. __CRC__ - Checksum did not match. Faulty cable or media.
4. __FCS Error__ - Integrity check fail.
4. __Collisions__ - Transmit on the same medium simultaneously
5. __Late Collisions__
6. __Overruns__ - Input buffer overflow

<br>

__L2 Technologies__
1. ARP
2. VLANs
   - VTP
3. SVI
   - L3 Connectivity
4. LoadBalance
   - Etherchannel
   - Stackwise
   - VSS
5. DHCP
   MAC Learning & Reservation
   - IP Reservation
 
&nbsp; 
---
&nbsp;

__How to get fired!__
~~~
!@CoreTAAS & CoreBABA
conf t
 no spanning-tree vlan 1-999
 end
~~~

<br>

__Save your network__
~~~
!@CoreTAAS & CoreBABA
conf t
 spanning-tree vlan 1-999
 end
~~~

&nbsp; 
---
&nbsp;

### L2 Vulnerabilities (_D3Pentest)
*Why you should properly protect the switch*
- VLAN Hopping attack
- VTP Attack
- Rogue DHCP Server
- CDP Flooding

&nbsp;
---
&nbsp;

## Master the five superheroes of switching
### 1. QPID (802.1Q)

<br>

__Access vs Trunk Links__

~~~
!@CoreTAAS & CoreBABA
conf t
 default int fa0/10-12
 int range fa0/10-12
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end
show int trunk
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 02: [3-Tier] Trunk the links between switches
Task 1.
- Configure the Open standard protocol for trunking on the links between Access & Distribution Switches.
- Configure trunk links between Distribution & Core Switches using the IEEE Standard frame tagging method.
- Make sure VLAN 1 is untagged on all switches.
- Allow all VLANs

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER
<details>
<summary>Show Answer</summary>

~~~
!@C1,C2
conf t
 int range e0/1-3,e1/1-2,e2/1-2
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end
show int trunk
~~~

<br>

~~~
!@D1,D2
conf t
 int range e1/0-3,e2/0-3,e3/1-2
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end
show int trunk
~~~

<br>

~~~
!@A1,A2,A3
conf t
 int range e1/1-2,e2/1-2
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  no shut
  end 
show int trunk
~~~

</details>



<br>
<br>

---
&nbsp;

### 2. DARNA (802.1D)
### `32768  vs  24576  vs  28672`

Properly configure the switch

~~~
!@CoreTAAS & C1
conf t
 spanning-tree mode pvst
 spanning-tree vlan 1-999 root primary
 end
~~~

<br>

~~~
!@CoreBABA & C2
conf t
 spanning-tree mode pvst
 spanning-tree vlan 1-999 root secondary
 end
~~~

<br>

__Determine Port Roles__
- Designated
- Root
- Alternate
- Back

<br>

__Who is the Root?__
Lowest Bridge ID (Priority + MAC Address)

<br>

__How to determine Port Cost__
1. Short Path Cost Method (IEEE 802.1D)

| Link Speed | Default Cost |
| ---        | ---          |
| 10 Mbps    | 100          |
| 100 Mbps   | 19           |
| 1 Gbps     | 4            |
| 10 Gbps    | 2            |

<br>

2. Long Path Cost Method (IEEE 802.1t / 802.1D-2004)

| Link Speed | Default Cost |
| ---        | ---          |
| 10 Mbps    | 2_000_000    |
| 100 Mbps   | 200_000      |
| 1 Gbps     | 20_000       |
| 10 Gbps    | 2_000        |
| 100 Gbps   | 200          |
| 1 Tbps     | 20           |

<br>

~~~
!@CoreBABA
show spanning-tree pathcost method
~~~

<br>

__Port Cost__ = Reference Bandwidth / Link Speed
__Default Ref BW__ = 20_000_000_000 bps

<br>
<br>

---
&nbsp;

### 🎯 Exercise 03: [3-Tier] Identify port roles.
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### [3-Tier] Modify Path costs
Task 1.
- Configure all switches to use the Long Path Cost Method.
- Modify the Reference Bandwidth to 20 Pbs
- Lower the cost of D1's e1/3 interface so it becomes the root port.

<br>

__Solution__

<br>

Task 1.
- Configure all switches to use the Long Path Cost Method.
~~~
!@C1,C2,D1,D2,A1,A2,A3,A4
conf t
 spanning-tree pathcost method long
 end
show spanning-tree pathcost method
~~~

<br>

- Modify the Reference Bandwidth to 20 Pbs
~~~
!@C1,C2,D1,D2,A1,A2,A3,A4
conf t
 !spanning-tree reference-bandwidth cost 20000000000000000
 end
~~~

<br>

- Lower the cost of D1's e1/3 interface to 10 so it becomes the root port.
~~~
!@D1
conf t
 int e1/3
  spanning-tree cost 10
  end
~~~

<br>

Who is __DARNA__ (__802.1D__)
| BLK | LIS | LRN | FWD   |
| --- | --- | --- | ---   |
|     | 15s | 15s | = 30s |

<br>

1. Blocking (BLK) - Listens for BPDUs, does not forward data
2. Listening (LIS) - Listens for BPDUs, starts topology change timer
3. Learning (LRN) - Builds MAC address table but does not forward traffic
4. Forwarding (FWD) - Forwards user traffic and BPDUs

<br>
<br>

---
&nbsp;

### 3. ⚡ WONDERWOMAN (802.1W)
~~~
!@CoreTAAS & CoreBABA, !@C1,C2,D1,D2,A1,A2,A3,A4
conf t
 spanning-tree mode rapid-pvst
 end
show spanning-tree vlan 1
~~~

Discarding, Learning, Forwarding

<br>

STP Features
1. Portfast - Skips all STP negotiation and go straight to forwarding.
   - EDGE Port - Non-Switch link
   - NETWORK Port - Switch to Switch link
2. BPDU Guard - Shuts down a port that receives a BPDU.
3. LOOP Guard - When BPDUs is no longer recieved on Designated ports, keep the port blocked. | Blocking
4. Root Guard - Stops a port from accepting superior BPDUs. | Blocking
5. BPDUFilter - Will not send BPDUs until received.
6. UplinkFast - Recover quickly from uplink failure.
7. BackboneFast - Old ver of Uplinkfast

<br>

__Best Practice__

<br>

Access Layer                        | spanning-tree portfast, spanning-tree bpduguard enable |
Distribution Layer (toward Access)  | spanning-tree guard root
Core/Trunk Links (between switches) | spanning-tree guard loop

<br>

~~~
!@CoreTAAS
conf t
 spanning-tree backbonefast    !unnecessary for rstp (has built-in convergence)
 spanning-tree portfast bpdufilter default
 spanning-tree portfast bpduguard default
 int range fa0/1-8
  spanning-tree portfast  !edge
 !int range fa0/10-12
  !spanning-tree portfast !network
  end
~~~

<br>

~~~
!@CoreBABA
conf t
 spanning-tree uplinkfast    !unnecessary for rstp (has built-in convergence)
 spanning-tree portfast bpdufilter default
 spanning-tree portfast bpduguard default
 int range fa0/1-8
  spanning-tree portfast
 !int range fa0/10-12
  !spanning-tree portfast !network
  end
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 04: [3-Tier] Determine STP Features
What STP features should be applied on the network to optimize STP traffic and network performance.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER
<details>
<summary>Show Answer</summary>
	
~~~
!@A1,A2,A3
conf t
 int range e0/1-2
  spanning-tree portfast edge
  spanning-tree bpduguard enable
  spanning-tree bpdufilter enable
 int range e1/1-2,e2/1-2
  spanning-tree guard loop
  spanning-tree portfast network
  spanning-tree uplinkfast
  end
~~~

<br>

~~~
!@D1,D2
conf t
 int range e1/0-3,e2/0-3,e3/1-2
  spanning-tree portfast network
  spanning-tree guard loop
 int range e1/0,e1/3,e2/0,e2/3
  spanning-tree uplinkfast
  end
~~~

<br>

~~~
!@D2
conf t
 int e0/0
  spanning-tree portfast edge
  spanning-tree bpduguard enable
  spanning-tree bpdufilter enable
  end
~~~

<br>

~~~
!@C1,C2
conf t
 int range e0/1-3,e1/1-2,e2/1-2
  spanning-tree portfast network
  spanning-tree guard loop
  end
~~~

<br>

~~~
!@C2
conf t
 int range e0/1-3
  spanning-tree uplinkfast
  end
~~~

</details>

&nbsp;
---
&nbsp;

### [3-Tier] NIST SP 800-41r1 network security guidance recommends to enable PortFast & BPDU Guard Globally.
~~~
!@Switches
spanning-tree portfast default
spanning-tree portfast bpduguard default
spanning-tree portfast bpdufilter default
~~~

<br>

Who is __WONDERWOMAN__ (__802.1W__)
| DIS | LRN | FWD |
| --- | --- | --- |
|     |     |     |

<br>

1. Discarding (DIS) - Not forwarding user frames; discards traffic. Listens for BPDUs
2. Learning (LRN) - Builds MAC address table but does not forward user traffic
3. Forwarding (FWD) - Forwards user traffic and BPDUs

<br>
<br>

---
&nbsp;

### 4. SUPERMAN (802.1S)
Step 1: Configure VTP
~~~
!@CoreTAAS,C1,C2
conf t
 vtp domain ccnp
 vtp password pass
 vtp mode server
 vtp version 2
 end
~~~

<br>

~~~
!@CoreBABA,D1,D2,A1,A2,A3,A4
conf t
 vtp domain ccnp
 vtp password pass
 vtp mode server
 vtp version 2
 end
~~~

Step 2: Configure VLANs

~~~
!@CoreTAAS,C1,C2
conf t
 vlan 1-40
  exit
 vlan 41-70
  exit
 vlan 71-100
 end
~~~

<br>

~~~
!@CoreBABA
conf t
 int range fa0/2,fa0/4
  switchport mode access
  switchport access vlan 10
 int range fa0/6,fa0/8
  switchport mode access
  switchport access vlan 50
 int fa0/3
  switchport mode access
  switchport access vlan 100
 int range fa0/5,fa0/7
  switchport voice vlan 100
  end
~~~

<br>

Step 3: Enable 802.1S

~~~
!@CoreTAAS,CoreBABA,C1,C2,D1,D2,A1,A2,A3
conf t
 spanning-tree mode mst
 spanning-tree mst configuration
  name superman-stp
  revision 1
   instance 1 vlan 1-40
   instance 2 vlan 41-70
   instance 3 vlan 71-100
   end
show spanning-tree mst configuration
~~~

<br>

Reconfigure Port Priority
~~~
!@CoreTAAS,C1
config t
 spanning-tree mst 0 root primary
 spanning-tree mst 1 root secondary
 spanning-tree mst 2 root primary
 spanning-tree mst 3 root secondary
end
~~~

<br>

~~~
!@CoreBABA,C2
config t
 spanning-tree mst 0 root Secondary
 spanning-tree mst 1 root primary
 spanning-tree mst 2 root Secondary
 spanning-tree mst 3 root primary
end
~~~

Who is SUPERMAN (802.1S)
Multiple VLANs sharing a spanning tree instance,  
compared to PVST & RST where each VLANs is its own STP instance.

<br>
<br>

---
&nbsp;

### 5. X-MEN (802.1X)
> [!IMPORTANT]
> Configure WinServer 2022 for a RADIUS Server

~~~
!@CoreTAAS
conf t
 username admin privilege 15 secret pass
 aaa new-model
 radius server WINRAD
  address ipv4 10.#$34T#.1.8 auth-port 1812 acct-port 1813
  key keykeymo
  exit
 aaa group server radius RADGROUP
  server name WINRAD
  exit
 aaa authentication login default group RADGROUP local
 aaa authorization exec default group RADGROUP local
 line vty 0 14
  login authentication default
  end
~~~

<br>
<br>

---
&nbsp;

### [3-Tier] Configure AAA-Based local database authentication on C1 & C2 

~~~
!@C1,C2
conf t
 username admin priv 15 secret pass
 aaa new-model
 aaa authentication login default local
 aaa authorization exec default local
 aaa authentication enable default enable
 line vty 0 4
  transport input all
  login authentication default
  end
~~~

<br>
<br>

---
&nbsp;

## Port Aggregation
LACP vs PAGP

| Mode             | On  | Active/Desirable | Passive/Auto |
| ---              | --- | ---              | ---          |
| On               | [x] | [ ]              | [ ]          | 
| Active/Desirable | [ ] | [x]              | [x]          |
| Passive/Auto     | [ ] | [x]              | [ ]          |

~~~
!@CoreTAAS
conf t
 int range fa0/10-12
  channel-group 1 mode active
  port-channel load-balance src-mac
  end
show int po1 | inc BW
~~~

<br>

~~~
!@CoreBABA
conf t
 int range fa0/10-12
  channel-group 1 mode passive
  port-channel load-balance src-mac
  end
show int po1 | inc BW
~~~

How does Port-Channel load balance
- src-mac
- src-dst-ip
- extended

<br>

Set a minimum & maximum bundle links.
~~~
!@CoreTAAS,CoreBABA
conf t
 int po1
  lacp max-bundle 8
  port-channel min-links 2
  end
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 05: [3-Tier] Configure Etherchannel links
Note:
- Configure Etherchannel on the links between switches.
- Configure the Port-Channel Number base on the diagram.

Task1:
- C1 & C2 must use the open standard protocol for link aggregation. 
- C1 & C2 must both participate in forming link aggregation on all linked ports.
- If the number of bundled ports goes down to 2 or less, the port-channel must go down.

Task2:
- D1 & D2 must use the open standard protocol for link aggregation. 
- D1 & D2 must not participate but will form link aggregation on all linked ports.

Task3:
- A1, A2, and A3 must use the open standard protocol for link aggregation. 
- A1, A2, and A3 must participate in forming link aggregation on all linked ports.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER
<details>
<summary>Show Answer</summary>
	
Task1:
- C1 & C2 must use the open standard protocol for link aggregation.
- C1 & C2 must both participate in forming link aggregation on all linked ports.

~~~
!@C1
conf t
 int range e0/1-3
  channel-group 102 mode active
 int range e1/1-2
  channel-group 11 mode active
 int range e2/1-2
  channel-group 12 mode active
  end
~~~

<br>

~~~
!@C2
conf t
 int range e0/1-3
  channel-group 102 mode active
 int range e1/1-2
  channel-group 21 mode active
 int range e2/1-2
  channel-group 22 mode active
  end
~~~

- On the link between C1 & C2, if the number of bundled ports goes down to 2 or less, the port-channel must go down.

~~~
!@C1,C2
conf t
 int po102
  port-channel min-links 3
  end
~~~

<br>

Task2:
- D1 & D2 must use the open standard protocol for link aggregation. 
- D1 & D2 must not participate but will form link aggregation on all linked ports.

~~~
!@D1
conf t
 int range e1/0,e1/3
  channel-group 11 mode passive
 int range e2/0,e2/3
  channel-group 21 mode passive
 int range e1/1-2
  channel-group 111 mode passive
 int range e2/1-2
  channel-group 112 mode passive
 int range e3/1-2
  channel-group 113 mode passive
  end
~~~

<br>

~~~
!@D2
conf t
 int range e1/0,e1/3
  channel-group 12 mode passive
 int range e2/0,e2/3
  channel-group 22 mode passive
 int range e1/1-2
  channel-group 221 mode passive
 int range e2/1-2
  channel-group 222 mode passive
 int range e3/1-2
  channel-group 223 mode passive
  end
~~~

<br>

Task3:
- A1, A2, and A3 must use the open standard protocol for link aggregation. 
- A1, A2, and A3 must participate in forming link aggregation on all linked ports.

~~~
!@A1
conf t
 int range e1/1-2
  channel-group 111 mode active
 int range e2/1-2
  channel-group 221 mode active
  end
~~~

<br>

~~~
!@A2
conf t
 int range e1/1-2
  channel-group 112 mode active
 int range e2/1-2
  channel-group 222 mode active
  end
~~~

<br>

~~~
!@A3
conf t
 int range e1/1-2
  channel-group 113 mode active
 int range e2/1-2
  channel-group 223 mode active
  end
~~~

</details>

<br>
<br>

---
&nbsp;

## IP ADDRESSING
### Switch Virtual Interface (SVI)

~~~
!@CoreTAAS
conf t
 int vlan 10
  description WIFIVLAN
  ip add 10.#$34T#.10.2 255.255.255.0
  no shut
  exit
 int vlan 50
  description CCTVVLAN
  ip add 10.#$34T#.50.2 255.255.255.0
  no shut
  exit
 int vlan 100
  description VOICEVLAN
  ip add 10.#$34T#.100.2 255.255.255.0
  no shut
  end
~~~

<br>

~~~
!@CoreBABA
conf t
 int vlan 10
  description WIFIVLAN
  ip add 10.#$34T#.10.4 255.255.255.0
  no shut
  exit
 int vlan 50
  description CCTVVLAN
  ip add 10.#$34T#.50.4 255.255.255.0
  no shut
  exit
 int vlan 100
  description VOICEVLAN
  ip add 10.#$34T#.100.4 255.255.255.0
  no shut
  end
~~~

<br>
<br>

Assign IP Addresses on PCs based on their specified VLAN.
- Make sure PCs can communicate with C1 & C2 (Gateway)

~~~
!@P1
conf t
 int e0/0
  no shut
  ip add 10.1.10.101 255.255.255.224
  end
~~~

<br>

~~~
!@P2
conf t
 int e0/0
  no shut
  ip add 192.168.30.113 255.255.255.248
  end
~~~

<br>

~~~
!@P3
conf t
 int e0/0
  no shut
  ip add 10.1.20.60 255.255.255.240
  end
~~~

<br>

~~~
!@P4
conf t
 int e0/0
  ip add 10.1.10.102 255.255.255.224
  no shut
  end
~~~
  
<br>
<br>

---
&nbsp;

### DHCP
~~~
!@CoreTAAS
conf t
 ip dhcp excluded-address 10.#$34T#.1.1 10.#$34T#.1.100
 ip dhcp excluded-address 10.#$34T#.10.1 10.#$34T#.10.100
 ip dhcp excluded-address 10.#$34T#.50.1 10.#$34T#.50.100
 ip dhcp excluded-address 10.#$34T#.100.1 10.#$34T#.100.100
 ip dhcp pool POOLDATA
  network 10.#$34T#.1.0 255.255.255.0
  default-router 10.#$34T#.1.4
  domain-name MGMTDATA.COM
  dns-server 10.#$34T#.1.10
 ip dhcp pool POOLWIFI
  network 10.#$34T#.10.0 255.255.255.0
  default-router 10.#$34T#.10.4
  domain-name WIFIDATA.COM
  dns-server 10.#$34T#.1.10
  option 43 ip 10.#$34T#.10.#$34T#
 ip dhcp pool POOLCCTV
  network 10.#$34T#.50.0 255.255.255.0
  default-router 10.#$34T#.50.4
  domain-name CCTVDATA.COM
  dns-server 10.#$34T#.1.10
 ip dhcp pool POOLVOICE
  network 10.#$34T#.100.0 255.255.255.0
  default-router 10.#$34T#.100.4
  domain-name VOICEDATA.COM
  dns-server 10.#$34T#.1.10
  option 150 ip 10.#$34T#.100.8
  end
~~~

<br>

| DHCP Options | Unit |
| ---          | ---  |
| 1            |      |
| 2            |      |
| 43           |      |
| 42           |      |
| 150          |      |

<br>

DHCP States:
1.
2.
3.
4.

What type of data traffic is each state? (Unicast, Broadcast, Multicast)
Base on Wireshark.

<br>
<br>

---
&nbsp;

### 🎯 Exercise 06: [3-Tier] Configure DHCP Pool for SALES
Task 1.
- Use the IP address 192.168.50.0/24
- Apply the First Valid IP on C1, last Valid on C2
- Load balance between C1 & C2 
  - C1 must distribute .100 - .199 IPs
  - C2 must distribute .200 - .253 IPs
- Set the Domain name to SALES.COM
- The default Gateway must be the DHCP server that provided the IP address.

<br>

Task 2.
- Configure P5 as a dhcp client

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER
<details>
<summary>Show Answer</summary>
	
~~~
!@C1
conf t
 int vlan 50
  no shut
  ip add 192.168.50.1 255.255.255.0
  exit
 ip dhcp excluded-address 192.168.50.1 192.168.50.99
 ip dhcp pool SALES.COM
  network 192.168.50.0 255.255.255.0
  default-router 192.168.50.1
  domain-name SALES.COM
  end
~~~

<br>

~~~
!@C2
conf t
 int vlan 50
  no shut
  ip add 192.168.50.254 255.255.255.0
  exit
 ip dhcp excluded-address 192.168.50.1 192.168.50.199
 ip dhcp pool SALES.COM
  network 192.168.50.0 255.255.255.0
  default-router 192.168.50.254
  domain-name SALES.COM
  end
~~~

<br>

~~~
!@P5
conf t
 int e0/0
  no shut
  ip add dhcp
  end
~~~

</details>

<br>
<br>

---
&nbsp;

### VLAN Management
*Did devices get IP from the correct VLAN?*

~~~
!@CoreBABA
conf t
 int range fa0/2,fa0/4
  switchport mode access
  switchport access vlan 10
  exit
 int range fa0/6,fa0/8
  switchport mode access
  switchport access vlan 50
  exit
 int fa0/3
  switchport mode access
  switchport access vlan 100
  exit
 int range fa0/5,fa0/7
  switchport mode access
  switchport access vlan 100
  switchport voice vlan 100
  mls qos trust device cisco-phone
  mls qos trust cos
  end
~~~

<br>

__Assign RSTVM to VLAN 1__
~~~
!@A3
conf t
 int e3/3
  no shut
  switchport mode access
  switchport access vlan 1
  end
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 07: [3-Tier] Assign end devices to their specified VLAN
| Device | VLAN    |
| ---    | ---     |
| P1     | ADMIN   |
| P2     | HR      | 
| P3     | FINANCE |
| P4     | ADMIN   |
| P5     | SALES   |

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER
<details>
<summary>Show Answer</summary>

~~~
!@A1
conf t
 int e0/1
  switchport mode access
  switchport access vlan 10
 int e0/0
  switchport mode access
  switchport access vlan 30
  end
~~~

<br>

~~~
!@A2
conf t
 int e0/1
  switchport mode access
  switchport access vlan 20
 int e0/0
  switchport mode access
  switchport access vlan 10
  end
~~~

<br>

~~~
!@A3
conf t
 int e0/1
  switchport mode access
  switchport access vlan 50
  end
~~~

</details>

<br>
<br>

---
&nbsp;

## MAC Learning
### IP Reservation
~~~
!@CoreTAAS
conf t
 ip routing
 ip dhcp pool CAMERA6
  host 10.#$34T#.50.6 255.255.255.0
  client-identifier #camera6macadd#
 ip dhcp pool CAMERA8
  host 10.#$34T#.50.8 255.255.255.0
  client-identifier #camera8macadd#
 end
~~~

&nbsp;
---
&nbsp;

### [3-Tier] Reserve IP address for S1
Task 1.
- Assign S1 to the ServerFarm VLAN
- Configure S1 with a Client-ID on its e0/0 interface as its MAC Address

<br>

Task 2.
- Configure a DHCP pool on C2 to reserve IP 10.1.100.200/25 for S1
- Have the DHCP pool name to be S1Farm
- Set the default gateway as C2
- Set S1 as a DHCP Client

<br>

~~~
!@D2
conf t
 int e0/0
  switchport mode access
  switchport access vlan 100
  no shut
  end
~~~

<br>

~~~
!@S1
show int e0/0
conf t
 int e0/0
  no shut
  ip dhcp client client-id hex #M4C4DDR3SS#
  ip add dhcp
  end
~~~

<br>

~~~
!@C2
conf t
 int vlan 100
  no shut
 ip dhcp pool S1Farm
  host 10.1.100.200 255.255.255.128
  default-router 10.1.100.130
  client-identifier #M4C4DDR3SS#
  end
~~~

<br>
<br>

---
&nbsp;

### Port Security
~~~
!@CoreBABA
conf t
 int fa0/6
  switchport mode access
  switchport port-security
  switchport port-security mac-address sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
  exit
 int fa0/8
  switchport mode access
  switchport port-security
  switchport port-security mac-address sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
  end
sh port-security address
sh int status err-disable
~~~

<br>

__Make Ports Alive again__
~~~
!@CoreBABA
config t
 int fa0/6
  no switchport port-security
  shut
  no shut
 int fa0/8
  no switchport port-security
  shut
  no shut
  end
~~~

<br>
<br>

---
&nbsp;

### 🎯 Exercise 08: [3-Tier] Set Port-Security for S1
Task 1.
- Configure D2 to dynamically learn only 1 MAC Address on its e0/0 interface.
- If it learns an Invalid MAC, make sure the port goes to an errdisabled state.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER
<details>
<summary>Show Answer</summary>

~~~
!@D2
conf t
 int e0/0
  switchport mode access
  switchport port-security
  switchport port-security mac-address sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
  end
~~~

<br>

~~~
!@S1
conf t
 int e0/0
  mac-address 0011.1111.1111
  end
~~~

<br>

~~~
!@D2
show port-security address 
show int status err-disable
~~~

</details>
 
<br>
<br>

---
&nbsp;

## Dynamic ARP Inspection & DHCP Snooping
~~~
!@CoreBABA
conf t
 ip dhcp snooping
 ip dhcp snooping vlan 100
 no ip dhcp snooping information option
 !
 int po1
  ip dhcp snooping trust
  end
show ip dhcp snooping binding
~~~

<br>

~~~
!@CoreBABA
conf t
 ip arp inspection vlan 100
 int range fa0/1-8,fa0/10-12
  ip arp inspection trust
  exit
 ip arp inspection validate src-mac dst-mac ip
 end
~~~

<br>
<br>

---
&nbsp;

## Managing Enterprise Communication
~~~
!@CUCM
conf t
 hostname CUCM-#$34T#
 enable secret pass
 service password-encryption
 no ip domain lookup
 no logging cons
 line cons 0 
  password pass
  login
  exec-timeout 0 0
 line vty 0 14
  password pass
  login
  exec-timeout 0 0
 int fa0/0
  ip add 10.#$34T#.100.8 255.255.255.0
  no shut
  end
~~~

<br>
<br>

---
&nbsp;

### Analog Phones
~~~
!@CUCM
conf t
 dial-peer voice 1 pots
  destination-pattern #$34T#00
  port 0/0/0
 dial-peer voice 2 pots
  destination-pattern #$34T#01
  port 0/0/1
 dial-peer voice 3 pots
  destination-pattern #$34T#02
  port 0/0/2
 dial-peer voice 4 pots
  destination-pattern #$34T#03
  port 0/0/3
 end
~~~

<br>

~~~
!@CUCM
conf t
 voice-port 0/0/0
  signal loopstart
  caller-id enable
  station-id name ANALOG1
  cptone PH  / US
 end
!
csim start #$34T#00
~~~

<br>
<br>

---

### IP Phones
__Requirements for IP Phones to work__
7.
6.
5.
4. 
3. 
2.
1.

<br>

~~~
!@CUCM
conf t
 no telephony-service
 telephony-service
  no auto assign
  no auto-reg-ephone
  max-ephones 5
  max-dn 20
  ip source-address 10.#$34T#.100.8 port 2000
  create cnf-files
 ephone-dn 1
  number #$34T#11
 ephone-dn 2
  number #$34T#22
 ephone-dn 3
  number #$34T#33
 ephone-dn 4
  number #$34T#44
 ephone-dn 5
  number #$34T#55
 ephone-dn 6
  number #$34T#66
 ephone-dn 7
  number #$34T#77
 ephone-dn 8
  number #$34T#88
 ephone 1
  mac-address #ephone1macadd#
  type 8945
  button 1:1 2:2 3:3 4:4
  restart
 ephone 2
  mac-address #ephone2macadd#
  type 8945
  button 1:5 2:6 3:7 4:8
  restart
 end
~~~

<br>
<br>

---
&nbsp;

### IP Phone Features (Video/Conference Calls)
~~~
!@CUCM
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
~~~

<br>
<br>

---
&nbsp;

### Quality of Service
- Markings
- Queue
- Tags

<br>

~~~
!@CoreBABA
conf t
 int range fa0/5,fa0/7
  mls qos trust device cisco-phone
  end
~~~

<br>
<br>

---
&nbsp;

### Incoming Calls
~~~
!@CUCM
conf t
 voice service voip
 ip address trusted list
 ipv4 0.0.0.0 0.0.0.0
 end
~~~

<br>
<br>

---
&nbsp;

### Outgoing Calls
~~~
!@CUCM
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
 dial-peer voice 91 Voip
  destination-pattern 91..
  session target ipv4:10.91.100.8
  codec g711ULAW
 dial-peer voice 92 Voip
  destination-pattern 92..
  session target ipv4:10.92.100.8
  codec g711ULAW
 end
~~~

<br>
<br>

---
&nbsp;

### Remote Access - Jumpserver
*Can you reach CUCM from the PC?*

~~~
!@cmd
ping 10.#$34T#.100.8
~~~

<br>
<br>

---
&nbsp;

## 🔧 Configure EDGE
### 🏨 Establish connectivity.
*How do you gain access to the internet?*

<br>

Customer Premises
- Provider EDGE
- Customer Devices

&nbsp;
---
&nbsp;

~~~
!@EDGE
conf t
 hostname EDGE-#$34T#
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
  ip add 10.#$34T#.#$34T#.1 255.255.255.0
  desc INSIDE
 int gi 0/0/1
  no shut
  ip add 200.0.0.#$34T# 255.255.255.0
  desc OUTSIDE
 int loopback 0
  ip add #$34T#.0.0.1 255.255.255.255
  desc VIRTUALIP
 end
~~~

<br>

### `Switch` vs `Routers`
~~~
!@CoreBABA
conf t
 int g0/1
  no switchport
  ip add 10.#$34T#.#$34T#.4 255.255.255.0
  no shut
  end
~~~

<br>
<br>

---
&nbsp;

## Site Connectivity
### Private Circuit
~~~
!@EDGE
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
 ip route 10.91.0.0 255.255.0.0 200.0.0.91 254
 ip route 10.92.0.0 255.255.0.0 200.0.0.92 254
 no ip route 10.#$34T#.0.0 255.255.0.0 200.0.0.#$34T# 254
 ip route 10.#$34T#.0.0 255.255.0.0 10.#$34T#.#$34T#.4 254
 !
 router ospf 1
  router-id #$34T#.0.0.1
  network #$34T#.0.0.1 0.0.0.0 area #$34T#
  network 10.#$34T#.#$34T#.0 0.0.0.255 area #$34T#
  network 200.0.0.0 0.0.0.255 area 0
 int gi 0/0/0
  ip ospf network point-to-point
  end
~~~

<br>

~~~
!@CoreBABA
conf t
 router ospf 1
  router-id 10.#$34T#.#$34T#.4
   network 10.#$34T#.0.0 0.0.255.255 area #$34T#
 int gi 0/1
  ip ospf network point-to-point
  end
~~~

<br>

~~~
!@CUCM
conf t
 router ospf 1
  router-id 10.#$34T#.100.8
  network 10.#$34T#.100.0 0.0.0.255 area #$34T#
  end
~~~

<br>
<br>

---
&nbsp;

### Internet Access
~~~
!@EDGE
conf t
 int g0/0/0
  ip nat inside
  exit
 int g0/0/1
  ip nat outside
  end
~~~

<br>

~~~
!@EDGE
conf t
 ip access-list extended NAT-POLICY
  deny ip 10.#$34T#.0.0 0.0.255.255 10.11.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.12.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.21.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.22.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.31.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.32.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.41.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.42.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.51.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.52.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.61.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.62.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.71.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.72.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.81.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.82.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.91.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.92.0.0 0.0.255.255
  no deny ip 10.#$34T#.0.0 0.0.255.255 10.#$34T#.0.0 0.0.255.255
  permit ip any any
  end
~~~

<br>

~~~
!@EDGE
conf t
 ip nat inside source list NAT-POLICY int g0/0/1 overload
 end
~~~

<br>

~~~
!@EDGE
conf t
 ip route 0.0.0.0 0.0.0.0 200.0.0.1
 ip name-server 10.#$34T#.1.10
 ip domain lookup
 end
~~~

<br>
<br>

---
&nbsp;

### Network Assurance (HSRP)
~~~
!@D1
conf t
 interface Vlan 10
  standby 1 ip 10.2.1.254
  standby 1 priority 110
  standby 1 preempt
  end
~~~

<br>

~~~
@D2
conf t
 interface Vlan 10
  standby 1 ip 10.2.1.254
  end
~~~











### Network Tunneling
~~~
!@EDGE
conf t
 int tun1
  ip add 172.16.1.#$34T# 255.255.255.0
  tunnel source g0/0/1
  tunnel mode gre multipoint
  no shut
  tun key 123
  ip nhrp authentication C1sc0123
  ip nhrp map multicast dynamic
  ip nhrp network-id 1337
  ip nhrp map 172.16.1.11 200.0.0.11
  ip nhrp map 172.16.1.12 200.0.0.12
  ip nhrp map 172.16.1.21 200.0.0.21
  ip nhrp map 172.16.1.22 200.0.0.22
  ip nhrp map 172.16.1.31 200.0.0.31
  ip nhrp map 172.16.1.32 200.0.0.32
  ip nhrp map 172.16.1.41 200.0.0.41
  ip nhrp map 172.16.1.42 200.0.0.42
  ip nhrp map 172.16.1.51 200.0.0.51
  ip nhrp map 172.16.1.52 200.0.0.52
  ip nhrp map 172.16.1.61 200.0.0.61
  ip nhrp map 172.16.1.62 200.0.0.62
  ip nhrp map 172.16.1.71 200.0.0.71
  ip nhrp map 172.16.1.72 200.0.0.72
  ip nhrp map 172.16.1.81 200.0.0.81
  ip nhrp map 172.16.1.82 200.0.0.82
  ip nhrp map 172.16.1.91 200.0.0.91
  ip nhrp map 172.16.1.92 200.0.0.92
  no ip nhrp map 172.16.1.#$34T# 200.0.0.#$34T#
  end
~~~

<br>

~~~
!@EDGE
conf t
 ip route 10.11.0.0 255.255.0.0 172.16.1.11 252
 ip route 10.12.0.0 255.255.0.0 172.16.1.12 252
 ip route 10.21.0.0 255.255.0.0 172.16.1.21 252
 ip route 10.22.0.0 255.255.0.0 172.16.1.22 252
 ip route 10.31.0.0 255.255.0.0 172.16.1.31 252
 ip route 10.32.0.0 255.255.0.0 172.16.1.32 252
 ip route 10.41.0.0 255.255.0.0 172.16.1.41 252
 ip route 10.42.0.0 255.255.0.0 172.16.1.42 252
 ip route 10.51.0.0 255.255.0.0 172.16.1.51 252
 ip route 10.52.0.0 255.255.0.0 172.16.1.52 252
 ip route 10.61.0.0 255.255.0.0 172.16.1.61 252
 ip route 10.62.0.0 255.255.0.0 172.16.1.62 252
 ip route 10.71.0.0 255.255.0.0 172.16.1.71 252
 ip route 10.72.0.0 255.255.0.0 172.16.1.72 252
 ip route 10.81.0.0 255.255.0.0 172.16.1.81 252
 ip route 10.82.0.0 255.255.0.0 172.16.1.82 252
 ip route 10.91.0.0 255.255.0.0 172.16.1.91 252
 ip route 10.92.0.0 255.255.0.0 172.16.1.92 252
 !
 no ip route 10.#$34T#.0.0 255.255.0.0 172.16.1.#$34T# 252
 end
~~~ 

<br>
<br>

---
&nbsp;

### OSPF vs EIGRP
*Does OSPF Routers form neighborships behind NAT devices?*

<br>

~~~
!@EDGE
conf t
 int tun1
  no ip eigrp next-hop-self
  no ip split-horizon eigrp 100
  bandwidth 10000
  mtu 1400
  ip tcp adjust-mss 1360
 no router ospf 1
 router ospf 1
  router-id #$34T#.0.0.1
  network 10.#$34T#.#$34T#.0 0.0.0.255 area #$34T#
  default-information originate always
 router eigrp 100
  no auto-summary
  router-id 200.0.0.#$34T#
  network 200.0.0.0 0.0.0.255
  network 172.16.1.0 0.0.0.255
  end
~~~

<br>

~~~
!@EDGE
conf t
 router ospf 1
  redistribute eigrp 100 subnets
  exit
 router eigrp 100
  redistribute ospf 1 metric 10000 100 255 1 1500
  end
~~~

<br>
<br>

---
&nbsp;

## Wireless Connectivity
Configure AUT-AP using python





### Assurance 
Review

Requirements for IP Phones to work
7. App
6. G711 G729
5. RTP
4. TFTP Server, SCCP: , SIP:
3. IP
2. MAC
1. PoE

!@cmd
nmap -v 10.#$43T#.100.8

How to monitor packets from a different network?
SPAN
!@CoreBABA
conf t
 monitor session 1 source int fa0/3,fa0/5,fa0/7
 monitor session 1 destination int fa0/1,fa0/9
 end

Remove SPAN
!@CoreBABA
conf t
 no monitor session 1 source int fa0/3,fa0/5,fa0/7
 no monitor session 1 destination int fa0/1,fa0/9
 end

















