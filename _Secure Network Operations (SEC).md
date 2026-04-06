
<!-- Your monitor number = #$34T# -->


# 👋 Welcome to Rivan
*"There's no better teacher than experience"*


&nbsp;
## 📋 Prove what you are doing.
 - Create a Github account: https://github.com/

<br>

Import the repositories.
 - Rivan_Day1 : https://github.com/art-stacks/Rivan_Day1
 - SecPlus701 : https://github.com/rivancorp/SECplus701
 - RivanSecPlus701 : https://github.com/rivancorp/RivanSecPlus701


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

---
&nbsp;


# 🏦 Secure Enterprise Network Architecture

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
<br>
<br>
<br>

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

  - WiFi 6     
  - WiFi 7     


<br>
<br>

---
&nbsp;


## 🔍 Implement security solutions.
*What is more valuable than gold? __Data__*

<br>

Network security infrastructure
 - NGFW, UTM, IDS
 - Security Policies
     - Windows Local Security Policy
 - Surveillance
     - IP Cameras (__CAM6__ & __CAM8__)

<br>

Made in US 🇺🇸 vs Made in China 🇨🇳


<br>
<br>

---
&nbsp;


# 🔧 Access the CLI
*How can you tell if a device is expensive? It has a __Console Port__*

<br>

Serial Cable
  - VGA, USB
  - Ugreen


<br>
<br>

---
&nbsp;


# 📤 IT Service Management
*If it is not documented, it never existed.*
- ITSM
- CMDB

<br>

### Lab Setup
__1. Run the *IR-ElasticSys* virtual machine & Setup a WINSERVER VM__  

<br>

__2. VM Login information:__
> Username: root  
> Password: C1sc0123

<br>

__3. Get the IP address of the VM.__  
Enter the command inside the VM
~~~bash
@IR-ElasticSys
ip addr
~~~

<br>

__4. Add a hostname mapping.__  
Access the __hosts__ file located on `c:\Windows\System32\drivers\etc`  
Then, enter add the following mapping to the hosts file:
~~~
192.168.102.133  rivan.cloudsoc.com
~~~

> [!Note]
> __192.168.102.133__ must be your virtual machine IP address.

<br>

__5. Ping to verify setup for the virtual machine.__
~~~
@cmd
ping rivan.cloudsoc.com
~~~


&nbsp;
---
&nbsp;


## 🔄 ITSM Process | Implementing Cybersecurity best practices
### 🏃 Service Delivery Team
http://rivan.cloudsoc.com/otrs/index.pl  
> Username: admin   
> Password: C1sc0123  


&nbsp;
---
&nbsp;


### 🙇 Service Desk
http://rivan.cloudsoc.com/otrs/customer.pl  
> Username: user1  
> Password: C1sc0123


&nbsp;
---
&nbsp;


## 📦 Operational Support System
*How easy is it to bring home items from your company?*

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


### 🎯 Exercise 01: Create a Customer User Account

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


### 🎯 Exercise 02: Register Windows Server 2025 to your company's database.

__1. Access CMDB__  

<br>
<br>

__2. Select the appropriate Item Class__  

<br>
<br>

__3. Register Windows Server 2025.__  
  
View System specs using __DirectX Diagnostic Tool__  
~~~
@WinServer [Win + R]
dxdiag
~~~

<br>

Or view __System Information__  
~~~
@WinServer [Win + R]
msinfo32
~~~

<br>

Identify Serial number
~~~powershell
@powershell
Get-WmiObject win32_bios | select Serialnumber
~~~

<br>

Expiration Date:


<br>
<br>

---
&nbsp;


## 🚀 Deploy CoreTAAS
### ⭐ 1. Register CoreTAAS to your company's database, including a *FAQ* to configure the devices.

~~~
!@CoreTaas
conf t
 hostname CoreTAAS-#$34T#
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
 vlan 10
  name WIFIVLAN
 vlan 50
  name CCTVVLAN
 vlan 100
  name VOICEVLAN
 int vlan 1
  no shut
  ip add 10.#$34T#.1.2 255.255.255.0
  desc DEFAULT-VLAN
 int vlan 10
  no shut
  ip add 10.#$34T#.10.2 255.255.255.0
  desc WIFI-VLAN
 int vlan 50
  no shut
  ip add 10.#$34T#.50.2 255.255.255.0
  desc CCTV-VLAN
 int vlan 100
  no shut
  ip add 10.#$34T#.100.2 255.255.255.0
  desc VOICE-VLAN
 end
~~~


<br>
<br>

---
&nbsp;


## 🚀 Deploy CoreBABA
### 🎯 Exercies 03: Register CoreBABA to your company's database.

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


<br>
<br>

---
&nbsp;


## Know the jobs of a Switch
### ⚙️ 1. __POE__
*Are there switches that don't support POE? __Yes__.*
> [!NOTE]
> If you need PoE functionality on a non-PoE switch, use a PoE injector.

<br>

| IEEE Standards  | Power Output |
| ---             |     ---      |
| 802.    (PoE)   |              |
| 802.    (PoE+)  |              |
| 802.    (PoE++) |              |

<br>

> __CMDB__  
> Name: CoreBABA  
> Description: 1st Job of a Switch - PoE  
>   Switches need to supply the right amount of power depending on the needs of end devices.  


