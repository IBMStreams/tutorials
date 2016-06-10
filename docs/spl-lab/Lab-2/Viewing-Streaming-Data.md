---
layout: docs
title:  Viewing streaming data
description:
weight: 330
---

# Viewing stream data
---

While developing, you often want to inspect not just the overall tuple flow, but the actual data. In Part 1 you simply looked at the results file, but you can also see the data in the Instance Graph. This way, you don’t have to add FileSinks whenever you want to capture the output of a particular operator. Let’s look at the input to and output from the Filter operator to see if it’s working as expected.

1. In the Instance Graph, right-click on the stream Throttled (output of the Throttled operator, input to Filtered); choose Show Data. (If you get an Untrusted Certificate Trust Manager message, select Permanently accept the certificate and click OK.)

    In the Data Visualization settings dialog, verify that the tuple type is what you expect (attributes id, time, latitude, longitude, speed, and heading) and click OK. A Properties view appears.

1. Repeat the previous step for the stream Filtered (between operators Filtered and Writer). Move and resize both Properties views so you can see the both tables as well as the Instance Graph.

  Notice that, as expected, the Filtered stream contains only tuples with an id value of “C101” or “C133”, whereas the Throttle output contains a greater mix of vehicle IDs:
  
<img width="100%" src="/tutorials/images/Lab2/4.jpg"/>


  When you have seen enough data, dismiss the two floating Properties views.

 {% include nextPageFinder.html context=page.url %}
 