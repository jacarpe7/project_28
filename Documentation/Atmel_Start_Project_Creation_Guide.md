<h1>Atmel Project Creation Steps </h1>

<h3>10/17/2020</h3>

Resources:

- [Atmel Start Page](https://start.atmel.com/)
- [Atmel Start Official Documentation](https://onlinedocs.microchip.com/pr/GUID-4E095027-601A-4343-844F-2034603B4C9C-en-US-4/index.html?GUID-A7503856-D18B-41FE-B5A2-E705E7587C30)
- [QTouch Library Documentation](https://microchipdeveloper.com/touch:generate-qtouch-configurator-touch-project)

**Step 1**. Create a new project:

![](https://i.imgur.com/foMq01V.png)


**Step 2**. Search and select your hardware (in our case it&#39;s the AVR128DA48):

![](https://i.imgur.com/zyGLm26.png)


**Step 3**. Add software components (QTouch library is built for hardware like the QT7):

![](https://i.imgur.com/MG8vMMi.png)


**Step 3** (continued):

![](https://i.imgur.com/O5zMUT9.png)


**Step 4.** Configure Pin assignments (see [official documentation](https://onlinedocs.microchip.com/pr/GUID-4E095027-601A-4343-844F-2034603B4C9C-en-US-4/index.html?GUID-CB09F642-6E2A-4E5C-87CE-6BD25D062331)): 

![](https://i.imgur.com/IkWhUUG.png)

**Step 5.** Configure Clock settings (see [official documentation](https://onlinedocs.microchip.com/pr/GUID-4E095027-601A-4343-844F-2034603B4C9C-en-US-4/index.html?GUID-F7559459-9D60-4F36-8135-0BAF685B3933)): 

![](https://i.imgur.com/cKzibUj.png)

**Step 6.** QTouch configuration (see [official documentation](https://microchipdeveloper.com/touch:generate-qtouch-configurator-touch-project)): 

![](https://i.imgur.com/weR8soL.png)

_Note: The technology selector reflects the axis of data. Mutualcap -\&gt; X &amp; Y axis, Selfcap -\&gt; Y axis. The Channels is the number of sensors to gather data from (our QT7 has 3 in the slider)._

Supported Features for QT Library Configuration: 

![](https://i.imgur.com/mQbqJSS.png)

**Step 7.** Review generated code:

![](https://i.imgur.com/3ZavAh7.png)

**Step 8.** Export to Atmel Studio: 

![](https://i.imgur.com/d1m072C.png)

**Step 9.**  For further information:

[Atmel Studio User Guide](Atmel_Studio_User_Guide.md)
