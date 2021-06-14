# Web_Crawling-AKiPS
AKiPS is a network monitoring tool using SNMP. Usually I need to know the specific MIB or data search syntax provided by AKiPS to get some information. Since the dashboard already displays a lot of valuable information, I thought it would be good to use web crawling to gather information dynamically. Since Selenium has more flexibility than BeautifulSoup so I used Selenium to search the first assigned IP address from the switch-port-mapper page. The source code contains a keyboard input and a mouse action.

## Main logic
  - Login the AKiPS server 
  - Navigate to events dashboard (Dashboards >> Evnets)  
  - Access to div tag with {class:left} attribute  
  - Gather a list of tables then access the second table (FYI, first one is Impact Assessment)  

## Update - 06/14/2021 (Added Selenium Crawling logic)
  - Login the AKiPS server
  - Navigate to Switch Port Mapper
  - Use specific xpath: /html/body/table/tbody/tr[2]/td[6]
  - Gather a list of the first assigned IP address (A device might have multiple IP address assigned logs)
