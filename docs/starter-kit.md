<div class="page-headers">
<h1>Starter Kit </h1>
</div>

This starter kit empowers you how to map your first line of the electrical transmission grid. If you ever get stuck with the Starter Kit or would like to provide feedback, please contact us via our [community chat](https://discord.gg/fBw7ARTUeR) or <a href="mailto:MapYourGrid@openenergytransition.org" target="_blank" rel="noopener"> via email</a>. A MapYourGrid member will help you finish your first line and set up your environment.

<div style="float: right; margin: 5px 0 20px 20px; width: 350px;">
  
  <img src="../images/openinframap-portugal.jpg" class="img-border" style="width: 100%;"> 
  <figcaption class="image-caption"><a href="https://openinframap.org/#6.54/39.026/-7.548" target="_blank">Open Infrastructure Map</a> showing the detailed transmission and distribution grid in Portugal. Click to enlarge.</figcaption>
</div>

For professional large scale grid mapping, editing lines the visualkkization of the total electrical grid in your editor we recommend JOSM. However, if you only want to add small changes, edits, notes or fixme tags, the iD editor in combination with OpenInframap and MapComplete might be the ideal tools. These tools also provide much better usability for field mapping tasks if you want to validate data. Click on of the two tutorials you would like to start with:

1. [JOSM Starter Kit for large scale mapping](starter-kit.md#josm-starter-kit)
2. [iD and MapComplete for small scale mapping and field mapping](starter-kit.md#id-and-mapcomplete-starter-kit) 

## <div class="stradegy-header">JOSM Starter Kit</div></h3>
    
### **<div class="tools-header">1. Install and Configure JOSM  <img src="../images/josm_logo.jpg" style="height: 1.2em; vertical-align: middle; margin-left: 10px;"></div>** 


<div style="float: right; margin: 5px 0 20px 20px; width: 350px;">
  <img src="../images/starter-kit/kenya-tanzania.jpg" class="img-border" style="width: 100%;"> </a>
  <figcaption class="image-caption">This is what your JOSM should look like after setting up the Starter-Kit. Click to enlarge.</figcaption>
  <img src="../images/preferences.jpg" class="img-border" style="width: 100%;"> </a>
  <figcaption class="image-caption">Different preferences that need to be configured, including the Power Presets. Click to enlarge.</figcaption>
</div>

1. Install [Java](https://www.java.com/en/download/help/download_options.html) on your device. <br>
1. Install [JOSM](https://josm.openstreetmap.de/) on your device (if needed, further instructions on how to install and use JOSM on your device can be found at [learnOSM](https://learnosm.org/en/josm/start-josm/)).
1. Link your OSM account to JOSM. Go to `Preferences → OSM Server` and select "Authorise". Login with your OSM account. Be aware that your token is now stored in your local preferences.xml file. Do not share this file with anyone. <br>
1. Enable `Remote control` in `Preferences → Remote Control`. This allows for grid data to be loaded automatically.
1. Enable `Expert Mode` `View → Expert Mode` to enable search function that you will need. 
1. Understanding JOSM layers. JOSM works with stacked layers, similar to Photoshop or GIS tools:
    * You’ll typically have an OSM data layer, imagery layers, and optionally GeoJSON or task layers.
    * You can switch between multiple satellite imagery sources (for instance, Esri, Mapbox) to use the clearest one for your area.
1. Create an OSM [account](https://www.openstreetmap.org/user/new) if you don't have one. Once you do, go to `Preferences → OSM Server` and press authorise now. Login with your OSM account, and authorise. Your account is now linked to JOSM on your device.
1. Load your Satellite Imagery via `Imagery` and select `Bing aerial imagery` and `Esri World Imagery`. In the `Layers` window on the right hand side you can now `Show/hide` the different imagery. This is also where you will load additional data layers. Changing the order of the data and imagery allows you to combine and overlap the different data sources.

!!! note
    The JOSM Preferences window is accessed through the `Edit → Preferences` menu on Windows and Linux, and `JOSM → Settings` on Mac.

### **<div class="tools-header">2. Setup your Presets </div>**

<div style="float: right; margin: 10px 0 20px 20px; width: 350px;">
  <img src="../images/josm-toolbar.png" class="img-border" style="width: 100%;"> 
  <figcaption class="image-caption">Default MapYourGrid Presets in JOSM toolbar. Click to enlarge.</figcaption>
</div>

1. For ease of mapping, customise your top toolbar with presets if you have not used the default preferences. Right click the toolbar and choose `Configure toolbar`, then select `Presets → Man Made → Man Made/Power` and add `Power Towers`, `Power Portal`, `Power Substation`, `Power Plants`, `Power Line` and `Power Generators`. This are the main objects to will need for transmission grid mapping. 
2. Another important Preset your will need is `Add Node`. You will find it under `Tools` → `Add Node`. 

    
### **<div class="tools-header">3. Add visual clarity with custom map styles :art:</div>**

<div style="float: right; margin: 5px 0 10px 20px; width: 350px;">
  <a href="https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/legend/power-grid-legend.png" target="_blank">
  <img src="https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/legend/power-grid-legend.png" class="img-border" style="width: 100%;"> </a>
  <figcaption class="image-caption">OhmyGrid legend for transmission grid mapping. Click to enlarge.</figcaption>
</div>
 
1. In JOSM, go to `Preferences → Map Paint Styles` and press the "+" in the top right.
2. Paste this [URL](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/ohmygrid-default.mapcss), or download the raw [file](https://github.com/open-energy-transition/color-my-grid/blob/main/ohmygrid-default.mapcss) on your device, and add it.
3. Make sure the style is active in the Map Paint Styles menu. 

**Optional steps for an even better visual experience :**

* Not all grids are made the same. Use this MapCSS file for [low-density grids](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/ohmygrid-default.mapcss), or this one for [high-density grids](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/ohmygrid-default.mapcss). 
* Check [ColorMyGrid](https://github.com/open-energy-transition/color_my_map), our MapCSS Generator tool, to easily adapt the MapCSS file to your needs. The raw data to edit the [map legend](https://raw.githubusercontent.com/open-energy-transition/color-my-grid/refs/heads/main/legend/power-grid-legend.png) is in the ColorMyGrid repo. 


### **<div class="tools-header">4. Let's map! Choose a Good First Line </div>**

Our community is constantly investigating transmission lines that are suitable for beginner friendly mapping experiences. Simply select a 'Good First Lines' from the following spreadsheet, and tick it if you have started mapping it:

??? success "Good First Lines (Click Me)"
    <iframe
     src="https://docs.google.com/spreadsheets/d/13YZftK9xZ09t2oSvhwjE0Zb7P25nl9OaUAxIBVNH0js/edit?usp=sharing&rm=minimal"
     class="iframestyle"
     style="width:100%; height: 500px; border:1px solid #ddd; ">
    </iframe>

### **<div class="tools-header">5. Load Power Infrastructure into JOSM :inbox_tray:</div>**

<div style="float: right; margin: 5px 0 10px 20px; width: 350px;">
  <img src="../images/starter-kit/kenya-look-into-data.jpg" class="img-border" style="width: 100%;"> </a>
  <figcaption class="image-caption">A substation of a hydroelectric power plant in Nigeria and the connection to the transmission grid.</figcaption>
</div>


1. Make sure remote control is enabled and ad-blocker disabled, and then go to the start mapping [page](https://MapYourGrid.org/map-it/). 
1. Here you can click on the country you want to map, and it will directly open JOSM and load the data of that country. The "Default Transmission (90kV+)" data should already be selected when you open the page. Now press the country, state or province of the `Good First Line` you would like to map. To load data for provinces or states, simply zoom in further until the border becomes visible. 
1. The data should now automaticlly appear in JOSM. In the `Layer` window on the right handside you should see the `Data Layer`. The ✅ on the left of the Data Layer should be visible, indicating that this is the active layer. All your edits in the main windows will now be part of this `Data Layer` 
1. Familiarize yourself with the grid data, click on the lines and substation to inspect the tags and memberships in the window in the right side. 



### **<div class="tools-header">6. Map your First Line</div>**

<div style="float: right; margin: 5px 0 20px 20px; width: 350px;">
  <img src="../images/starter-kit/josm_env.jpg" class="img-border" style="width: 100%;">
  <figcaption class="image-caption">Key JOSM elements for continuing a transmission line. Click to enlarge.</figcaption>
  <img src="../images/mapfast.png"  class="img-border" style="width: 100%;"> 
  <figcaption class="image-caption">Selecting all the finished notes in a line enables you to quickly turn them into Power Towers.</figcaption>
  <img src="../images/starter-kit/validation.jpg" class="img-border" style="width: 100%;">
  <figcaption class="image-caption">Before uploading, JOSM will test your edits for known issues and various rule sets. Try to resolve as many validation results as possible. Click to enlarge.</figcaption>
</div>

 Mapping is an iterative process, so you will make mistakes. However, this should not stop you from mapping; simply map what you can see in the imagery. Those who are new to the field should avoid altering existing data at all costs. However, you cannot break anything by adding new data, as this is constantly validated by our quality assurance tools. Now Start Mapping:

1. Zoom in on the satellite imagery until you can see the houses and roads.
1. Copy the Coordiantes of your `Good First Line` and press the `Add Node` <img src="../images/starter-kit/add-node.png" class="icon-svg off-glb" style="width: 30px; height: auto;"> presets button. Enter the coordiantes here and press Ok. You should now see power towers that are not mapped at the end of a transmission line.
1. Now, press `Draw Line` <img src="../images/starter-kit/draw-nodes.png" class="icon-svg off-glb" style="width: 30px; height: auto;"> the last tower symbol at the end of the line. You should now be able to extend the line. 
1. Search for the next power towers you can find and click on its footprint. 
1. If you ever feel unsure about how the line runs just place towers without the lines. By adding power towers you can do nothing wrong. Adding power towers is the easiest way to get started.
1. Continue the line to the best of your ability press CTRL+F while the line is still selected. Select all nodes you have created by Entering `child selected type:node AND untagged` as search string. Now Press `Search` to select all nodes without a tag. 
1. Now press the `Power Tower` <img src="../images/starter-kit/power-towers.png" class="icon-svg off-glb" style="width: 30px; height: auto;"> preset followed by `Apply Preset`.


### **<div class="tools-header">7. Upload your work :outbox_tray: </div>**

1. With having the `Data Layer` activated, press the Green Upload arrow pointing upwards <img src="../images/starter-kit/upload.png" class="icon-svg off-glb" style="width: 30px; height: auto;">. 
1. A new window will apear in the right panel showing all the issues identified. Right-clicking on an issue will allow you to zoom in on it. Avoid ignoring this validation results. The only acceptable warning when uploading data is `Possible missing line support node within power line`. 
1. You just mapped your First Good Line. Feel free to close more First Good Lines, but make sure you leave some for the others. You can use the [Tools and Strategies](tools.md) we have provided to find your own unmapped line. To support our initiative, please use the #MapYourGrid hashtag in the comments you make in the changeset.



## **<div class="tools-header"> Avoid these common mistakes :name_badge:</div>**

<div style="float: right; margin: 5px 0 10px 20px; width: 350px;">
  <img src="../images/starter-kit/power-towers-without-lines.jpg" class="img-border" style="width: 100%;"> </a>
  <figcaption class="image-caption">In particular, in the dense urban areas that are widespread in Nigeria, it can be very difficult to determine the route of the lines in satellite images. Therefore, mappers simply place unconnected power towers that appear as blue squares at higher zoom levels.</figcaption>
</div>

Mapping is an iterative process and mistakes happen. This should not stop you from mapping; simply map what you can verify based on your skillset. If a tower, lines or attributes are missing, our quality assurance tool Osmose will automatically detect this.

1. Our tools focus on transmission grids, that’s why you don’t see lines below 90 kV. To see already mapped lines below 90 kV or lines tagged with power=minor_line, download the whole area you’re working on with the green arrow pointing down.
2. When mapping, make sure to not go across the border of the country you’re working on (visible dashed orange lines). Otherwise, you may find yourself mapping something that already exists, but hasn’t been downloaded in JOSM.
3. Don’t map beyond your expertise. If unsure, leave it for experienced mappers or locals, make a fixme tag, or ask the community! If you ever feel unsure about where to place the lines, just focus on adding power towers. You can't go wrong this way. Adding power towers is the easiest way to get started.

For a safe mapping, we recommend you reading about [good practices](https://wiki.openstreetmap.org/wiki/Good_practice).

!!! note
    **⚠️ In some countries, mapping power lines is restricted. Always verify local guidelines, connect with the OSM local community first, or check out the [local projects](https://wiki.openstreetmap.org/wiki/Power_networks#Local_projects).**
    
    **⚠️ By following our [Code of Mappers](./code-of-mappers.md), we collectively protect the integrity of the OSM platform, foster trust with communities, and unlock the power of open data for a more resilient and just energy future.** 

## **<div class="tools-header">What else? Learn the grid basics </div>**
You don’t need to be a grid expert to start mapping, but a little knowledge helps!
The following documents and materials will give you a basic understanding of how to map an electrical grid.

The [Learning Curve](https://www.youtube.com/@TheLearningCurveBenila/videos), is a YouTube channel that will help you understand the fundamental knowledge of the electrical grid. Here some video we recommend for grid mappers. 

1. [Electrical Line Supports - Transmission Towers & Poles](https://www.youtube.com/watch?v=AB1qYsiDm0M)
1. [Components of Overhead Transmission Lines](https://www.youtube.com/watch?v=A6fwq3yHRXQ)
1. [Comparison between HVAC and HVDC transmission system](https://www.youtube.com/watch?v=l9nHs8e0WUg)

The following image is take from the report Key technology components of electricity grids Source: IEA - [Electricity Grids and Secure Energy Transitions](https://iea.blob.core.windows.net/assets/ea2ff609-8180-4312-8de9-494bcf21696d/ElectricityGridsandSecureEnergyTransitions.pdf).

<div style="float: left; margin: 5px 0 20px 20px; width: 100%;">
  <a href="../images/grid-design.png" target="_blank">
  <img src="../images/grid-design.png" class="img-border" style="width: 100%;"> </a>
  <figcaption class="image-caption">Key technology components of electricity grids Source: IEA - Electricity Grids and Secure Energy Transitions.</figcaption>
</div>


## <div class="tools-header">Still "On the Line" and Motivated to Continue?</div>

Well done on making it this far! We are offering free, hands-on transmission grid mapping workshops to people who have tried the Starter-Kit. You are very welcome to join our [community chat](https://discord.gg/a5znpdFWfD) called _📍-mapyourgrid_ on the PyPSA-Earth discord channel. Here you can ask questions, and interact with the community. For mapping specific questions and to participate in our free personalized training, please join our [📍-mapyourgrid-support-and-training](https://discord.gg/fBw7ARTUeR) channel. 

Check out our [Tools and Strategies](tools.md) to learn how to find your own new lines and become a grid mapping expert! You are also welcome to join our community calls and tutorials to learn more about the mapping process and the initiative. The OpenStreetMap Wiki pages [The Power Network](https://wiki.openstreetmap.org/wiki/Power_networks) and [Key:Power](https://wiki.openstreetmap.org/wiki/Key:power) provide an overview of how to map different power infrastructure.

<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=Europe%2FBerlin&showPrint=0&title=Community%20live%20sessions&src=Y182ODE3NjE1MGIzMjY4MGRkZmUzMGM1ZTE1MDU0YTc5MTVhMzY2NmY1OGY5NjkxOGVjOTZhNDJjZWQwODQ2ZGVmQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&color=%23AD1457" style="border:solid 1px #777" width="800" height="600" frameborder="0" scrolling="no"></iframe>


## <div class="stradegy-header">iD and MapComplete Starter Kit</div></h3>

Before mapping power infrastructure, get familiar with OpenStreetMap (OSM):

1. Create an OSM account. [Sign up here](https://www.openstreetmap.org/user/new). 
2. Learn basic mapping with the in-browser editor (iD) :
    - Use the [iD Beginners' Guide](https://learnosm.org/en/beginner/id-editor/) to get starter. 
    - Start small. Add missing streets, parks, buildings in your area. 
3. Find missing power infrastructure near you. 
    - Go to [Open Infrastructure Map](https://openinframap.org/).
    - Click "Find my location" on the top right corner, or search your city. 
    - See a missing line or substation nearby ? Map it ! Use the iD editor. 
    - Check detailed mapping guidelines in the OSM Wiki. 
    
Even small edits like missing towers or bits of power lines make a big difference by helping others complete the grid. Don't worry about making mistakes. Mapping is an iterative process, and the OpenStreetMap community can detect anything that is missing or wrongly tagged.