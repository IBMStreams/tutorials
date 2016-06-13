---
layout: docs
title:  Monitoring your application
description:
weight: 300
---

# Lab 2 - Monitoring your application
---

In this part, you will further develop the vehicle data filtering application and get a more detailed understanding of the data flow and the facilities in Studio for monitoring and examining the running application. To make this easier, you will make two enhancements that let you see what is happening before the data runs out: you will slow the flow down (left to its own devices, Streams is just too fast) and you’ll make it possible to read multiple files. This is a general design pattern for development and debugging.


## Prerequisites
<div class="alert alert-warning" role="alert">
<h4><b>Note</b></h4>
If you are confident that your results from the previous part are correct, you can continue working with them and skip this section.
</div>

To continue with this part even if you did not successfully complete the previous part, import a Streams project that has been prepared for you, containing the expected results of Lab 1.

1. In the Project Explorer, right-click on the current project (MyProject) and choose Close Project. This gets it out of the way for builds or name conflicts, without deleting any files.

1. In the top Eclipse menu, choose File > Import….

1. In the Import dialog, select InfoSphere Streams Studio > SPL Project; click Next >.

1. Click Browse…; in the file browser, expand My Home and select Labs. Click OK.

1. Select (check the box) MyProject1 and click Finish.

    This kicks off a build, but there is no need to wait until it finishes.

1. In the Project Explorer, expand MyProject1 and then my.name.space.

1. Double-click MyMainComposite to open it in the graphical editor.

# Adding operators to enhance monitoring

Two new operators are needed to make your application easier to monitor and debug. The Throttle operator copies tuples from input to output at a specified rate rather than as fast as possible. The DirectoryScan operator periodically scans a given directory; for each new file that satisfies optional criteria, it sends out a tuple that contains the file’s full path.

Instead of using the palette’s filter field to quickly pick up the operators you want, let’s browse the full palette to achieve the same result.

1. In the graphical editor’s palette, expand spl (under Toolkits), and then spl.adapter. Drag DirectoryScan into the main composite. The editor names the operator DirectoryScan_4.

1. Scroll down in the palette and expand spl.utility; scroll down further and find Throttle. Drag and drop it onto the stream Observations, exactly as you did with the LocationType schema previously. (Make sure the stream is highlighted by green handles before you let go.)

    The operator will be called Throttle_5. The editor automatically connects the Observations stream to its input port and creates a new stream, with the same schema as Observations, from its output port to the input of Filtered. There is no need to adjust the schema of this new stream: The Throttle operator merely controls the rate at which tuples flow, without changing their contents.

    To straighten out the graph, click   Layout and   Fit to Content.

1. Rename the new stream to Throttled. Rename the operator (to Throttled) by blanking out its alias. (That’s in the General tab of the Properties view; review Part 1 if you forgot how to get there.)

1. Drag a stream from the output of DirectoryScan_4 to the input of Observations.

Your streams view should look like this at this point:

<img width="85%" src="/tutorials/images/Lab2/3.JPG"/>

<div class="alert alert-info" role="alert">
<h4><b>Optional input ports</b></h4>
  The FileSource operator can have an input port, but it is optional. In the original graph you did not use it, so there is no yellow box on the left. But while dragging a stream from another operator’s output port, the optional input port is indicated by a lightly outlined, unfilled box, and you can connect the stream to it like any other port.
  </div>

  Click   Layout and   Fit to Content.

  To finish up, you need to define the schema for the stream from the DirectoryScan, and tell that operator where to look for files; adjust the configuration of Observations (since it now gets its instructions from an input stream rather than a static parameter); and tell the Throttle the flow rate you want.

1. The DirectoryScan operator’s output port supports only one schema: a single attribute of type rstring, which will hold the full path to the file; you can call that attribute anything you like.

    * Select the output stream from DirectoryScan_4, and rename it to Files.

    * In the Schema tab in the Properties view, click on the first Name field (placeholder varName) and type file; press Tab to move to the next field (placeholder varType).
    * Enter rstring. Remember to use content assist (Ctrl+Space) to reduce typing and avoid errors. Press Enter.<br><br>
    
1. In the editor, select the DirectoryScan_4 operator. In the Properties view, go to the Param tab and set the directory parameter to the value "/home/streamsadmin/data". (Remember to include the double quotes.)

1. Rename the operator (to Files) by blanking out its alias.

    A FileSource operator knows which file(s) to read either from a static parameter (called file) or from the tuples coming in on an input stream—but not both. Now that you are getting filenames from a DirectoryScan operator, that file parameter you used previously is no longer needed; in fact, it’s an error to keep it.

1. Select the Observations operator in the editor. In the Properties view (Param tab), click on the file parameter and then click Remove.

1. The Throttle operator has a mandatory parameter for specifying the desired flow rate; it is a floating-point number with a unit of tuples per second.

  In the editor, select Throttled. In the Properties view (Param tab), click on the Value field next to the rate parameter and enter 40.0. (The decimal point is necessary to indicate a floating-point value).

  Save. There should be no build errors.

 {% include nextPageFinder.html context=page.url %}
 
