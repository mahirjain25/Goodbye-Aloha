#!/usr/bin/awk -f

BEGIN {
	received=0;
	dropped=0;
	start_time = 0;
	stop_time = 0;
	total_recvd_packet_size = 0;
}

{
	event = $1;
	time = $2;
	packet_size = $6;
	packet_type = $5;

	if(packet_type=="cbr") {		#Main check.
		if(event=="r") {					#Block only for received packets.
			received++;
			total_recvd_packet_size += packet_size;

			if(time > stop_time) {
				stop_time = time;
			}
		}
		else if(event=="d") {			#Block only for dropped packets.
			dropped++;
		}
		else if(event=="s" || event=="+") {		#Block only for sent packets.
			if(!start_time || time < start_time) {
				start_time = time;
			}
		}
	}
}

END {
	printf("Packets received = %d\n" , received);
	printf("Packets dropped = %d\n" , dropped);
	printf("Packet Drop Rate[PDR] = %f\n\n" , 100 * ((float)(dropped) / (received + dropped)));
	printf("Throughput = %f kbps\n" , ((float)(total_recvd_packet_size) / (stop_time - start_time)) * 0.008);
}
