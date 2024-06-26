# homeassistant-frosterlabels
To connect the Power of Home-Assistant with Label-Printer to print Froster-Labels and maintain a List of the Content of your Froster.
# Overview 
To print Froster-Labels and add the items to the Content-List of my Froster I use the following Workflow:
  - In the Gui I enter the details of a product being added to the froster. <br />
    Additional Infos can be entered in my case: 
    * Weight/Amount
    * Color of the Container
    * Color of the Cover
    * Format of the Container
  - by pressing a Button 
    - A label is printed with "Product", "Weight/Amount" and the actual Date and
    - the Item is added to a ToDo-List called **froster**.

Now I am able to see the content of my froster in the ToDo list. <br />
When I take Items out, i can check them and they gonna be deleted from the List.

## Requirements 
   * Label Printer **Brother QL 810W**

The Brother QL 810W has the possibility to store a template and print this template with Ad-Hoc provided date with a simple TCP/IP packet. <br />
If you don't own this printer you have to find a possibility to print a label using a shell command e.g.: `/usr/local/bin/printlabel -p PRODUCT -m AMMOUNT`

## Environment 
My Home-Assistant runs as a Docker-Container, but I think this tutorial can also be applied to other Home-Assistant types of installation.

# Brother QL 810W Label Templates
Howto generate and store Templates for the Brother QL 810W Label Printer.
## Design your Label with the P-Touch Label Software. 
You'l find my templates is located in the folder p-touch-templates, this should be a good point to start with.<br />
There are two Templates
  * `template_text.lbx` only one textfield
  * `template_froster.lbx` three textfields for product, ammount and date.

## Transfer Templates to the Printer
  * This can be done with the `P-Touch Transfer Manager` (I used Version 2.5.004) or by  
  * starting the `P-Touch Transfer Manager` from the `P-Touch Editor` <br />
    In the German Version it is done via `Datei/Vorlage übertragen/übertragen`<br /><br />
![Screenshot of P-Touch Editor](/images/transfer_editor.png)<br />
  * You have to take care, that the `Schlüsselzuordnung` contains the numbers of the template position, wehre it is stored in the printer.
    * The Printer must bee connected via USB.
    * The Field `Schlüsselzuordnung` (maybe `keyvalue` in English) contains the numbers of the template as handled by the printer.
  * Then you can transfer the Templates to Printer by clicking `Übertragen` (maybe `transfer` in English) <br /><br />
![Screenshot of P-Touch Transfer Manager](/images/transfer_manager.png)<

## Activate WiFi on the Printer
  * Set the Printer that it can be accessed via WiFi and write down his IP-Address e.g.: `203.0.113.80`
## Test Template Print
  * To test the Template-Printing via WiFi use any Unix Shell with netcat ant type:<br />
    `echo -e "^II\n^TS002\nBolognese\t550g\t22.02.2022\n^FF" | nc -N 203.0.113.80 9100`<br />
    be sure to change the IP-Address to the one of your printer.

# Store python-script in /config folder
  * Store the python-scripts <br />
    `print_t1.py` and <br />
    `print_t2.py` <br />
    in the Config-Folder of your Home-Assistant installation (where your configuration.yaml is stored).
  * Edit the python-scripts
    * Change `host = '203.0.113.80'` to match the IP-Address of your Printer
  * Test python-scripts by running the follwing commands
    * `python3 print_t1.py -t "Hello World"`
    * `python3 print_t2.py -p "Bolognese" -m "666g"`

# Settings in Home Assistant 
## Add Shell-Command to your configuration.yaml 
append this to your configuration.yaml 

```
shell_command:
  # Print labels on Brother QL810W
  print_t1: 'python print_t1.py -t "{{ states("input_text.label_text") }}"'
  print_t2: 'python print_t2.py -p "{{ states("input_text.label_produkt") }}" -m "{{ states("input_text.label_menge") }}"'
```

## Add Helpers to Home-Assistant 
I have containers and covers in different colors and in squared and rectangular shapes.<br />
I store Container- and Cover-Color as well as geometry to be able to find a desired container easier in the froster.<br />
To meet this requirements, we need the following helpers, you may change them to meet your needs.<br />
### Text
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
### Dropdowns
  * `Helper/Add Helper/Dropdown`
    * "name": "Dose"
    * "icon": "mdi:cog-box"
    * "options": "transparent", "rot", "grün", "gelb", "blau"
    * Edit Helper and set ID to `input_select.dosenfarbe` 
  * `Helper/Add Helper/Dropdown`
    * "name": "Deckel"
    * "icon": "mdi:checkbox-blank-circle-outline"
    * "options": "grün", "gelb", "blau"
    * Edit Helper and set ID to `input_select.deckelfarbe` 
  * `Helper/Add Helper/Dropdown`
    * "name": "Form"
    * "icon": "mdi:rectangle-outline"
    * "options": "Originalverpackung", "qwuadratisch", "rechteckig"
    * Edit Helper and set ID to `input_select.dosenform` 
    
## Add thist Scripts to Home-Assistant 
You'll find the yaml-code of the scripts in the `/scripts`-directory.
Add the Froster Manager Script:
  * `Settings/Automations & Scenes/Scripts/New ScriptCreate/New Script`
    * Name: Froster Manager
    * Entity-ID: script.froster_manager<br />
    * Switch to YAML Mode and paste: `Frostermanager.yaml`, <br />
Add the Print Test Label Script:
  * `Settings/Automations & Scenes/Scripts/New ScriptCreate/New Script`
    * Name: Print Text Label
    * Entity-ID: script.print_text_label<br />
    * Switch to YAML Mode and paste: `PrintTextLabel.yaml`, <br />
  
## Add cards to your Dashboard
You'll find the yaml-code of the cards in the `/lovelance`-directory.
  * `goto a dashboard of your coice`
  * `edit`
  * `add card` and choose any 
  * activate `yaml`-mode 
  * paste code from `/lovelance`-directory<br /><br />

![Screenshot of Home-Assistant Cards](/images/lovelance_froster_product.png)<br /><br />
![Screenshot of Home-Assistant Cards](/images/lovelance_froster_list.png)<br /><br />
![Screenshot of Home-Assistant Cards](/images/lovelance_label_print.png)<br /><br />

Have fun.
