#class_note

## SDN_concept

Practical Challenges

* Scalability
  The controller needs to be responsible for many switches
* Response time
* Reliability
  The network should survive the failures of the controller and switches
* Consistency
  If multiple controllers are used at the same time, they should behave consistently
* Security
  Network vulnerable to attacks on the controller 
* Interoperability
  Should be able to co-work with legacy switches during transition period 

## OpenFlow

### LBP: Learning Bridge Protocol

### LLDP: Link Layer Discovery Protocol

Flow modify -> <br>
controller packet out to add LLDP flows with output action -> <br>
switch packet in to controller with LLDP response -> <br>
spanning tree (keep alive!)
