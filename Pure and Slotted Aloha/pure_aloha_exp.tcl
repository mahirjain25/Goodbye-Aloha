#This is the implementation of pure aloha which will contain a lot
#of packet drops. Just to prove aloha is a bad protocol and to prove
#that we have a better protocol with us.


if { $argc != 2 } {
  puts "Usage: ns $argv0 <number of nodes> <pure_aloha--1/slotted_aloha--2>"
  exit 0
}

if { [lindex $argv 0] <= 0} {
  puts "Number of nodes cannot be negative. Exitting..."
  exit 0
}

global ns
set ns [new Simulator]

global macType

$ns rtproto DV
if { [lindex $argv 1] == 1} {
  $ns macType Mac/Sat/UnslottedAloha
} elseif { [lindex $argv 1] == 2} {
  $ns macType Mac/Sat/SlottedAloha
} else {
  puts "Invalid option for MAC Protocol has been chosen. Exiting..."
  exit 0
}

set node_count [lindex $argv 1]

set tracefile [open highdrop_aloha.tr w]
$ns trace-all $tracefile

set namfile [open highdrop_aloha.nam w]
$ns namtrace-all $namfile

proc finish { } {
  global ns tracefile namfile
  $ns flush-trace
  close $tracefile
  close $namfile
  exit 0
}

#This "hub" node is the centre of our star topology.
set hub [$ns node]
set udp100 [new Agent/UDP]
set cbr100 [new Application/Traffic/CBR]
$ns attach-agent $hub $udp100
$cbr100 attach-agent $udp100
$cbr100 set packetSize_ 500
$cbr100 set interval_ 0.005


#Create 100 nodes in the topology.
#Set the network configuration of the "node_count" number of nodes.

set n []
set udp []
set cbr []

for { set i 0 } { $i < $node_count } { incr i} {

#Create the node. Create the link between the hub and node.
  lappend n [$ns node]
  $ns duplex-link [lindex $n $i] $hub 10Mb 1ms DropTail

#Create a transport layer agent. Attach that protocol/agent with the node.
  lappend udp [new Agent/UDP]
  $ns attach-agent [lindex $n $i ] [lindex $udp $i]

#Create an application layer agent.Attach it to transport layer protocol.
  lappend cbr [new Application/Traffic/CBR]
  [lindex $cbr $i] attach-agent [lindex $udp $i]

#Set attributes.
  [lindex $cbr $i] set packetSize_ 500
  [lindex $cbr $i] set interval_ 0.000005

  $ns connect [lindex $udp $i] $udp100
}

#Schedule the events for the CBR agent and network dynamics.
#This is the place where we can make it get high packet drops.

for {set i 0 } { $i < 10 } { incr i} {
  if  {$i == 1} {
    $ns at 0.5 "[lindex $cbr 15] start"
    $ns at 0.5 "[lindex $cbr 27] start"
  } elseif {$i == 4} {
    $ns at 4.0 "[lindex $cbr 38] start"
    $ns at 7.0 "[lindex $cbr 51] start"
  } elseif {$i == 9} {
    $ns at 8.0 "[lindex $cbr 63] start"
    $ns at 9.0 "[lindex $cbr 89] start"
  } else {
      continue;
    }
  }

  $ns at 15.0 "[lindex $cbr 15] stop"
  $ns at 15.0 "[lindex $cbr 27] stop"
  $ns at 15.0 "[lindex $cbr 38] stop"
  $ns at 15.0 "[lindex $cbr 51] stop"
  $ns at 15.0 "[lindex $cbr 63] stop"
  $ns at 15.0 "[lindex $cbr 89] stop"



#At the end , call the finish routine.
$ns at 20.0 "finish"

#Run the simulation.
$ns run
