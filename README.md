# Data Communications (CO250): Mini Project

### Title:
Goodbye ALOHA!

### Group Members:

Mahir Jain (16CO123) - mahirjain25@gmail.com

Suraj Singh (16CO146) - surajnitk4@gmail.com

Adwait Gautham (16CO203) - adwait.gautham@gmail.com

### Abstract:

The vision of the Internet of Things (IoT) to interconnect and Internet-connect everyday people, objects, and machines poses new challenges in the design of wireless communication networks. The design of medium access control (MAC) protocols has been traditionally an intense area of research due to their high impact on the overall performance of wireless communications. The majority of research activities in this field deal with different variations of protocols somehow based on ALOHA, either with or without listen before talk, i.e., carrier sensing multiple access. These protocols operate well under low traffic loads and low number of simultaneous devices. However, they suffer from congestion as the traffic load and the number of devices increase. For this reason, unless revisited, the MAC layer can become a bottleneck for the success of the IoT. This paper describes the current limitations and envisioned challenges for the near future. Motivated by those, we identify a family of simple algorithms based on distributed queueing (DQ), which can operate for an infinite number of devices generating any traffic load and pattern. A description of the DQ mechanism is provided and most relevant existing studies of DQ applied in different scenarios are described in this paper. Finally, a description of the very first demo of DQ is also included in this paper.

### Tools Used:

The **ns2** software tool is being used to implement Pure and Slotted ALOHA. **MATLAB** is being used to implement the concept mentioned in the chosen paper.


### References:
A. Laya, C. Kalalas, F. Vazquez-Gallego, L. Alonso and J. Alonso-Zarate, "Goodbye, ALOHA!," in IEEE Access, vol. 4, pp. 2029-2044, 2016. [Click Here](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7457611)

## File Structure
- Introduction.md - Description of the theoretical aspects of the project with the help of diagrams shown in the paper
- Design.md - Designing the solution
- Pure and Slotted Aloha - A folder with all files pertaining to pure and slotted ALOHA. It contains the .tcl, .nam, .tr and .awk scripts.
- Contention Resolution Implementation - A folder with all files pertaining to the new algorithm being implemented.
