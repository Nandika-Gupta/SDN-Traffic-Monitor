# SDN Traffic Monitor and Firewall (POX)

## Project Overview
- Implements SDN using POX controller in Mininet
- Monitors packets in real-time
- Blocks traffic from specific host (h3)
- Demonstrates OpenFlow-based control
- Uses ping and iperf for testing

## Topology

- 3 hosts, 1 switch, remote controller

## Requirements
- Ubuntu (20.04 / 22.04)
- Mininet
- POX Controller
- Open vSwitch

## Execution

## Terminal 1
```bash
cd ~/pox
./pox.py ext.traffic_monitor

## Terminal 2
```bash
sudo mn --topo single,3 --controller remote

## Testing

### Connectivity
```bash
pingall

## Block Test
```bash
h3 ping h1

## Allowed Traffic
```bash
h1 ping h2

## Flow Table
```bash
sh ovs-ofctl dump-flows s1

## Throughput (iperf)
```bash
h3 iperf -s &
h1 iperf -c h3

## Results
- h1 ↔ h2: allowed
- h3 → others: blocked
- flows installed dynamically
- high throughput when allowed
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
