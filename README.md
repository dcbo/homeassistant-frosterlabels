# homeassistant-frosterlabels
To connect the Power of Home-Assistant with a froster
# Overview 
To connect the Power of Home-Assistant with my froster I use the following Workflow:
  - In the Gui I enter the details of a product being added to the froster. Additional Infos can be entered in my case: 
    * Weight/Amount
    * Color of the Box
    * Format of the Box
    * Color of the Cover
  - by pressing a Button 
    - A label is printed with "Product", "Weight/Amount" and "actual Date"
    - The Item is added to a ToDo-List calles froster.
Now I am able to see the content of my froster in the ToDo list. When I take out the Items, i can check them in the List and they gonna be deleted from the List.

## Requirements 
   * Label Printer **Brother QL 810W**

The Brother QL 810W has the possibility to store a template and print this template with Ad-Hoc provided date with a simple TCP/IP packet. 
If you don't have this printer you have to find a possibility to print a label using a shell command e.g.: `/usr/local/bin/printlabel -p PRODUCT -m AMMOUNT`

## Environment 
My Home-Assistant runs as a Docker-Container, but I think this can also be applied to other Home-Assistant ways of installation.

# Label Template 
First you will have to design your Label with the P-Touch Label Software. You'l find my templates is located in the folder p-touch-templates
`c:\Users\$USER\AppData\Roaming\Brother\P-touch Editor\LayoutStyle\Roll\`

