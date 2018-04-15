#!/usr/bin/awk -f

#This awk script is run on a .tr file(trace file) to get the Packet Drop Rate(PDR) and throughput.
#This script can be used to analyze any trace file whose entries contain the "cbr" protocol.

#BEGIN block initialises the variables required.

BEGIN {
	received=0;
	dropped=0;
	start_time = 0;
	stop_time = 0;
	total_recvd_packet_size = 0;
}

#The below block iterates through the trace file line by line(entry by entry) and grabs the required information.

{
	event = $1;
	time = $2;
	packet_size = $6;
	packet_type = $5;

	if(packet_type=="cbr") {		#Check if the protocol entry / packet type is "cbr"
		if(event=="r") {					#Block of code only for entries whose event is 'r' / packet received.
			received++;
			total_recvd_packet_size += packet_size;

			if(time > stop_time) {
				stop_time = time;
			}
		}
		else if(event=="d") {			#Block of code only for entries whose event is 'd' / dropped packets.
			dropped++;
		}
		else if(event=="s" || event=="+") {				#Block of code only for sent packets.
			if(!start_time || time < start_time) {
				start_time = time;
			}
		}
	}
}

#The END Block prints the metrics calculated.

END {
	printf("Packets received = %d\n" , received);
	printf("Packets dropped = %d\n" , dropped);
	printf("Packet Drop Rate[PDR] = %f\n\n" , 100 * ((float)(dropped) / (received + dropped)));
	printf("Start time = %f, Stop time = %f\n" , start_time, stop_time);

	printf("Throughput = %f kbps\n" , ((float)(total_recvd_packet_size) / (stop_time - start_time)) * 0.008);
}
