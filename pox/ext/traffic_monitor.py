from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ipv4 import ipv4

log = core.getLogger()

# Counters
packet_count = 0
blocked_count = 0
allowed_count = 0

def _handle_PacketIn(event):
    global packet_count, blocked_count, allowed_count

    packet = event.parsed
    if not packet:
        return

    src = packet.src
    dst = packet.dst

    # Count packets
    packet_count += 1
    log.info("\nPacket #%d\n   From: %s\n   To:   %s",
             packet_count, src, dst)

    # Block traffic from h3 (IP-based)
    if packet.type == 0x0800:
        ip = packet.next
        if isinstance(ip, ipv4):
            if str(ip.srcip) == "10.0.0.3":
                blocked_count += 1
                log.info("Blocked traffic from h3 (IP)\n---------------------")
                return

    # Allowed traffic
    allowed_count += 1

    # Forward remaining traffic
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

    # Report
    if packet_count % 10 == 0:
        log.info("\n===== TRAFFIC REPORT =====")
        log.info("Total Packets: %d", packet_count)
        log.info("Allowed Packets: %d", allowed_count)
        log.info("Blocked Packets: %d", blocked_count)
        log.info("==========================\n")


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Traffic Monitor and Filter Controller Started")
