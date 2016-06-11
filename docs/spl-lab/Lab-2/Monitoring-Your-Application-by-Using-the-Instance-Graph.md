---
layout: docs
title:  Monitoring your application by using the instance graph
description:
weight: 320
---

# Monitoring your application by using the instance graph
---
To the right of the Instance Graph, a layout options drop-down menu and two selection panes for Layers and Color Schemes allow you to control the display. Explore the various options; here are some explanations and suggestions that will help interpret what you see.

The layout options control how the operators in the graph are grouped:

* By Composite: This is the default. You see two boxes representing the two main composites—that is, the two applications, and inside each composite the operators that make up the application; three for the old job and five for the new one.

* By Category: You can assign categories to your operators to group them any way you want; this is useful when you have a large number of operators. You did not use this facility in this lab, so this option shows all the operators without grouping—though you can still identify the two distinct flows, of course.

* By PE: A PE is a Processing Element—essentially an operating system process. Operators can be combined (fused) into a single PE; this couples them tightly and reduces communication latencies. That is a performance optimization beyond the scope of this lab; you’ve simply used the default of giving each operator its own process. This layout option shows each operator inside a box representing its PE, which in this case does not add much information.

* By Resource: Since the virtual machine is only a single resource (host), all operators are shown within the same box representing the resource.


The Instance Graph in Studio provides many ways to monitor what your application does and how data flows through a running job. This part of the lab is a matter of exploring those capabilities; the steps here are just hints.

1. Launch the application: In the Project Explorer, right-click on the main composite (MyMainComposite) and choose Launch…. In the Edit Configuration dialog, click Continue (if you switched workspaces, you may have to click Apply first).

1. Maximize the Instance Graph view. You now have two running jobs: the one you just launched and the one from the previous exercise. The old one is dormant (it is not getting any data), but leave it running for now.

    <img width="85%" src="/tutorials/images/Lab2/1.JPG"/>


1. For the rest of this exercise, keep the layout set to Composite.

    In the Layers box, only the Alert layer is relevant; it should be checked. The other, Consistent Region, is beyond the current scope (it has to do with guaranteed tuple delivery); checked or unchecked, it will have no bearing on this lab.

    Move on to the Color Schemes. Note that they are mutually exclusive (you can only check one at a time), and you cannot interact with the checkboxes on the individual colors under each scheme. It is possible, however, to add new color schemes, and to edit existing ones. The color schemes assign colors to the operators based on their properties (the PE or job they belong to, the resource they run on, etc.) or on metrics—counters maintained by the Streams runtime to monitor diagnostic statistics, which are refreshed periodically and present a real-time view of the instance. This is extremely helpful in identifying problems quickly, especially in a large, complex graph.

1. The default color scheme is Health. Expand the twisty for Health in the Color Schemes pane: green indicates that the operators (actually, their PEs) are healthy, meaning that there are no errors and they are up and running and ready to process data. You may have noticed when launching an application that the operators are red and yellow before they turn green; this reflects the initialization process, during which a PE may be waiting for another to finish loading before a stream connection can be made, for example.

1. Check the Flow Under 100 [nTuples/s] color scheme. All operators (most likely) turn black, indicating that no tuples are flowing. This is because it has been more than 45 seconds or so since you launched the application; despite the throttling it finished reading the entire file.

    You will need to supply more data. This is easy enough to do by making the same file appear multiple times in the source directory. You can manually do this by making copies of the file in the same directory, using the File Browser or using the command line in a Terminal window.

    A better trick is to update the file’s time stamp at regular intervals: each time the DirectoryScan operator sees the file with a new time stamp, it treats it as a whole new file and passes the file path into the FileSource operator. The lab installation provides a desktop launcher that does this at 45-second intervals (about the time it takes the Streams job to read the file), and keeps doing it until you cancel it. This has the effect of simulating an infinite data feed, even though it’s really the same file over and over. You can let this run for the duration of the lab; it does not copy any data and will not fill up the disk.

1. On the desktop, double-click the Infinite Source launcher.     (Move or minimize the Studio window to see it.)

    A Terminal window pops up; leave it up as long as you want data to flow. (It’s OK to minimize it.) To cancel, close the window or type Ctrl+C when the window has the keyboard focus.

1. Maximize the Studio window again and look at the Instance Graph view.

    After a slight delay (the DirectoryScan operator scans every five seconds), the colors change in the new job; the old job stays black, as it is not designed to read more than one file. The colors are mostly yellow (31-40) for Throttled and Filtered, and brown (1-5) for Writer. It makes sense for the rate after the Filter operator to be lower, as only a subset of tuples makes it through.
  
    <img width="75%" src="/tutorials/images/Lab2/2.JPG"/>

1. Check the nFinalPunctsSubmitted color scheme. A Final Punctuation marker is a special message (not a tuple), generated by any operator to indicate that a stream will no longer carry new tuples. This marker travels downstream through the graph; any operator that has received one on every one of its input ports (every operator you’ve used so far has only one input port) is from then on dormant and ready to shut down, and in turn submits a Final Punctuation. Operators without output ports, like the FileSink, do not support this metric, so they are not colored by this scheme.

    Notice that the operators in the old job are now black, indicating that they have submitted a Final Punctuation; this happened when the FileSource reached the end of the input file. The operators in the current job are green (no Final Punctuation) because they have not reached the end of the input data, and never will: there is no way to know when another file will appear in the source directory.

1. Now you might as well get rid of the old job; you don’t want it cluttering up your Instance Graph any further. There are at least three options.

    * If you just want to remove some clutter, simply collapse the main composite by clicking the   minimize button in the title bar of the composite.

    * If you want it to disappear from view altogether but are not ready to cancel the job, just filter it out of the graph display: click the   Filter graph… button in the Instance Graph view’s toolbar; in the Instance Graph Filter dialog, check only the most recent job under Job ID Filter, and click OK.

    * To cancel the job completely, right-click anywhere in the main composite and choose Cancel job; in the Confirm dialog, click Yes.

 {% include nextPageFinder.html context=page.url %}
 
