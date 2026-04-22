# SDN Traffic Monitor and Firewall (POX)

## Project Overview
- Implements SDN using POX controller in Mininet
- Monitors packets in real-time
- Blocks traffic from specific host (h3)
- Demonstrates OpenFlow-based control
- Uses ping and iperf for testing

## Topology
         h1
         |
         |
         s1
       /     \
      |       |
     h2       h3
 - h1, h2, h3 are hosts  
- s1 is an Open vSwitch  
- Controller (POX) is remote and controls s1  

## Topology Details

- 3 hosts: h1 (10.0.0.1), h2 (10.0.0.2), h3 (10.0.0.3)  
- 1 switch: s1  
- Remote controller using POX  
- All hosts connected to a single switch  

## Requirements
- Ubuntu (20.04 / 22.04)
- Mininet
- POX Controller
- Open vSwitch

## Execution

## Terminal 1 - Controller
```bash
cd ~/pox
./pox.py openflow.of_01 ext.traffic_monitor
```

## Terminal 2 - Mininet
```bash
sudo mn --topo single,3 --controller remote
```
## Testing

### Connectivity
```bash
pingall
```

## Allowed Traffic
```bash
h1 ping h2
```

## Block Test
```bash
h3 ping h1
```

## Flow Table
```bash
sh ovs-ofctl dump-flows s1
```
## Throughput Test (Allowed Case)
```bash
h2 iperf -s &
h1 iperf -c h2
```

## Throughput Test (Blocked Case)
```bash
h3 iperf -s &
h1 iperf -c h3
```

## Results
- h1 ↔ h2: allowed
- h3 → others: blocked
- flows installed dynamically
- high throughput when allowed
- 
## Validation
- ping → connectivity
- iperf → performance
- ovs-ofctl → flow rules
- logs → packet monitoring
  
## Conclusion
- Demonstrates SDN-based monitoring and firewall
- Centralized control using POX
- Efficient traffic handling
  
## Author
Nandika Gupta
