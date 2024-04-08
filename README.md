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
Here i show you howto setup the Brother QL 810W Label Printer.
## 1. design your Label with the P-Touch Label Software. 
You'l find my templates is located in the folder p-touch-templates, this should be a good point to start with.
## 2. Transfer Templates to the Printer
  * This can be done with the `P-Touch Transfer Manager` (I used Version 2.5.004) or by  
  * starting the `P-Touch Transfer Manager` from the `P-Touch Editor` <br>
    In the German Version it is done via `Datei/Vorlage übertragen/übertragen`
  * You have to take care, that the `Schlüsselzuordnung` contains the numbers of the template as handles by the printer.
    * The Printer is connected vis USB
    * The Field `Schlüsselzuordnung` (maybe `keyvalue` in English) contains the numbers of the template as handled by the printer.
  * Then you can transfer the Templates to Printer by clicking `Übertragen` (maybe `transfer` in English) 

![Screenshot of P-Touch Editor](/images/transfer_editor.png)
![Screenshot of P-Touch Transfer Manager](/images/transfer_manager.png)
