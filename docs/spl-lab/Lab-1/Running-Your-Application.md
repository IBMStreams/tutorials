---
layout: docs
title:  Running your application
description:
weight: 250
---

# Running your application
---
You are now ready to run this program or, in Streams Studio parlance, launch the build.

1. In the Project Explorer, right-click MyMainComposite (expand MyProject and my.name.space if necessary); choose Launch….

    In the Edit Configuration dialog, click Apply, and then Continue.

    The Streams Launch progress dialog appears briefly. To see what happened, switch consoles, from the SPL Build to the Streams Studio Console.

2. In the Console view, click the Display Selected Console button (way over to the right) to switch consoles.

    The Streams Studio Console shows that job number 0 was submitted to the instance called StreamsInstance in the domain StreamsDomain.
    
    <div class="alert alert-info" role="alert">
    <h4><b>Launch configuration</b></h4>
    There are many options that can be set or changed at the time you launch an application; for now, ignore all that.
    </div>

    Since nothing else seems to have happened, you need to look for some effect of what you’ve done. First, you’ll view the job running in the instance; then you’ll inspect the results.

3. Switch to the Streams Explorer (the second tab in the view on the left, behind the Project Explorer). Expand the Streams Domains folder, the one domain named StreamsDomain, and the Resources and Instances folders under that:

    The Resources folder refers to the machines available to the domain; of course, in this virtual machine there is only one. Resource tags let you dedicate different hosts to different purposes, such as running runtime services or application processes. In this single-resource environment, this is not relevant.
    
    <div class="alert alert-info" role="alert">
    <h4><b>Streams jobs and instances</b></h4>
    The Streams Jobs and Streams Instances folders simply repeat, for convenience, information from the Instances folders under the listed domains, but they lack further drill-down information.
    </div>

    You know you have one instance, StreamsInstance, in the domain StreamsDomain; the entry tells you that it is the default instance (where launched applications will run unless otherwise specified), that it is Running, and its current wall clock time. (You may have to widen the view to see the status.)

4. Expand default:StreamsInstance@StreamsDomain. This shows a number of elements, but the only one you’re interested in for now is the last one: 0:my.name.space::MyMainComposite_0 is the job you have just submitted (a running application is called a job), and its status is Healthy. There is much information here about a job and its constituent operators and Processing Elements (PEs), but you are going to explore it graphically instead.

    <div class="alert alert-warning" role="alert">
    <h4><b>What if my job is not healthy?</b></h4>
    If you are in an instructor-led lab, ask the instructor to help you. Otherwise, you have to diagnose the problem yourself. The most likely culprit is a mistake in the FileSource’s file parameter, which would not be caught by the compiler but would cause a file-not-found exception at runtime. More elaborate debugging, involving trace files and other diagnostics, is beyond the scope of this lab.
    </div>

5. Right-click on default:StreamsInstance@StreamsDomain; choose Show Instance Graph.

    A new view opens up in the bottom panel, showing a graph similar to that in the graphical editor; but this one shows, live, what is actually running in the instance. If you launch multiple applications (or multiple copies of the same application) you will see them all. And it lets us inspect how data is flowing, whether there are any runtime problems, etc.

    If necessary, expand or maximize the Instance Graph view; click   Fit to Content in the view’s toolbar.

    <b>Figure 3. Finished and running application. All PEs are healthy, so the job is, too.</b>

    <img width="45%" src="/tutorials/images/Lab1/4.JPG"/>


    There is a lot more to the Instance Graph; you will explore it further in the next part.

6. Hover over Filtered; you get current information about data flows and other metrics. Among other things, it will tell you that the input received 1902 tuples, and the output sent 95 tuples. This seems reasonable, given that the output should be only a subset of the input. But it also says that the current tuple rate on both input and output is 0/sec, so no data is currently flowing. Why? Because it has read all the data in the all.cars file, and there will never be any more data.

<b>Streams jobs run forever</b>

The input data is exhausted but the job is still running. This is always true for a Streams application running in an instance (distributed applications): a job can only be canceled by manual (or scripted) intervention. In principle, a stream is infinite, even though in some cases (like when reading a file) this may not be quite true.

1. To inspect the results, you must look at the input and output data.

    a. In the top menu, choose File > Open File...
    
    b. In the Open File dialog, browse to streamsadmin/data/all.cars and click OK.

    Studio opens the file in an editor view; it shows location observations for multiple vehicle IDs: C127, C128, etc.

2. In the Project Explorer (the first tab in the view on the left), expand Resources; there should be a file under data, but there is no twisty in front of the directory. To update the view, right-click data and choose Refresh. The twisty appears; expand it, and double-click on filtered.cars. This file contains coordinates, speeds, and headings only for vehicles C101 and C133.

<b>Show files side by side</b>

You can show two editors side by side by dragging the tab of one of them to the right edge of the editor view. As you drag, green outlines appear, which arrange themselves side by side as you approach the right edge. To undo, drag the tab back to a position among the other tabs, or close it.

 {% include nextPageFinder.html context=page.url %}
 
