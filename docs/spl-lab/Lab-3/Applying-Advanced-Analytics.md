---
layout: docs
title:  Applying advanced analytics
description:
weight: 400
---

# Lab 3 - Applying advanced analytics
---

In this part, you will enhance the app you’ve built by adding an operator to compute an average speed over every five observations, separately for each vehicle tracked. After that, you will use the Streams Console to visualize results.

So far, the operators you’ve used look at each tuple in isolation; there was no need to keep any history. For many analytical processes, however, it is necessary to remember some history to compute the desired results. In stream computing, there is no such thing as “the entire dataset”, but it is possible to define buffers holding a limited sequence of consecutive tuples—for example, to compute the average over that limited subset of tuples of one or more numeric attributes. Such buffers are called windows. In this part, you will use an Aggregate operator to compute just such an average.

## Prerequisites

<div class="alert alert-warning" role="alert">
<h4><b>Note</b></h4>
If you are confident that your results from the previous part are correct, you can continue working with them and skip this section.
</div>

To continue with this part even if you did not successfully complete the previous part, import a Streams project that has been prepared for you, containing the expected results of Part 2.

1. In the Project Explorer, right-click on the current project (MyProject or MyProject1) and choose Close Project. This gets it out of the way for builds or name conflicts, without deleting any files.

1. In the top Eclipse menu, choose File > Import….

1. In the Import dialog, select InfoSphere Streams Studio > SPL Project; click Next >.

1. Click Browse…; in the file browser, expand My Home and select Labs. Click OK.

1. Select (check the box) MyProject2 and click Finish.

    This kicks off a build, but there is no need to wait until it finishes.

1. In the Project Explorer, expand MyProject2 and then my.name.space.

1. Double-click MyMainComposite to open it in the graphical editor.
