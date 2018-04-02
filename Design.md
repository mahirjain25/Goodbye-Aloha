#### Objective: To explain what Distributed Queuing(DQ) is , and how MAC protocols built on DQ are more robust and suitable for modern systems than ALOHA based MAC protocols.

**DQ Mechanism**

1. DQ works in start topology networks with one coordinator and a number of devices. It has a dynamic and reconfigurable master-slave architecture.As the name suggests , the way DQ works is fully distributed in the sense that the coordinator of the network does not decide who , when and how the devices transmit. The only job of the coordinator is to broadcase minimum amount of awareness information into the network such that the devices can make autonomous and well-informed decision of when to transmit the data(or use the channel).

From the above statement , it can be concluded that 3 different types of information flow in the link:
  1. The normal collision-free data.
  2. Access requests transmitted by different devices.
  3. Feedback/control information broadcasted by the coordinator back to the network.

  The first type takes up a large part of transmission resources.(uplink or downlink)
  The second and third type take only a small part of resources(downlink)

  The DQ frame structure comsists of 3 parts:
    1. m slots for collision resolution.
    2. 1 slot for collision-free data.
    3. 1 slot for transmission of feedback information by the coordinator .

  This the operation of DQ:
    1. At the beginning of each frame , the devices which have data ready to transmit choose one of the 'm' contention slots to transmit something known as **Access Request Sequence(ARS)** . From the status of the coordinator , the access slots can
      [a] Be empty .
      [b] successful(only one ARS is decoded) or
      [c] Collision(more than one ARS is decoded).

   2. The coordinator broadcasts this information in the form of a **FeedBack Packet(FBP)** . Each of the device decodes this packet and executes certain rules of the protocol and decide to enter into one of the 2 queues.
      	a. Colliding devices enter the **Contention Resolution Queue(CRQ)** . A **tree-splitting algorithm** is used to resolve those contentions.
       	b. Succeeding devices enter the **Data Transmission Queue** . In this case , a FIFO Queue allows devices to transmit data in subsequent frames using the data-slot of the DQ Queue.

    The queue is represented in each device by 2 integer numbers.
      a. Length of the queue.
      b. Position of each device in the queue.

      Length of the queue is updated by the coordinator.

  To understand the working of DQ , it is important to understand the working of CRQ and DRQ.

##### Contention Resolustion Queue(CRQ) :
  **a**. The first stage is the **Contention Resolution** where a tree splitting algorithm is used to resolve the contention in groups.
   **b**. There are 2 parameters a device must calculate dynammically and keep them updated. They are [a]CRQ length , [b]Device position in the CRQ.
  **c**. The devices which occupy the first position in the CRQ will transmit a new ARS(Access Request Sequence) in the next frame selecting another access slot at random. The other devices back in the queue can switch to sleep mode when they do not have an oppurtunity to send any Access requests.
 **d**. After a device sends an ARS , it gets a feeback in the form of FeedBack Packet(FBP) whether it has got the channel access or not.

##### Data Transmission Queue(DRQ) :

 **a**. When the device gets a success feedback , it means that the contention is resolved. The device now is virtually organised into a Data Transmission Queue.
 **b**. The CRQ and DRQ work in parallel.(not with respect to a single device , but they function in parallel)
 **c**. A device must successfully exit CRQ to enter DTQ.
 **d**. The devices have to be updated with 2 parameters , [a]DTQ length , [b] Device position in DTQ.
 **e**. The device occupying the first position in DTQ transmits a data packet in the next frame. Therefore the other devices which cannot transmit data in the next frame can switch to sleep mode.


   This is the crux of the DQ based MAC protocol.