<br>
<br>

---
&nbsp;


### ⚙️ 2. SVI (Switch Virtual Interface)
*Why segment network traffic? __WireShark__*

<br>

> __FAQ (Knowledge Database)__   
> Title: 2nd Job of a Switch - SVI  
> Symptom: Lack of IP addresses.  
> Problem: Prevents remote management and L3 operations   
> Solution:   


<br>

~~~
!@CoreBABA
conf t
 hostname coreBaba-#$34T#
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
  ip add 10.#$34T#.#$34T#.4 255.255.255.0
 int vlan 1
  no shut
  ip add 10.#$34T#.1.4 255.255.255.0
  desc DEFAULT-VLAN
 int vlan 10
  no shut
  ip add 10.#$34T#.10.4 255.255.255.0
  desc WIFI-VLAN
 int vlan 50
  no shut
  ip add 10.#$34T#.50.4 255.255.255.0
  desc CCTV-VLAN
 int vlan 100
  no shut
  ip add 10.#$34T#.100.4 255.255.255.0
  desc VOICE-VLAN
 end
~~~

<br>

Verify Connectivity: 

~~~
!@cmd
ping 10.#$34T#.1.4
~~~


<br>
<br>

---
&nbsp;


# ⭐ Fundamental Security Concepts
1. __C__
2. __I__
3. __A__

&nbsp;
---
&nbsp;

### 🔐 Confidentiality

~~~
!@cmd
ping 10.#$34T#.1.4
ping 10.#$34T#.1.2
~~~

<br>

~~~
!@cmd
nmap -sP 10.3.3.0/24
nmap -O 10.3.3.0/24
~~~

<br>

~~~
!@cmd
nmap -v 10.#$34T#.1.2
~~~

<br>

Is port __23/Telnet__ open?  
Is port __445/Microsoft-DS & 139/ServerMessageBlock__ open?  

<br>

*How to access port 445 because you don't have a Firewall!*
~~~
!@cmd
net use \\10.3.3.x\ipc$ /user:administrator C1sc0123
net use x: /delete
net use x: \\10.3.3.x\c$
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 04: Why use VPN when you are WFH
~~~
!@CoreTAAS
conf t
 username admin privilege 15 secret pass
 line vty 0 14
  password pass
  login local
  exec-timeout 0 0
  end
~~~

<br>

__Access Wireshark__

<br>

| Attempt    | Answer                          |
| ---        | ---                             |
| 1:Username | What did you eat last night?    | 
| 2:Password | What is your favorite dessert?  |
| ###        | ###                             |
| 1:Username | What's the name of your school? |
| 2:Password | What's your course in college?  |
| ###        | ###                             |
| 1:Username | admin                           |
| 2:Password | pass                            |

<br>

__Implement Secure Protocols: SSH__

| 🔑 | Public | Private | 🔑 |
| --- | ---   | ---     | --- |

<br>

~~~
!@CoreTAAS
conf t
 ip domain name sec.com
 crypto key generate rsa
 2048
 ip ssh version 2
 line vty 0 14
  transport input all
  end
~~~

__Parser View__
~~~
!@CoreTAAS
conf t
 aaa new-model
 aaa authentication login default local
 aaa authorization exec default local
 line vty 0 14
  transport input all
  login authentication default
 !
 parser view T1
  secret pass
  commands exec include configure terminal
  commands exec include show ip interface brief
  commands exec include show interface *
  commands configure include interface
  commands configure include interface GigabitEthernet1 
  commands interface include shutdown
  commands interface include no shutdown
  exit
 username tier1 view T1 secret pass
 username tier2 privilege 15 secret pass
 end
~~~


<br>

*__Confidentiality__ is the security concept that ensures data is protected from unauthorized access or __Disclosure__.*


<br>
<br>

---
&nbsp;


### ✉️ Integrity
~~~
!@cmd
certutil -hashfile SERVER_EVAL_x64FRE_en-us.iso md5
~~~


<br>
<br>

---
&nbsp;


### 🔀 Availability
*Avoid a single point of failure*


Execute a persistent ping
~~~
!@cmd
ping 10.#$34T#.1.2 -t
~~~

~~~
!@CoreBABA & CoreTAAS
conf t
 int range fa0/10-12
  channel-group 1 mode active
  exit
 int po1
  switchport trunk encaps dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan 1
  end
show int po1 | inc BW
~~~


<br>
<br>

---
&nbsp;


### ⚙️ 3. DHCP / BOOTPS & BOOTPC
*In a network, which device should be a DHCP Server? __It depends.__*

| Network     | DHCP Device |
| ---         |     ---     |
| SOHO        |             |
|             |             |
| Enterprise  |             |
| Medium Biz  |             |
| Large Biz   |             |


<br>
<br>

---
&nbsp;


🔴 __Creating a Rogue DHCP Server:__
- WireShark
- Pentest

<br>

__\_Pentest__
~~~
!@linux
nmcli connection add \
type ethernet \
con-name TUNAYNALAN \
ifname eth0 \
ipv4.method manual \
ipv4.addresses 10.#$34T#.1.20/24 \
autoconnect yes

nmcli connection up TUNAYNALAN
~~~


<br>


