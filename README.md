# Web_Crawling-AKiPS
AKiPS is a network monitoring tool using SNMP. Usually I need to know the specific MIB or data search syntax provided by AKiPS to get some information. Since the dashboard already displays a lot of information, I thought it would be good to use web crawling.

## Main logic
  - Reqeust a device list to AKiPS  
  - Access to the jumpbox  
  - Access to the device  
  - Gather a interface list with "down" status from each device
  - Using this interface to retrieve running-configuration (sh run int xxx) and check it has shutdown configuration
  - Save as a xlsx file
