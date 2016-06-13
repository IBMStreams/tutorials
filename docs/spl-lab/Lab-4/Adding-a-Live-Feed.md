---
layout: docs
title:  Adding a live feed
description:
weight: 710
---
# Adding a live feed
---

## Prerequisites

<div class="alert alert-warning" role="alert">
<h4><b>Note</b></h4>
This section assumes that you have internet connectivity. If your lab environment is not connected, you can still go through the steps of importing and launching the application and seeing the connections being made, but no live data will flow. In most cases, there will be no other symptoms.<br><br>

In instructor-led events in venues where participants’ machines have no connectivity, the instructor may go through this section as a demonstration rather than an exercise for everyone to complete.
</div>

## About this task
Rather than building a live-data ingest application from scratch, you will import a Streams project that has already been prepared. This application uses an operator called HTTPGetXMLContent, from a version of the com.ibm.streamsx.inet Toolkit that can currently only be found on GitHub, to connect to a web services feed from NextBus.com and periodically (every 30 seconds) download the current locations, speeds, and headings of San Francisco Muni’s buses and trams. It parses, filters, and transforms the data and makes the result look similar to the file data—though some differences remain. It exports the resulting stream with a set of properties that match the subscription of your processing app; when you launch the NextBus app, the connection is automatically made and data flows continuously until you cancel the job.

1. Before you can use the NextBus project, you must tell Studio where to find the version of the com.ibm.streamsx.inet toolkit that it depends on.

    a. In the Streams Explorer, expand InfoSphere Streams Installations [4.1.0.0] > InfoSphere Streams 4.1.0.0 > Toolkit Locations.

    b. Right-click Toolkit Locations and choose Add Toolkit Location….

    c. In the Add toolkit location dialog, click Directory… and browse to My Home > Toolkits. (My Home is all the way at the top; the dialog comes up in the completely separate Root tree.) Select Toolkits and click OK.

    d. Click OK again.

    If you expand the new location, (Local) /home/streamsadmin/Toolkits, you see com.ibm.streamsx.inet[2.5.0]. This is different from the version of this toolkit that is installed with Streams (2.0.1), so the NextBus project can select the right one by version. (You’ll find the 2.0.1 version under the location STREAMS_SPLPATH.)

1. Import the NextBus project.

    a. In the top Eclipse menu, choose File > Import….

    b. In the Import dialog, select InfoSphere Streams Studio > SPL Project; click Next >.

    c. Click Browse…; in the file browser, expand My Home and select Toolkits. Click OK.

    d. Select NextBus and click Finish.

1. Expand project NextBus and namespace com.ibm.streamslab.transportation.nextbus. Launch application NextBusIngest (you may have to wait till the project build finishes).

1. Maximize and organize the Instance Graph. If you want, you can expand the nested composites in the NextBusIngest job.

## Check your results
You should see the three applications all connected; tuples flow from the FileIngest job whenever you copy another file into the Data directory. Tuples flow from the NextBus job in 30-second bursts. The error.observations file gradually fills with records from NextBus: their vehicle IDs do not conform to the “Cnnn” format. (Refresh the file periodically: click in the editor showing the file and click Yes in the File Changed dialog, which comes up when Studio detects that the underlying contents have changed.)

 {% include nextPageFinder.html context=page.url %}
 
