---
layout: docs
title:  Splitting off the ingest module
description:
weight: 620
---

# Splitting off the ingest module
---
Now it gets interesting. Within a Streams application, data flows from operator to operator on <b>streams</b>, which are fast and flexible transport links. The Streams application developer is not concerned with how these are implemented. They may work differently between operators running on different hosts, in different PEs on the same host, or within the same PE, but the logic of the graph stays the same. When an application needs to exchange data with the outside world, that requires the explicit use of <b>source</b> and <b>sink</b> operators—for file I/O, ODBC, TCP, UDP, or HTTP connections, message queues, and so on.

For Streams applications running in the same instance, however, another mode of data exchange is possible: <b>Export</b> and <b>Import</b>. An application can export a stream, making it available to other applications running in the instance; one or more applications can import such a stream, based on flexible criteria. Exported streams, once they are connected, are just like all the other streams that run between PEs within an application—fast and flexible. It’s only at the time a job is submitted or canceled that the runtime services get involved to see which links need to be made or broken; once that’s done, there is no difference in runtime behavior (well, almost none, but the difference is beyond the scope of this lab), and there is no performance penalty.

But there is a tremendous gain in flexibility. Application stream connections can be made based on publish-and-subscribe criteria, and this allows developers to design completely modular solutions, where one module can evolve and be replaced, removed, or replicated, without affecting the other modules. It keeps individual modules small and specialized.
In the lab so far, you have built a monolithic app, but there is a logical division. The front end of the app, from DirectoryScan to Throttle, is concerned with reading data, in this case from files, and “replaying” that data in a controlled fashion to make it look like a real-time feed. The rest of the app, from Split to FileSinks, performs analysis and writes out the results. If you split off the front end into a separate “Ingest” module, you can imagine that it would become easy to have another module, alongside it or as a replacement, that produces tuples that have the same structure and similar contents, but that come from a completely different source. And that is exactly what this part will do: add another module that reads a live data feed and makes the data available for processing by the rest of this application.

1. 	In the graphical editor, drag a <b>Composite</b> (under <b>Design</b> in the palette) and drop it on the canvas. Not on the existing main composite, but outside of any graphical object. The editor will call it Composite; rename it to <b>FileIngest</b>.

    Notice that the new composite appears in the Project Explorer, but it does not have a build associated with it. Create one.
    
    2. 	In the <b>Project Explorer</b>, right-click the <b>FileIngest</b> main composite. Choose <b>New > Distributed Build</b>. In the dialog that pops up, change the <b>Configuration name</b> to Distributed, accept all other defaults, and click OK.

3. 	Move the three front-end operators from the old main composite to the new.
    
    a. 	In <b>MyMainComposite</b>, select the three operators <b>Files</b>, <b>Observations</b>, and <b>Throttled</b>.

    To do this, hold down the Ctrl-key while clicking each one in turn. Cut them (Ctrl+X or right-click, Cut) to the clipboard.

    b. 	Select the FileIngest composite; paste the three operators in (Ctrl+V or right-click, Paste).
    
    You now have two applications (main composites) in the same code module (SPL file). This is not standard practice, but it does work. The applications, however, are not complete: you have broken the link between <b>Throttled</b> and <b>IDChecker</b>.

4. 	Set up the new application (<b>FileIngest</b>) for stream export.

    a. 	In the palette, find the <b>Export</b> operator and drop one into the <b>FileIngest</b> composite.
    
    b. 	Drag a stream from <b>Throttled</b> to the <b>Export</b> operator. Note that the schema is remembered even while there was no stream, since it belongs to the output port of <b>Throttled</b>.
    
    c. 	Edit the <b>Export</b> operator’s properties; Rename it to FileExporter.
    
    d. 	In the <b>Param</b> tab, add the properties parameter. In the <b>Value</b> field for properties, enter the following “tuple literal”:<br>{ category = "vehicle positions", feed = "sample file" }

    What this does is “publish” the stream with a set of properties that are completely arbitrary pairs of names and values. The idea is that an importing application can look for streams that satisfy a certain subscription: a set of properties that need to match.

    e. 	Save. The <b>FileIngest</b> application builds, but <b>MyMainComposite</b> still has errors.
    
5. 	Set up the original application for stream import.
    
    a. 	In the palette, find the Import operator and drop it into the old main composite.
    
    b. 	Drag a stream from <b>Import_11 to IDChecker.
    
    c. 	Assign a schema to this stream, by dragging and dropping LocationType from the palette.
    
    d. 	Rename the new stream to Observations. (There is already another stream called Observations, but it is now in a different main composite, so there is no name collision.)
    
    e. 	Select the Import operator and Rename it to Observations by blanking out the alias.
    
    f. 	In the Param tab, edit the Value for parameter subscription. Replace the placeholder parameterValue with the following boolean expression:<br>category == "vehicle positions"

    Notice that this is only looking for one property: the key category and the value "vehicle positions". It is perfectly fine to ignore the other one that happens to be available; if the subscription predicate is satisfied, the connection is made (as long as the stream types match).

    g. 	Save.
6. 	Test the new arrangement of two collaborating applications.

    a. 	In the Instance Graph, cancel any remaining jobs. Set the color scheme to Flow Under 100 [nTuples/s]. Enlarge the view so you can comfortably see the two jobs.
    
    b. 	In the Project Explorer, launch the old application, MyMainComposite.
    
    c. 	Launch the new application FileIngest.
    
Notice that the tuples flow from operator to operator throughout the instance graph, even though they are divided into two main composites. Leave the two applications running; you’ll be adding a third.

<img width="100%" src="/tutorials/images/Lab4/1.jpg"/>

 {% include nextPageFinder.html context=page.url %}
 