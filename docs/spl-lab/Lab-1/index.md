---
layout: docs
title:  Lab 1 - A Simple Streams Application
description:  Lab Overview
weight: 10
---

# Lab 1 - Developing a simple application
---

In this module, you will develop an application for a simple scenario: read vehicle location, speed, and other sensor data from a file, look for observations of a specific few vehicles, and write the selected observations to another file.

You will create an SPL application project, build an application graph with three operators, configure the operators, run the application, and verify the results.

The application will meet the following high-level requirements:

* Reads vehicle location data from a file
* Filters vehicle location data by vehicle ID
* Writes the filtered vehicle location data to a file


*	Design the application graph in the graphical editor
* Use three operators (an operator is the basic building block of an application graph): one each to read a file (FileSource), write a file (FileSink), and perform the filtering (Filter)
* Take it step by step:

    1. Define a new type for location data, to serve as the schema, or stream type, of several streams

        A schema defines the type, or structure, of each packet of data, or tuple, flowing on the stream. The tuple type is a list of named attributes and their types. Think of a tuple as the Streams analogue of a row in a table or a record in a file, and of its attributes as the analogue of columns or fields.

    2.	Drop the required operators into the editor

    3.	Make the required stream connections to “wire up” the graph

    4.	Define the schema of the streams in the graph

    5.	Specify the parameters and other details of the individual operators
  
## Creating a project
Before you can begin working with streams a .project file is created when you initialize a project. This file contains all of the information eclipse needs to build and run your program.

Project dependencies
In the Dependencies field you can signal that an application requires operators or other resources from one or more toolkits—a key aspect of the extensibility that makes Streams such a flexible and powerful platform. For now, you will only use building blocks from the built-in Standard Toolkit.


You’re ready to start building your application. First you’ll create a Streams project (a collection of files in a directory tree in the Eclipse workspace) and then an application in that project.

The New SPL Application Project wizard takes care of a number of steps in one pass: creating a project, a namespace, an SPL source file, and a main composite.

In Streams, the **main composite** is an application. Usually, each main composite lives in its own source file (of the same name), but this is not required. This lab does not explore the nature of composite operators or what distinguishes a main composite from any other composite.

<div class="alert alert-info" role="alert">
<h4>Extend</h4>
Want to learn more about main composites? Additional information is available in the
<a href="http://www.ibm.com/support/knowledgecenter/SSCRJU_3.0.0/com.ibm.swg.im.infosphere.streams.spl-introductory-tutorial.doc/doc/compositeoperators.html">IBM Knowledge Center</a>
along with other Streams information.
</div>

To create a project:

1. Select *File > New > Project….*

  Alternatively, right-click in the Project Explorer and choose New > Project….

  _Would anyone else object to getting rid of the right-click guidance? I have a feeling that it's the kind of thing a lot of users will figure out for themselves._

  _I think InfoSphere Streams Studio might change. Need to confirm with Mary Komor._
  
1. In the New Project dialog, expand InfoSphere Streams Studio and select *SPL Application Project*. Click *Next*.

2. In the New SPL Application Project wizard, enter the following information:

    * In the **Project name** field, enter MyProject.
    * In the **Namespace** field, enter my.name.space.
    * In the **Main Composite Name** field, enter MyMainComposite.

    <br>Click **Next**.

3. On the SPL Project Configuration panel:

  * Change the Toolkit name to MyToolkit.
  * In the **Dependencies** field, clear **Toolkit Locations**.
  * Click **Finish**.

## Check your results
You should see the following in Streams Studio:

* The new project shows up in the Project Explorer view, on the left.

* The code module MySourceFile.spl opens in the graphical editor, with an empty MyMainComposite in the canvas.

<div class="alert alert-success" role="alert">
<h4>Hint</h4>
If you want to give the editor more space, close the Outline view and collapse the Layers and Color Schemes palettes (this lab does not use them).
</div>
