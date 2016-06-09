---
layout: docs
title:  Adding a window-based operator to your application
description:
weight: 410
---

# Adding a window-based operator to your application
---
You will compute average speeds over a window, separately for vehicles C101 and C133. Use a tumbling window of a fixed number of tuples: each time the window has collected the required number of tuples, the operator computes the result and submits an output tuple, discards the window contents, and is again ready to collect tuples in a now empty window. Window partitioning based on a given attribute means that the operator will allocate a separate buffer for each value of that attribute—in effect, as if you had split the stream by attribute and applied a separate operator to each substream. The specifications are summarized in Table 5, below.

<b>Table 5. Specifications for window-based aggregation</b>

| Specification | Value |
|-------------------------|----------------------------------------------------------------|
| Operator type | Aggregate |
| Window Specification | Tumbling, based on tuple count, 5 tuples |
| Window partitioning | Yes, based on vehicle ID (id) |
| Stream to be aggregated | Filtered |
| Output schema | id             - rstring time         -int64 avgSpeed -float64 |
| Aggregate computation | Average(speed) |
| Results destination | File: average.speed |

<br>

1. 	Add the two required operators.

    a. 	In the graphical editor’s palette filter box, type agg; drag an Aggregate operator into the main composite. The editor calls it Aggregate_6. This is you main analytical operator.
    
    b. 	In the palette filter, begin typing filesink until you see the FileSink operator; drag one into the main composite: FileSink_7. This will let you write the analytical results to a file.
    
2. 	Fold the two new operators into the graph by connecting one existing stream and adding another.

    a. 	Drag a stream from Filtered to Aggregate_6. This means Aggregate_6 is tapping into the same stream as Writer is already consuming, so the schema is already defined. This is indicated in the editor by a solid arrow.
    
    b. 	Drag another stream from Aggregate_6 to FileSink_7. This stream does not yet have a schema, so the arrow is dashed.
    
    Click   Layout and   Fit to Content.

3. 	Rename the new stream and operators.

    a. 	Rename the stream to Averaged.

    b. 	Rename the Aggregate operator to Averaged by blanking out its alias.
    
    c. 	Rename the FileSink to AvgWriter.
    
4. 	Give the Averaged stream (output of the Aggregate operator) its own schema. In the Schema tab of the Properties view for the stream, fill in attribute names and types.

    a. 	In the first field under Name, type id; press Tab.
    
    b. 	Under Type, type rstring; press Tab to go to the next name field.
    
    c. 	Continue typing (and using Tab to jump to the next field) to enter the output schema attribute names and types listed in Table 5 on page 32.

5. 	Tell the Aggregate operator what to do.
    
    a. 	Select the Averaged operator; in the Properties view, go to the Window tab. A placeholder window specification is already filled in; you only need to edit it slightly.
    
    <ol type="I"> 
    
        <li>Click Edit…;</li>
        
        <li> 	in the Add Window Mode… dialog, keep Tumbling Window selected;</li>
        
        <li> 	set Eviction policy value to 5;</li>
        
        <li> 	check Partitioned (leave Eviction policy blank); and </li>
        
        <li> 	click OK.</li>
        
        </ol>
        
    <img width="50%" src="/tutorials/images/Lab3/3.jpg"/>

    b. 	Configure the window as partitioned on vehicle ID (the id attribute).
    
    <ol type="I">
    
    <li>	In the Param tab, click Add…</li>
        
    <li> 	in the Select parameters dialog, check partitionBy and click OK.</li>
        
    <li> 	In the partitionBy value field, enter id.</li>
        </ol><br>
        
    c. 	Go to the Output tab (you may have to scroll down the list of tabs, or make the Properties view taller) to specify the output assignment. Expand the twisty in front of Averaged in the Name column; you may have to widen the columns and enlarge the view horizontally to see the full Name and Value columns. The attributes id and time will simply be copied from the most recent input tuple. This is already reflected in the Value column; by default, output attribute values are assigned from attributes of the same name, based on the last input tuple. <br> <br>Since the window is partitioned by id, all tuples in a window partition will have the same value for this attribute. This is not the case for time, but in this example it is reasonable to use the most recent value.
    
    <ol type="I">
    
    <li>	Click Show Inputs; expand the Filtered twisty, and again LocationType. This shows the attributes you can use to create an output assignment expression.</li>
        
    <li> 	Click in the value field for avgSpeed; type Ctrl+Space for content assist. In the list of possible entries, choose (double-click, or select and Enter) Average(T) : T. (The syntax simply means that for any input type T, the output value will also be of type T.) This inserts Average(T) into the field.</li>
        
    <li> 	Again click in the value field for avgSpeed; delete the T inside the parentheses and keep the cursor there. Type Ctrl+Space to bring up content assist, and this time choose speed - float64.</li>
        </ol>	
        
    <div class="alert alert-info" role="alert">
    <h4><b>Custom output functions</b></h4>
    The functions shown in content assist are custom output functions specific to the Aggregate operator. They are not general-purpose SPL functions. Every output assignment must contain a call to one of these. The automatic assignments for the non-numeric attributes described above implicitly call the Last(T) custom output function.
    </div>
    
6. 	Specify where the results go: select the newly added FileSink operator (AvgWriter).
    a. 	In the Param tab, set the file parameter to "average.speeds" (with the double quotes).
    b. 	Click Add…; in the Select parameters dialog, check format and quoteStrings; click OK. Set format to csv and quoteStrings to false.
    c. 	Save. Close the Properties view. Your application is ready to launch.
    
7. 	Launch the application. Right-click MyMainComposite in the Project Explorer and choose Launch…. Click Apply (if necessary) and Continue in the Edit Configuration dialog.

 {% include nextPageFinder.html context=page.url %}
 