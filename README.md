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
    - The Item is added to a ToDo-List called **froster**.

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
  * starting the `P-Touch Transfer Manager` from the `P-Touch Editor` <br />
    In the German Version it is done via `Datei/Vorlage übertragen/übertragen`
![Screenshot of P-Touch Editor](/images/transfer_editor.png)
  * You have to take care, that the `Schlüsselzuordnung` contains the numbers of the template as handles by the printer.
    * The Printer is connected vis USB
    * The Field `Schlüsselzuordnung` (maybe `keyvalue` in English) contains the numbers of the template as handled by the printer.
  * Then you can transfer the Templates to Printer by clicking `Übertragen` (maybe `transfer` in English) 
![Screenshot of P-Touch Transfer Manager](/images/transfer_manager.png)
## 3. Activate WiFi on the Printer
  * Set the Printer that it can be accessed via WiFi and write down his IP-Address e.g.: `203.0.113.80`
## 4. Test Template Print
  * To test the Template-Printing via WiFi use any Unix Shell with netcat ant type:<br />
    `echo -e "^II\n^TS002\nBolognese\t550g\t22.02.2022\n^FF" | nc -N 203.0.113.80 9100`<br />
    be sure to change the IP-Adress to the one of your printer.

# Store python-script in /config folder
  * Store the python-scripts <br />
    `print_t1.py` and <br />
    `print_t2.py` <br />
    in the Config-Folder of your Home-Assistant installation<br /> (where your configuration.yaml is stored).
  * Edit the python-scripts
    * Change `host = '203.0.113.80'` to match the IP-Address of your Printer
  * Test python-scripts by running the follwing commands
    * `python3 print_t1.py -t "Hello World"`
    * `python3 print_t2.py -p "Bolognese" -m "666g"`

# Add Shell-Command to your configuration.yaml 
<code yaml>
shell_command:
  # Print labels on Brother QL810W
  print_t1: 'python print_t1.py -t "{{ states("input_text.label_text") }}"'
  print_t2: 'python print_t2.py -p "{{ states("input_text.label_produkt") }}" -m "{{ states("input_text.label_menge") }}"'
</code>

# Add Helpers to Home-Assistant 
I have Boxes in different Colors in square and rectangular and covers in other colors.<br />
I store Box and Cover-Color as well as geometry to be able to find a desires box easier.<br />
To mmet this requirements, we need the following Helpers, you can change them to meet your needs.<br />
## Text
  * `Helper/Add Helper/Text`
    * "name": "Text"
    * "min": 0,
    * "max": 100,
    * Edit Helper and set ID to `input_text.label_text` 
  * `Helper/Add Helper/Text`
    * "name": "Produkt"
    * "min": 1,
    * "max": 100,
    * Edit Helper and set ID to `input_text.label_produkt` 
  * `Helper/Add Helper/Text`
    * "name": "Menge"
    * "min": 0,
    * "max": 10,
    * Edit Helper and set ID to `input_text.label_menge` 
## Dropdowns
  * `Helper/Add Helper/Dropdown`
    * "name": "Dose"
    * "icon": "mdi:cog-box"
    * "options": "transparent", "red", "green", "yellow", "blue"
    * Edit Helper and set ID to `input_select.dose` 
  * `Helper/Add Helper/Dropdown`
    * "name": "Deckel"
    * "icon": "mdi:checkbox-blank-circle-outline"
    * "options": "green", "yellow", "blue"
    * Edit Helper and set ID to `input_select.deckel` 
  * `Helper/Add Helper/Dropdown`
    * "name": "Form"
    * "icon": "mdi:rectangle-outline"
    * "options": "square", "rectangular"
    * Edit Helper and set ID to `input_select.form` 
    
# Add three Scripts to Home-Assistant 
You'll find the yaml-code of the scripts in the `/scripts`-directory.
  * `Scripts/Add Scripts/Yaml`
  * paste the scripts <br />
    `Print Text Label.txt`, <br />
    `Print Froster Label.txt` and <br />
    `Print Froster Label List.txt` <br />
  
# Add cards to your Dashboard
You'll find the yaml-code of the cards in the `/lovelance`-directory.
  * `goto a dashboard of your coice`
  * `edit`
  * `add card` and choose any 
  * activate `yaml`-mode 
  * paste code from `/lovelance`-directory

Have fun.
