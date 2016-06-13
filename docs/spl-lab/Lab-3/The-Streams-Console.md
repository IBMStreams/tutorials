---
layout: docs
title:  The Streams Console
description:
weight: 510
---

# Monitoring with the Console
---

In this module, you will learn about the Streams Console, a general-purpose and web-based administration tool for IBM Streams. Features and uses for the Console covered here include:

* What is part of the Console, such as the application dashboard
* How you can identify problems as they occur
* How to monitoring your jobs
* How to visualizing the flow of data

## The Streams console

The Streams Console is a general-purpose, web-based administration tool. Each Streams domain has its own console environment; the console interacts with one specific domain at a time, based on its Streams Web Service (SWS) URL. In addition to managing and monitoring instances, resources, jobs, logging and tracing, and many other administrative things, it serves as a simple data visualization tool. It is not intended to be a production-quality dashboard such as Cognos, but mainly a useful facility for monitoring applications and understanding data during development.

There are several ways to launch the Console: with a desktop launcher, or by looking up the URL and opening it directly in Firefox or any other browser—from any machine with https access to the Streams environment. Normal user authentication and security apply. You’ll open it from within Studio.

To open the Streams Console:

1. 	In the **Streams Explorer**, expand **Streams Domains**. Right-click on **StreamsDomain** (the only domain listed) and choose **Open Streams Console**.
1. 	In the **Untrusted Connection** page, expand **I Understand the Risks** and click **Add Exception…**.
1. 	In the **Add Security Exception** dialog, keep **Permanently store this exception** checked and click **Confirm Security Exception**.
1. 	Log in as user `streamsadmin` with the password `passw0rd`.


    The initial view is the **Management Dashboard**, which monitors the domain from an administrator’s point of view. Each of the views, called cards, shows a specific type of object (PEs, jobs, instances, and so on), with a graphical view that lets you see at a glance what is going on. At the top is a navigation bar with buttons that show a count of objects and their state (healthy/unhealthy or stopped/starting/running) and let you get quickly to a monitoring view for that object.

    The image shows a snapshot highlighting some of the graphically depicted information. For example, the **PES** card shows quickly which processing elements consume little memory and CPU (in the bottom left) and which consume a lot (top and right). This lets a developer identify quickly which operators to focus on during performance optimization, or pinpoint a memory leak.

    <img width="100%" src="/tutorials/images/Lab3/2.JPG"/>

    <div class="alert alert-info" role="alert">
    <h4><b>Remember PEs?</b></h4>
    A PE or processing element is essentially a runtime process, encapsulating one or more operators. Where the operator is the logical unit of operation, the PE is the unit of execution at runtime.
    </div>

    With only a single job running in a single instance on a single resource, many of the graphics are not very interesting, but they are useful when managing a real cluster with many running jobs. Hovering over the graphic in each card pops up a panel with detailed information and links for drilling down further. Also while hovering, controls appear in the top right of the card:

    **Card Settings** (color schemes, filters, and other settings appropriate for the information shown), **Refresh**, **Card Flip Action** (to show the tabular data behind a graphic), **Stack** (minimize the card), and **Max** (maximize the card). Not all cards have all controls.

1. 	Explore the dashboard: resize, rearrange, and maximize cards; flip a card (for example, **PE Details**) to see the information in tabular form. Hover over one of the categories in the navigation bar and in the popup click on Monitor <nobr>[Instance | Job | …] </nobr> to see a different set of cards.

    <div class="alert alert-info" role="alert">
    <h4><b>Browser acting slow?</b></h4>
    The Console uses fancy graphics, which likely makes the browser the heaviest CPU consumer in your VMware environment (the “guest”), crowding out the Streams runtime and application. If the Console responds slowly or occasionally freezes up, try using a browser in the native environment of your computer (the “host”). Depending on your configuration, this may let the browser run on different CPU cores, freeing up the cores used by the guest for Streams itself.<br><br>
    Copy the URL: https://streamsqse.localdomain:8443/streams/domain/console from the address bar of the guest browser. Paste it into the address bar of the host browser, and replace the hostname streamsqse.localdomain with the IP address, which you get from the hover popup of the Resources card in the image further up on this page. Close the guest browser when you connect successfully.
    </div>

## The application dashboard

Let’s look more closely at your running application. As a developer, you can even set up your own dashboard by saving a set of cards in your preferred arrangement, with a query to focus on just the jobs that are of interest to you.

- In the title bar, choose **Management Dashboard** > **Open Dashboard** > **Application Dashboard**.

Some of the cards are equivalent to similar ones in the Management Dashboard:

- **PE Metrics Scatter Chart** shows the same information as **PEs** but with the axes swapped

- **Resource Load Chart** is the same as **Resources**.

In addition, there are other cards with useful information:

- A **Summary** card that shows at a glance the health or exception status of jobs, operators, streams, and congestion (and consistent regions, which this lab does not explore).

- A **Streams Tree** that is a lot like the **Streams Explorer** in Studio.

- A **Streams Graph**, similar to the **Instance Graph** in Studio (if you have more than one job running, you’ll have to expand twisties to see their graphs).

- A **Flow Rate Chart** showing the tuple submission rates of all source operators from all jobs.

<img width="100%" src="/tutorials/images/Lab3/4.JPG"/>

The **Flow Rate Chart** is interesting. It shows that the tuple rate is bursty: the source operator (FileSource, in this case) reads the file as fast as it can, until it runs out of data; this fills up the input port buffer of the Throttle, which calmly draws down that buffer at 40 tuples per second. At just about the right time, when the Throttle operator is almost out of data, the same file is reported to the FileSource, which reads it again in one sharp burst. The chart shows the flow rate at zero most of the time, with peaks up to just over 600 tuples per second spaced 45 seconds apart. Note that the chart shows a moving average over three seconds; in reality, the FileSource reads the entire file containing 1902 tuples in less than a second.

 {% include nextPageFinder.html context=page.url %}
 