> __FAQ (Knowledge Database)__   
> Title: 3rd Job of a Switch - DHCP  
> Symptom: Lack of IP addresses.  
> Problem: If End devices do not have IP addresses they will not be able to communicate across the network.
> Solution:


<br>


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
  option 43 ip 10.#$34T#.10.7
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


🔴 __DHCP Starvation Attack:__

| States      | Type      |
| ---         | ---       |
| Discover    |           |
| Offer       |           |
| Request     |           |
| Acknowledge |           |


<br>
<br>

---
&nbsp;


### ⚙️ 4. VLAN Creation & VLAN Management
*Ports must be placed in the correct VLANs.*

<br>

*How to check what ports belong to what VLAN? __SVB - `show vlan brief`__*

~~~
!@CoreBABA
show vlan brief
~~~


&nbsp;
---
&nbsp;


Just because there's an SVI doesn't mean there's a VLAN.

<br>

> __FAQ (Knowledge Database)__   
> Title: 4th Job of a Switch - VLAN Creation & VLAN Management   
> Symptom: Network devices share the same broadcast domain.    
> Problem: Lack of traffic segmentation on L2 can lead to a broadcast storm.  
> Solution:  


<br>

~~~
!@CoreTAAS
conf t
 vtp mode server
 vtp domain SEC
 vtp version 2
 vlan 10
  name WIFIVLAN
 vlan 50
  name CCTVVLAN
 vlan 100
  name VOICEVLAN
  end
~~~

~~~
!@CoreBABA
conf t
 vtp mode server
 vtp domain SEC
 vtp version 2
 end
~~~


&nbsp;
---
&nbsp;


Place Switchports in their correct VLAN.

~~~
!@CoreBABA
conf t
 int fa 0/2
  switchport mode access
  switchport access vlan 10
 int fa 0/4
  switchport mode access
  switchport access vlan 10
 int fa0/6
  switchport mode access
  switchport access vlan 50
 int fa0/8
  switchport mode access
  switchport access vlan 50
 int fa 0/3
  switchport mode access
  switchport access vlan 100
 int fa 0/5
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
 int fa 0/7
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
 end
~~~


<br>


🔴 __VTP Revision Number Attack:__
*What happens when a device is connected to a VLAN that does not exist? __Orphan-ports__*

<br>
<br>
<br>
<br>

---
&nbsp;


## ⚙️ 5. MAC Learning & MAC Reservation
*What is in a MAC Address?*

<br>

~~~
!@cmd
nmap -sP -sn 192.168.1.0/24
~~~

<br>

How switches forward data? __Frame Forwarding__

~~~
!@Windows
arp /a

!@Linux
arp -a
~~~

<br>

How to view the MAC addresses learned by the Switch? __SMAC - `show mac address-table`__
~~~
!@CoreBABA
show mac address-table
~~~

<br>

| Camera         | MAC Address      |
| ---            | ---              |
| Camera fa0/6   | #camera6macadd#  |
| Camera fa0/8   | #camera8macadd#  |

<br>

Assign a specific IP address to a device.


<br>


> __FAQ (Knowledge Database)__   
> Title: 5th Job of a Switch - MAC Learning & MAC Reservation   
> Symptom: Cameras have dynamic IP addresses
> Problem: Certain endpoints must have a static IP address
> Solution:  

<br>

~~~
!@CoreBABA
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

<br>

Verify DHCP: __SIDB - `show ip dhcp bindings`__

~~~
!@CoreBABA
show ip dhcp bindings
~~~


&nbsp;
---
&nbsp;


Review the jobs of a switch:
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;

 
<br>
<br>

---
&nbsp;


🔴 __CDP Flooding Attack__
Verify:
~~~
!@CoreBABA
show process cpu | inc uti
~~~


<br>
<br>

---
&nbsp;


## ITSM Change Process

### STEP 1 - User reports an issue to [Tier 1 NOC] with the internet slowing down  

__Ticket__  
- Type: Incident  
- To: [NOC] Tier 1 - Monitoring & First Response  
- Service: [NOC] Infrastructure & Application Monitoring  
- SLA: Performance Management SLA  
- Subject: Network Issue  
- Priority: 4 High  

<br>

- Text:   
~~~
The network is very slow, and we are unable to reliably connect to services such as servers and printers. 
Additionally, IP phone extensions/numbers are disappearing intermittently. 
This is impacting our ability to make and receive calls.
~~~


&nbsp;
---
&nbsp;


__Admin [Rivan Cyber] responds to ticket.__  
- Reply  
~~~
Hi user1,

Thank you for reporting this issue.

We are currently investigating the network performance problems and the IP phone registration issue. 
Initial checks show possible network congestion or a connectivity disruption affecting multiple services.

Thank you for your patience while we work to resolve this.

Best regards,
IT Support Team
~~~


<br>
<br>

---
&nbsp;


### STEP 2 - User checks the logs, then discover that Certain Switches have unusually high traffic.


<br>


__Change Owner__
- Subject: Network Issue T2 Escalation
- Text: 
~~~
Issue summary:
  Network extremely slow
  Cannot access servers and printers
  IP phones losing registration
  Multiple users affected

