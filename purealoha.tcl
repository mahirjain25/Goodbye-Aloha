set ns [new Simulator]

$ns rtproto DV
$ns macType Mac/Sat/UnslottedAloha

set nf [open aloha.nam w]
$ns namtrace-all $nf
#Open the output files
set f0 [open aloha.tr w]
$ns trace-all $f0
#Define a finish procedure
proc finish {} {
global ns f0 nf
$ns flush-trace
#Close the trace file
close $f0
close $nf 
exec nam aloha.nam &
exit 0 
}
