# Web_Crawling-AKiPS
AKiPS is a network monitoring tool using SNMP. In order to get the data you want, there are cases where you need to know the specific MIB and retrieve the information. However, it was developed by judging that the desired information can be dynamically obtained by crawling the information already seen in the dashboard.

## Main logic
  - Reqeust a device list to AKiPS  
  - Access to the jumpbox  
  - Access to the device  
  - Gather a interface list with "down" status from each device
  - Using this interface to retrieve running-configuration (sh run int xxx) and check it has shutdown configuration
  - Save as a xlsx file