Troubleshooting performed by Tier 1:
  Verified issue affects multiple users
  Confirmed both wired/wireless impacted
  Restarted affected workstation(s)
  Verified no local NIC errors
  Basic connectivity tests failed/intermittent

Reason for escalation:
  Issue appears to be infrastructure-related (core switch / firewall / VoIP system). 
  Requires Tier 2 investigation.
~~~


&nbsp;
---
&nbsp;


__Update the User__
- Reply
~~~
Hi user1,

Your ticket has been escalated to our Tier 2 Network Team for further investigation. 
They are currently reviewing the infrastructure components involved.

We will provide updates as soon as more information is available.

Thank you for your patience.
~~~


<br>
<br>

---
&nbsp;


### STEP 3 - Create an ITSM Change with a Work Order for Change [Request] Creation 

__ITSM Change__
- Title: Implement Port Security on Access Switches to Prevent MAC Flooding
- Description: 
~~~
Network is currently slow caused by a traffic congestion from CoreSwitches
CoreSwitches consuming high CPU usage caused by a flood of MAC Addresses.
Switches are currently lacking proper security implementations to prevent L2 attacks.
~~~


<br>


- Justification:
~~~
CPU utilization for five seconds: 99%/0%; one minute: 6%; five minutes: 6%
 272           0           2          0  0.00%  0.00%  0.00%   0 Routing Topology
~~~


<br>


- Category: 4 High
- Impact: 4 High
- Priority: 4 High


&nbsp;
---
&nbsp;


__WorkOrder [REQUEST]__
- Title: Change Request Creation
- Workorder Type: Approval
- Planned Time: +1 Day
- Description:  
~~~
Users reported slow connectivity. Investigation identified high CPU utilization on Cisco access switch due to MAC address table flooding. The switch is vulnerable to MAC flooding attack.
Requesting change approval to implement port security configuration on affected access ports.


Reason for Change:
  Mitigate network traffic congestion.
  Prevent recurrence of MAC flooding attack.
  Improve switch stability.
  Enhance Layer 2 security posture.


Proposed Solution:
  Enable port security.
  Limit MAC addresses per port.
  Enable violation restrict/shutdown mode.
  Enable sticky MAC where applicable.
~~~


<br>
<br>

---
&nbsp;


### STEP 4 - Create a Work Order for [Impact Analysis] & Plan Assessment

__WorkOrder [IMPACT ANALYSIS]__  
- Title: Technical & Risk Assestment / Action Plan  
- Workorder Type: Approval  
- Planned Time: +1 Day  
- Description:  
~~~
Technical Analysis
Enabling port security may:
  Temporarily disrupt connected devices
  Cause port shutdown if misconfigured
  Requires maintenance window
  Minimal downtime expected (per access port configuration)
  
  
Risk Assessment:
Risk	            Likelihood	   Impact	Mitigation
Port shutdown	    Medium	       Medium	Configure restrict mode first
User disconnection	Low	Low	       Change   during maintenance window
Misconfiguration	Low	Medium	   Peer     review config


Impact Scope
Affected Devices:
Cisco Access Switch SW-ACC-01
SW-ACC-02


Affected Users:
Office Floor 2 (~45 users)
No impact to core or WAN


Backout Plan
!@Switch
conf t
 int range fa0/1-12
  no switchport port-security
  shut
  no shut
  end
~~~


<br>
<br>

---
&nbsp;


### STEP 5 - Create a Work Order for [Approval/Denial]

__Work Order [APPROVAL/DENIAL]__  
- Title:  CAB Review Approval/Denial  
- Workorder Type: Decision  
- Planned Time: +1 Day  
- Description:  
~~~
Approval Considerations
- Minimal downtime
- Security Imporvement
- Backout Plan

Decision:
 Proposed Maintenance Window
 Schedule: 22:00 - 23:30
~~~


<br>
<br>

---
&nbsp;


### STEP 6 - Create a Work Order for [Implementation]  

__Work Order [IMPLEMENTATION]__  
Title: Implementation Procedure   
- Workorder Type: Workorder  
- Planned Time: +1 Day  
- Description:  
~~~
Pre-implementation Tasks:
Backup Configs:

!@Cisco
copy run start
copy run ftp:

- Save external backup to TFTP
- Notify users of maintenance window
- Confirm monitoring alerts configured

Implementation:
PORT SECURITY
!@CoreBABA
conf t
interface range fa0/6,fa0/8
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security violation restrict
 switchport port-security mac-address sticky
end

DHCP SNOOPING
!@CoreBABA
conf t
 ip dhcp snooping
 ip dhcp snooping vlan 1,10,50,100
 !
 int po1
  ip dhcp snooping trust
  exit
 int fa0/1
  no ip dhcp snooping trust
  exit
 !
 no ip dhcp snooping information option
 !
 interface range fa0/1-12
  ip dhcp snooping limit rate 10
  end
show ip dhcp snooping
show ip dhcp snooping binding


DAI Dynamic Arp Inspection
!@CoreBABA
conf t
 ip arp inspection vlan 1,10,50,100
 !
 int po1
  ip arp inspection trust
  exit
 !
 arp access-list PC-HOST
  permit ip host 10.#$34T#.1.10 mac host ___.___.___.___
  exit
 ip arp inspection filter PC-HOST vlan 1
 !
 int fa0/1
  no ip arp inspection trust
  end
