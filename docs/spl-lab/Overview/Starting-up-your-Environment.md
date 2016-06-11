---
layout: docs
title:  Setting up your environment
description:
weight: 110
---

# Setting up your environment
---
To use the lab, you must have either IBM Streams Quick Start Edition (QSE) VMWare Image or IBM Streams installed.

The [IBM Streams Quick Start Edition (QSE) VMware Image](https://www.ibm.com/services/forms/preLogin.do?source=swg-ibmistvi&S_TACT=M161075W) is recommended, and the instructions for the lab assume that you are running the QSE.

The following software is already installed on the QSE VMware image:

* Red Hat Enterprise Linux 6.5 (64-bit)
* IBM Streams QSE 4.1.1.0, including Streams Studio

The QSE VMware Image has the following configuration:

| Parameter | Value |
|-----------|-------|
| Host name | streamsqse (streamsqse.localdomain) |
| User and administrator ID | streamsadmin (logged in automatically) |
| User home directory | /home/streamsadmin |
| User password | passw0rd (password with a zero for the O) |
| root password | passw0rd |
| Streams domain | StreamsDomain (started automatically) |
| Streams instance | StreamsInstance (started automatically) |

<br>In the QSE VMware Image, a domain (StreamsDomain) and instance (StreamsInstance) have already been created and automatically started. This means that everything you need to run and test your applications is already prepared for you.

A **domain** is a logical grouping of resources in a network for the purpose of common management and administration. The domain is managed by a small number of Linux services (daemons) for tasks such as authentication and authorization, auditing, supporting the Streams Console, etc.

A domain can contain one or more Streams **instances** that share the domain’s security model. An instance provides the runtime environment that you can submit applications to. It consists of a small number of additional services; this includes a resource manager, an application manager, and a scheduler, among others.

The lab does not explore the creation and administration of domains and instances.




<div class="alert alert-info" role="alert">
<h4>Alternative environments</h4>
<p>You aren't required to use the Quick Start Edition VMware image. You can install and run the lab in any other environment with a current Streams installation.</p>

<p>However, some things might look different, depending on how closely your environment matches the QSE virtual machine setup described above.</p>

<p>Additionally, your environment might not have the shortcuts that are used to start the different tools used in this lab.<br>
</p></div>

### Installing the lab
After you start the QSE VMware image, you need to install the lab projects, data files, and toolkits.

To install the lab:

1. In the VMware Image, open the Firefox browser (in the VMware image) and go to the Introductory Streams Lab page on Streamsdev at  https://developer.ibm.com/streamsdev/docs/streams-lab-introduction/.

1. Open the link to the current version: 4.1.1.

1. Follow the instructions for installing the lab on that page.

#### Check your results
If you successfully installed the lab files, your VMware desktop should look like the following graphic:

<img width="100%" src="/tutorials/images/Overview/desktop.png"/>

 Your domain and instance are ready to run your applications.
 
 {% include nextPageFinder.html context=page.url %}
