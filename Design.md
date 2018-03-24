
**Objective**: To explain what Distributed Queuing(DQ) is , and how MAC protocols built on DQ are more robust and suitable for modern systems than ALOHA based MAC protocols.

**DQ Mechanism**

1. DQ works in start topology networks with one coordinator and a number of devices. It has a dynamic and reconfigurable master-slave architecture.As the name suggests , the way DQ works is fully distributed in the sense that the coordinator of the network does not decide who , when and how the devices transmit. The only job of the coordinator is to broadcase minimum amount of awareness information into the network such that the devices can make autonomous and well-informed decision of when to transmit the data(or use the channel).

From the above statement , it can be concluded that 3 different types of information flow in the link:
 - The normal collision-free data.
 - Access requests transmitted by different devices.
 - Feedback/control information broadcasted by the coordinator back to the network.

  The first type takes up a large part of transmission resources.(uplink or downlink)
  The second and third type take only a small part of resources(downlink)

  The DQ frame structure comsists of 3 parts:
    1. m slots for collision resolution.
    2. 1 slot for collision-free data.
    3. 1 slot for transmission of feedback information by the coordinator .

  This the operation of DQ:
    1. At the beginning of each frame , the devices which have data ready to transmit choose one of the 'm' contention slots to transmit something known as **Access Request Sequence(ARS)** . From the status of the coordinator , the access slots can

 - be empty
 - be successful (only one ARS in decoded) or
 - be a collision (more than one ARS is decoded)
 
2. The coordinator broadcasts this information in the form of a Feedback Packet  **(FBP)**. Each device decodes this packet and executes certain rules of the protocol and decide to enter one of the two queues. 

 - Colliding devices enter the **Contention Resolution Queue(CRQ)** . A **tree-splitting algorithm** is used to resolve those contentions.
 - Succeeding devices enter the **Data Transmission Queue** . In this case , a FIFO Queue allows devices to transmit data in subsequent frames using the data-slot of the DQ Queue.


The queue is represented in each device by two integer numbers:

 - Length of the queue
 - Position of each device in the queue
 (The length of the queue is updated by the coordinator)
 
  To understand the working of DQ , it is important to understand the working of Contention Resolution Queue **(CRQ)** and Data Transmission Queue **(DRQ)**.


This is the design of the DQ based Protocol.