show ip arp inspection
show ip arp inspection statistics


~~~


<br>
<br>

---
&nbsp;


### STEP 7 - Create a Work Order for Post Implementation Review PIR [Report]  

__Work Order [REPORT/REVIEW]__  
Title: PIR Incident Report  
- Workorder Type: PIR  
- Planned Time: +1 Day  
- Description:  
~~~
Review Date: 3 days - 1 week after change

Port security was configured on the core switches to improve network security by limiting MAC addresses per port and preventing unauthorized device connections.
The objective was to enhance network access control and reduce the risk of rogue devices.

Observations
- CPU usage reduced from 85% → 18%
- No further MAC flooding detected
- No user complaints
- Port violations logged correctly

Lessons Learned
- Port security was not enabled by default
- Access switches lacked L2 security hardening baseline
- Need standard switch hardening template

~~~


<br>
<br>

---
&nbsp;


### STEP 8 - Create Conditions to allow Change States

__A Review on the 5 ITSM Change Process__

1. __REQUEST__

| OBJECT    | SELECTOR | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---      | ---       | ---      | ---              |
| WORKORDER | REQUEST  | STATE     | IS       | ACCEPTED         |
|           |          |           |          |                  |
| CHANGE    | 0000xxxx | STATE     | SET      | PENDING APPROVAL |


<br>

2. __IMPACT ANALYSIS__

| OBJECT    | SELECTOR         | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---              | ---       | ---      | ---              |
| WORKORDER | IMPACT ANALYSIS  | STATE     | IS       | ACCEPTED         |
|           |                  |           |          |                  |
| CHANGE    | 0000xxxx         | STATE     | SET      | APPROVED         |


<br>

3. __APPROVAL__

| OBJECT    | SELECTOR         | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---              | ---       | ---      | ---              |
| WORKORDER | APPROVAL         | STATE     | IS       | ACCEPTED         |
|           |                  |           |          |                  |
| CHANGE    | 0000xxxx         | STATE     | SET      | IN PROGRESS      |


<br>

4. __IMPLEMENTATION__

| OBJECT    | SELECTOR         | ATTRIBUTE | OPERATOR | VALUE            |
| ---       | ---              | ---       | ---      | ---              |
| WORKORDER | IMPLEMENTATION   | STATE     | IS       | ACCEPTED         |
|           |                  |           |          |                  |
| CHANGE    | 0000xxxx         | STATE     | SET      | PENDING PIR      |


<br>

5. __REVIEW/REPORT__

| OBJECT    | SELECTOR | ATTRIBUTE | OPERATOR | VALUE   |
| ---       | ---      | ---       | ---      | ---     |
| WORKORDER | REVIEW   | STATE     | IS       | CLOSED  |
|           |          |           |          |         |
| CHANGE    | 0000xxxx | STATE     | SET      | SUCCESS |


<br>
<br>

---
&nbsp;


### STEP 9 - Report on every single Work Order to Change states

1. __REQUEST__

<br>

Terms:
  __RFC (Request for Change)__   
  __Change Record__    
  __Change Initiator__   
  __Business Justification__    
  __Change Category__    
  __Priority__   


&nbsp;
---
&nbsp;


2. __IMPACT ANALYSIS__

<br>

Terms:  
  __Impact__  
  __Risk__  
  __Risk Matrix__  
  __CI (Configuration Item)__  
  __Dependency Mapping__  
  __Rollback Plan__  
  __Mitigation Plan__  

<br>


&nbsp;
---
&nbsp;


3. __APPROVAL/DENIAL__

<br>

Terms:  
  __CAB (Change Advisory Board)__   
  __ECAB__   
  __Change Manager__   
  __Approval Workflow__   
  __Segregation of Duties__    
  __Compliance & Audit Trail__    


&nbsp;
---
&nbsp;


4. IMPLEMENTATION

<br>

Terms:
  __Change Window__
  __Maintenance Window__
  __Work Orders__
  __Deployment Plan__
  __Backout Plan__
  __Release Management__
  __Technical Validation__

<br>

Control Mechanisms  
  - &nbsp;
  - &nbsp;
  - &nbsp;
  - &nbsp;
  

&nbsp;
---
&nbsp;

  
5. REVIEW/REPORT

<br>

Terms:  
  __PIR (Post Implementation Review)__  
  __RCA (Root Cause Analysis)__   
  __Lessons Learned__  
  __KPI Review__  
  __Change Success Rate__  
  __Continuous Improvement__  


<br>
<br>

---
&nbsp;


## 🔒 Secure Layer 2 Network
*Why should you buy an expensive switch?*

1. MAC Address Learning
2. MAC Address Filtering
3. MAC Address Forwarding
4. Layer 2 Loop Avoidance


&nbsp;
---
&nbsp;


### PortSec
*Ensure your devices don't get swapped.*
Guard the switchports so that it can't be replaced by hacking devices.

<br>

~~~
!@BABA
config t
 int fa0/6
  switchport mode access
  switchport port-security
  switchport port-security mac-address Sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
 int fa0/8
  switchport mode access
  switchport port-security
  switchport port-security mac-address Sticky
  switchport port-security maximum 1
  switchport port-security violation shutdown
  end
