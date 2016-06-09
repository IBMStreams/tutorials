---
layout: docs
title:  Creating an application graph
description:
weight: 240
---

# Creating an application graph
---

You are now ready to construct the application graph.

| Parameter | Value |
|-----------|-------|
| Input file | /home/streamsadmin/data/all.cars |
| Output file	| filtered.cars |
| File format	 | CSV (both input and output) <br>Do not quote strings on output |
| Filter condition | vehicle ID is “C101” or “C133” |
| Stream names | Observations (before filter) <br>Filtered (after filter)|


<br>With this information, you can create the entire application. You will use the graphical editor. There will be no SPL coding in this lab.

<div class="alert alert-info" role="alert">
<h4>Want to see code?</h4>
If you do want to see SPL code for what you are creating, just right-click anywhere in the graphical editor and choose Open with SPL Editor.
Explaining what you see there is beyond the scope of this lab.
</div>

# Adding operators to your application graph
_What are operators? What do they do in the application?_

Operator templates
Some operators appear once in the palette; others (the ones you used) have twisties and expand into one or more subentries. These are templates: invocations of the operator with specific settings—for example, a Filter operator with a second output port to produce rejected tuples. In this lab, the generic version (with the twisty) is always the right one; don’t use the templates.

Operator names
The editor generates placeholder names for the operators you drag onto the canvas, consisting of the operator kind (“FileSink”) and a sequence number (“1”). The sequence number depends on the order in which the operators are added to the graph, and yours may not match this document. You can safely ignore that: it does not affect anything in the application, and in any case you will change the generated names later, to match the role each operator plays.

Organize layout and maximize in view
To organize the layout, click the   Layout button in the editor’s toolbar; to zoom in and use all of the space in the graphical editor canvas, click the   Fit to Content button. The slider in the toolbar lets you manually control the zoom level.


### Before you begin
First, you will reduce clutter in the palette. Initially, the list of toolkits is long, because it shows all toolkits that Streams Studio knows about; in your preconfigured lab workspace, that means all toolkits installed with Streams. For now, you will not use any of those toolkits (and you have not declared any dependencies), so it is not helpful to have them in the palette.


To drop the operators you want into the editor, you need to find them in the palette: this is the panel to the left of the canvas, showing various elements under the headings Design, Toolkits, Exported Streams, Governance Catalogs, and Current Graph.

You are looking for three specific operators: FileSource, FileSink, and Filter. You can filter the palette contents and quickly get the ones you want.

To add operators to your application graph:


1. In the graphical editor for MySourceFile.spl, go to the palette filter field (showing Find), and type fil. As it happens, this narrows the palette down to a list that includes the three operators you need. Select each of the ones with a twisty in front of it in turn and drag it into the MyMainComposite main composite (make sure the green handles appear before you let go). The editor names the operators: FileSink_1, FileSource_2, and Filter_3.

<div class="alert alert-danger" role="alert">
<h4><b>Note</b></h4>
  Make sure that the main composite MyMainComposite, and not one of the previously added operators, is highlighted when you drop the next operator. If a Confirm Overwrite dialog comes up, simply click No and try again.<br><br>
  If you drop the operator on the canvas outside the main composite, the editor creates a new composite (called Comp_1) and places the operator there. If that happens, simply undo (Ctrl+Z or Edit > Undo Add Composite with Operator) and try again.
  </div>

# Adding streams to your application graph

To add streams to your application graph:

1. Add a stream connecting FileSource_2’s output to Filter_3’s input.

    Output ports are shown as little yellow boxes on the right side of an operator; input ports on the left. To create a stream, click on an output port and start dragging. The cursor changes to a + cross, dragging a line from the output port. Release the mouse button as you drag, and click on the input port of another operator (it turns green when you hover over it) to complete the link. The two ports are now connected by a dashed line, indicating that there is a stream but its type is not yet defined.

1. Add another stream, from Filter_3 to FileSink_1. Click  Layout and Fit to Content to organize the graph.

1. Save your work: use Ctrl+S or the   Save toolbar button, or File > Save in the menu.

<div class="alert alert-info" role="alert">
<h4><b>Hover Popups</b></h4>
By default, hovering over an operator in the graphical editor brings up a popup showing the SPL code behind that operator. As you build and lay out the graph, these popups may get in the way. Click the Toggle hover toolbar button to turn off these popups.
</div>

### Check your results
The main composite as well as the three operators it contains now have   error indicators. This is expected, as the code so far contains only placeholders for the parameters and stream types, and those placeholders are not valid entries.
