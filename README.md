# Web_Crawling-AKiPS
AKiPS is a network monitoring tool using SNMP. Usually I need to know the specific MIB or data search syntax provided by AKiPS to get some information. Since the dashboard already displays a lot of valuable information, I thought it would be good to use web crawling to gather information dynamically.

## Main logic
  - Login the AKiPS server 
  - Navigate to events dashboard (Dashboards >> Evnets)  
  - Access to div tag with {class:left} attribute  
  - Gather a list of tables then access the second table (FYI, first one is Impact Assessment)  