show port-security address
show int status err-disable
~~~

<br>

Make ports work again.

~~~
@CoreBABA
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
show int status err-disable
~~~


<br>
<br>

---
&nbsp;


### 📃 Full Script
<details>
<summary>Show Script</summary>
	
~~~
!@coreBaba
conf t
 hostname coreBaba-#$34T#
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
  ip add 10.#$34T#.#$34T#.4 255.255.255.0
 int vlan 1
  no shut
  ip add 10.#$34T#.1.4 255.255.255.0
  desc VLANMGMTDATA
 int vlan 10
  no shut
  ip add 10.#$34T#.10.4 255.255.255.0
  desc VLANMGMTWIFI
 int vlan 50
  no shut
  ip add 10.#$34T#.50.4 255.255.255.0
  desc VLANMGMTCCTV
 int vlan 100
  no shut
  ip add 10.#$34T#.100.4 255.255.255.0
  desc VLANMGMTVOICE
 end

!@switchport
conf t
 vlan 1
  name MGMTVLAN
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
 int fa 0/7
  switchport mode access
  switchport voice vlan 100
  switchport access vlan 1
 end

!@camera
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

</details>


<br>
<br>

---
&nbsp;


### 💾 Save the configurations
~~~
!@CoreTAAS & CoreBABA
copy run start
~~~


<br>
<br>

---
&nbsp;


## 🔧 Configure CUCM
### 📠 Enterprise Communication   

