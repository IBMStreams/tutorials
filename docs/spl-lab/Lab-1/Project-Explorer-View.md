---
layout: docs
title:  Project Explorer view (optional)
description:
weight: 220
---

# Project Explorer view
---
The Project Explorer shows both an object-based and a file-based view of all the projects in the workspace.

1. In **Project Explorer**, expand **MyProject** by clicking the _twisty_ (triangle) on the left.

    The next level shows namespaces (only one, in this case), a dependencies entry, and resources (directories and files).

1. Under **MyProject**, expand the namespace **my.name.space**.

    The next level shows main composites; other objects, such as types and functions, if you had any, would appear there as well.

1. Under **my.name.space**, expand the main composite **MyMainComposite**.

    The next level shows build configurations; here, there is only one, **Distributed**, created by default. You can create multiple builds, for debug, for standalone execution, and other variations.

1. Expand **Resources**.

    The next level shows a number of directories, as well as two XML files containing descriptions of the current application or toolkit. (In Streams, toolkit and application are the same in terms of project organization and metadata.) The only directory you will use in this lab is the data directory: by default, build configurations in Streams Studio specify this as the root for any relative path names (paths that do not begin with “/”) for input and output data files.

<div class="alert alert-info" role="alert">
<h4>Default data directory</h4>
Beginning with version 4.0, Streams applications do not have a default data directory unless you explicitly set one in the build specification. Here, we are simply taking advantage of a feature of Streams Studio, which will provide that specification by default. It works, because we only have a single host.<br>

Because Streams is a distributed platform that does not require a shared file system, you have to be careful when specifying file paths. A process accessing a file must run on a host that can reach it; in general this means specifying absolute paths and constraining where a particular process can run; using relative paths and a default data directory makes the application less portable.
</div>

# Defining a stream type

Rather than defining the schema (stream type) of each stream separately in the declaration of each stream, create a type ahead of time, so that each stream can simply refer to that type. This eliminates code duplication and improves consistency and maintainability.

Therefore, you’ll begin by creating a type, `LocationType`, for the vehicle location data that will be the main kind of tuple flowing through the application.

<div class="alert alert-info" role="alert">
<h4>The Tuple</h4>
Before we continue to work with streams it is best to define what a tuple, the basic unit of information used in streams, is. A tuple can be considered an ordered list of elements, like a shopping list of information. This list can hold a variety of data types, such as int64, or float64 data, which we will be working with shortly.
</div>

Use the following information to create the stream type:


Table 3. Other application requirements

| Name | Type | Comments |
|------|------|----------|
| id | rstring | Vehicle ID (an rstring uses “raw” 8-bit characters) |
| time | int64 | Observation timestamp (milliseconds since 00:00:00 on January 1, 1970)|
| latitude | float64 | Latitude (degrees) |
| longitude | float64 | Longitude (degrees) |
| speed | float64 | Vehicle speed (km/h) |
| heading | float64 | Direction of travel (degrees, clockwise from north) |

<br>To define a stream type:

1. In the graphical editor for **MySourceFile.spl**, right-click anywhere on the canvas, outside the main composite (MyMainComposite), and choose Edit.

    This brings up a **Properties** view, which floats above all the other views. Make sure it looks as below, with the three tabs for General, Uses, and Types; if not, dismiss it and right-click again in the graphical editor, outside the main composite.

1. In the **Properties** view, click the Types tab.
Select the field under Name, which says Add new type….

    Key in **LocationType**; press Enter.<br>Select the field in the Name column below LocationType, which says Add attribute….<br>Key in id; press Tab to go to the Type column.<br> Key in rstring; Press Tab to go to the next name field.

3. Continue typing and using Tab to jump to the next field to enter the attribute names and types listed in Table 3, above. The fields should look like the Figure below.

<br><img width="60%" src="/tutorials/images/Lab1/2.JPG"/>

  Leave the Properties view open. 
  
  Note: The floating properties view may obscure other views, an alternative is to use the properties tab in the view at the bottom of the perspective.

<div class="alert alert-info" role="alert">
<h4>Content Assist</h4>
In the Type column, use Ctrl+Space to get a list of available types. Begin typing (for example, “r” for rstring) to narrow down the list; when the type you want is selected, press Enter to assign it to the field. This reduces keyboard effort as well as the probability of errors.
</div>

## Check your results
The tuple type LocationType is now available for use as a stream type in any main composite within the namespace my.name.space.

 {% include nextPageFinder.html context=page.url %}
 