Cisco Unified Call Manager | [Unified Communications and Collaboration.](https://www.cisco.com/c/en/us/products/unified-communications/index.html)
  - POTS (__Analog__)
  - VOIP (__ePhone__)


<br>

> __CMDB__  
> Name: CUCM  
> Description:  Establish a Cybercrime hotline via Call Control System

<br>

| PBX (Private Branch Exchange) | PSTN (Public Switched Telephone Network)  |
| ---                           | ---                                       |
| Private Carrier               | Public Carrier Infrastructure             |
| Trad (Analog/Digital)         | Analog (POTS)                             |
| IP PBX (VoIP-Based)           | ISDN (Integrated Service Digital Network) |
| Cloud PBX (Hosted)            | T1/E1                                     |


&nbsp;
---
&nbsp;

### Requirements to make IP Phones Operational
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;
6. &nbsp;
7. &nbsp;


<br>

> __FAQ (Knowledge Database)__   
> Title: Bootstrap Configurations for CUCM   
> Symptom: Newly Procured  
> Problem: No Configurations  
> Solution:  

<br>

~~~
!@CUCM
conf t
 hostname CUCM-#$34T#
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
  ip add 10.#$34T#.100.8 255.255.255.0
 end
~~~

<br>
<br>

---
&nbsp;

### Know the jobs of a Call Manager

<br>

## ⚙️ 1. Analog Phones (RJ11)
*Why do companies still use Analog phones?*

<br>

> __FAQ (Knowledge Database)__   
> Title: 1st Job of a Call Manager - Analog Phones   
> Symptom: Busy dial when pressing any button  
> Problem: No DN Assigned  
> Solution:  

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

Verify Functionality:

~~~
!@CUCM
show dial-peer voice summary
csim start #$34T#00
~~~

&nbsp;
---
&nbsp;

Modify the tone of the phone.
~~~
!@CUCM
conf t
 voice-port 0/0/0
  cptone dutch
  end
~~~

<br>
<br>

---
&nbsp;

## ⚙️ 2. IP Phones (RJ45) - Cisco Skinny Client Control Protocol (SCCP)
*What kind of phones do enterprise use?*

### Requirements to make IP Phones Operational
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;
6. &nbsp;
7. &nbsp;


<br>

> __FAQ (Knowledge Database)__   
> Title: 2nd Job of a Call Manager - IP Phones   
> Symptom: Lack of IP Phone DN Configurations  
> Problem: No Configuration Files fo IP Phones  
> Solution:


<br>
<br>

---
&nbsp;

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
  end
~~~

<br>

*Why 10.#$34T#.100.8? __TFTP__*

<br>

Ephone 1 MAC: #ephone1macadd#  
Ephone 2 MAC: #ephone1macadd#  

&nbsp;
---
&nbsp;

~~~
!@CUCM
conf t
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
 ephone-dn 9
  number #$34T#99
 ephone 1
  mac-address #ephone1macadd#
  type 8945
  button 1:1 2:2 3:3 4:4
 ephone 2
  mac-address #ephone2macadd#
  type 8945
  button 1:5 2:6 3:7 4:8
  end
~~~

<br>

> [!TIP]
> Still no numbers? Because IP Phones need to generate configuration files. __MANDATORY__

<br>

~~~
!@CUCM
conf t
 telephony-service
  create cnf-files
 !
 ephone 1
  restart
 ephone 2
  restart
  end
~~~

<br>

> [!NOTE]
> Depending on the ephone, __`create cnf-files`__ will need to be pasted twice.

<br>
<br>

---
&nbsp;

## ⚙️ 3. Video Calls

> __FAQ (Knowledge Database)__   
> Title: 3rd Job of a Call Manager - Video Conference   
> Symptom: Lack of Video  
> Problem: Video does not activate during calls  
> Solution:

<br>

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

## ⚙️ 4. Allow Incoming & Outgoing Calls

> __FAQ (Knowledge Database)__   
> Title: 4th Job of a Call Manager - Incoming & Outgoing Calls   
> Symptom: Phone becomes busy when calling other branches  
> Problem: No configurations for Incoming/Outgoing Calls  
> Solution:


<br>

~~~
!@CUCM
conf t
 voice service voip
 ip address trusted list
  ipv4 0.0.0.0 0.0.0.0
 end
~~~

<br>

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

## ⚙️ 5. Interactive Voice Response System (IVRS)
*How do large call centers handle numerous calls?*

<br>

> __FAQ (Knowledge Database)__   
> Title: 5th Job of a Call Manager - IVRS   
> Symptom: Not enough individuals responding to calls.    
> Problem: Influx of incoming calls.  
> Solution:  

<br>

~~~
!@CUCM
config t
 dial-peer voice 69 voip
  service rivanaa out-bound
  destination-pattern #$34T#69
  session target ipv4:10.#$34T#.100.8
  incoming called-number #$34T#69
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
   param aa-pilot #$34T#69
  service rivanqueue flash:app-b-acd-3.0.0.2.tcl
   param queue-len 15
   param aa-hunt1 #$34T#00
   param aa-hunt2 #$34T#01
   param aa-hunt3 #$34T#22
   param aa-hunt4 #$34T#66
   param queue-manager-debugs 1
   param number-of-hunt-grps 4
   end
~~~

<br>

> [!WARNING]
Configurations for IVRS cannot be overwritten. In case of wrong configurations, paste the commands below to the call manager then repaste the correct IVRS configurations.

<br>

~~~
!@CUCM
config t
 application
  no service callqueue flash:app-b-acd-2.1.2.2.tcl
  no service rivanaa flash:app-b-acd-aa-2.1.2.2.tcl
  end
~~~

<br>
<br>

---
&nbsp;

Review the jobs of a call manager:
 1. &nbsp;
 2. &nbsp;
 3. &nbsp;
 4. &nbsp;
 5. &nbsp;
  
<br>
<br>

---
&nbsp;

### Requirements to make IP Phones Operational
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;
6. &nbsp;
7. &nbsp;

<br>

## SPAN
~~~
!@CoreBABA (Serial)
conf t
 monitor session 1 source interface fa0/3,fa0/5,fa0/7
 monitor session 1 destination interface fa0/1,fa0/9
 end
~~~

<br>

__Remove SPAN__
~~~
!@CoreBABA (Serial)
conf t
 no monitor session 1 source interface fa0/3,fa0/5,fa0/7
 no monitor session 1 destination interface fa0/1,fa0/9
 end
~~~

&nbsp;
---
&nbsp;

## ☁️ Remote Access | [JUMPSERVER](https://www.jumpserver.com/)
### 🎯 Exercies 06: Attempt to establish a telnet session with the call manager

<br>

Is the device pingable?

~~~
@cmd
10.#$34T#.100.8
~~~

<br>
<br>

---
&nbsp;

### 📃 Full Script

<details>
<summary>Show Script</summary>
	
~~~
!@CUCM
conf t
 hostname CUCM-#$34T#
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
  ip add 10.#$34T#.100.8 255.255.255.0
 end

!@alog & ephone
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
 ephone-dn 9
  number #$34T#99
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
 dial-peer voice 91 Voip
  destination-pattern 91..
  session target ipv4:10.91.100.8
  codec g711ULAW
 dial-peer voice 92 Voip
  destination-pattern 92..
  session target ipv4:10.92.100.8
  codec g711ULAW
 end
 
!@IVRS
config t
 dial-peer voice 69 voip
  service rivanaa out-bound
  destination-pattern #$34T#69
  session target ipv4:10.#$34T#.100.8
  incoming called-number #$34T#69
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
   param aa-pilot #$34T#69
  service rivanqueue flash:app-b-acd-3.0.0.2.tcl
   param queue-len 15
   param aa-hunt1 #$34T#00
   param aa-hunt2 #$34T#01
   param aa-hunt3 #$34T#22
   param aa-hunt4 #$34T#66
   param queue-manager-debugs 1
   param number-of-hunt-grps 4
   end
~~~

</details>

<br>
<br>

---
&nbsp;

### 💾 Save the configurations
~~~
!@CUCM
copy run start
~~~

<br>
<br>

---
&nbsp;

## 🌐 Site Connectivity
*When to use UTP and Fibre Optic*

<br>

[IEEE Ethernet Standards](https://www.ccnaacademy.com/2018/09/ieee-ethernet-standards_16.html)

  | Name            | Speed    | IEEE      |
  | ---             |  ---     | ---       |
  | Ethernet        | 10 Mbps  |           |
  | FastEthernet    | 100 Mbps |           |
  | GigEthernet     | 1 Gbps   |           |
  | TenGigEthernet  | 10 Gbps  |           |

<br>

  - RJ45 Jack
  - SFP (Small Form-factor Pluggable)

<br>

  | Copper                                           | Single-mode fiber                    |
  | ---                                              | ---                                  |
  | Conductor, Bedding, Sheathing                    | Core, Cladding, Coating              |
  | Affected by electrical and magnetic interference | Comprised of insulated glass strands |

<br>
<br>

---
&nbsp;

## 🔧 Configure EDGE
### 🏨 Establish connectivity to your enterprise.
*How do you gain access to the internet?*

&nbsp;
---
&nbsp;

*What is the maximum distance of a UTP cable? 100m?*

Network Scopes
  - 🏠 LAN                  Local Area Network
  - 🌎 WAN                  Wide Area Network

<br>

PLDT Home vs PLDT Enterprise
  - 🌃 MAN                  Metropolitan Area Network
                         PLDT Enterprise Metro Ethernet

<br>

Transport technologies
  - Leased Line
  - SDWAN
  - MPLS VPLS            (Pseudowire, L3 & L2)
  - VPN                  (EVPN)

<br>

*Why PLDT?*
  __Submarine Cable Map__

*Why NOT PLDT?*
  - Cabling
  - [Service Reliability](https://www.pldthome.com/termsandconditions)

&nbsp;
---
&nbsp;

*How to know if you are connected to PLDT? __SCN - `show cdp neighbor`__*

~~~
!@EDGE
show cdp neighbor
~~~

<br>
<br>

---
&nbsp;

> __FAQ (Knowledge Database)__   
> Title: Bootstrap Configurations for EDGE   
> Symptom: Newly Procured  
> Problem: No Configurations  
> Solution:

<br>

~~~
!@EDGE
conf t
 hostname EDGE-#$34T#
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line cons 0
  password pass
  login
  exec-timeout 0 0
  exit
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
<br>

---
&nbsp;

> __FAQ (Knowledge Database)__   
> Title: Jobs of an EDGE Router   
> Symptom: Newly Procured  
> Problem: No Configurations  
> Solution:

~~~
Jobs of an EDGE Router:
1. Static Routing 
2. Default Routing 
3. EIGRP Routing 
4. OSPF Routing 
5. BGP Routing 
~~~

<br>
<br>

### ⚙️ Configure routing protocols
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
 ip route 10.91.0.0 255.255.0.0 200.0.0.81 254
 ip route 10.92.0.0 255.255.0.0 200.0.0.82 254
 ip route 10.#$34T#.0.0 255.255.0.0 10.#$34T#.#$34T#.4 253
 no ip route 10.#$34T#.0.0 255.255.0.0 200.0.0.#$34T# 254
 end
~~~

<br>

~~~
!@CUCM
conf t
 ip routing
 ip route 0.0.0.0 0.0.0.0 10.#$34T#.100.4 254
 end
~~~

<br>

~~~
!@CoreBABA
conf t
 ip route 0.0.0.0 0.0.0.0 10.#$34T#.#$34T#.1 254
 end
~~~

&nbsp;
---
&nbsp;

Verify: *How can you check the list of routes?  __SIR - `show ip route`__*

~~~
!@CoreBABA, CUCM, EDGE
show ip route
~~~

&nbsp;
---
&nbsp;

*How do you configure routes on windows?*

~~~
!@cmd
route add 10.0.0.0 mask 255.0.0.0 10.#$34T#.1.4
route add 200.0.0.0 mask 255.255.255.0 10.#$34T#.1.4
~~~

<br>
<br>

---
&nbsp;

### ⚙️ 2. OSPF ROUTING
*At what capacity do you want your devices to run?*

~~~
!@edge
conf t
router ospf 1
router-id #$34T#.0.0.1
network 200.0.0.0 0.0.0.255 area 0
network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
network #$34T#.0.0.1 0.0.0.0 area 0
int gi 0/0/0
ip ospf network point-to-point
end
~~~

<br>

~~~
@coreBaba
conf t
router ospf 1
router-id 10.#$34T#.#$34T#.4
network 10.#$34T#.0.0 0.0.255.255 area 0
int gi0/1
ip ospf network point-to-point
~~~

<br>

~~~
@cucm
conf t
router ospf 1
router-id 10.#$34T#.100.8
network 10.#$34T#.100.0 0.0.0.255 area 0
end
~~~

&nbsp;
---
&nbsp;

*Verify: How to check if OSPF is working? <br>
  __SIP - `show ip protocols`__ <br>
  __SION - `show ip ospf neighbor`__ <br>
  __SIRO - `show ip route ospf`__* <br>

&nbsp;
---
&nbsp;

### Now that routing is in place, there's no need to jump to access CUCM.
Ping

~~~
!@cmd
ping 10.#$34T#.1.2                 CoreTAAS
ping 10.#$34T#.1.4                 CoreBABA
ping 10.#$34T#.100.8               CUCM
ping 10.#$34T#.#$34T#.1            EDGE
~~~

<br>
<br>

---
&nbsp;


### Dedicated Line vs Internet VPN

<br>
<br>

## 🧱 Setup a Firewall (CSR1000v)
   
<br>

__Ordinary Firewall vs NGFW__

<br>
<br>

### `fbi.gov`   vs   `neu.edu.ph`   vs   `dpwh.gov.ph`
- Threat Defense
- Intrusion Detection
- Open Ports: HTTP, HTTPS, SSH, DNS

<br>

__Setup CSR1000v__

~~~
conf t
 hostname FW-EDGE
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 192.168.103.11 255.255.255.0
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 end
wr
~~~
