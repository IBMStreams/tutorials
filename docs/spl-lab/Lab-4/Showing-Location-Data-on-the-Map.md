---
layout: docs
title:  Showing location data on the map
description:
weight: 720
---

# Showing location data on the map
---
The NextBus toolkit comes with another application that lets you view data in a way that is more natural for data that involves locations: on a map. Just like MyApplication, it is designed to connect to the kind of stream exported by NextBusIngest and FileIngest. Without any further configuration, it can take the latitude and longitude values in the tuples, along with an ID attribute, and generate an appropriate map.  It is not the prettiest or most dynamic of maps, but real cartography is a lot of work, and this is only intended as a quick method for learning about your data—similar to the views and charts in the Streams Console.

1. In the NextBus toolkit, launch NextBusVisualize. In the Edit Configuration dialog, scroll down to see the Submission Time Values; note the value of the port variable: 8080 (widen the Name column to see the full name).

    In the Instance Graph, each of the two exported streams is connected to each of the downstream jobs. The arrows look a bit confusing, but if you select each of the branches in turn, you can untangle them.

1. To open the map in the Firefox browser, double-click the Live Map desktop launcher.
(Minimize the Studio window or move it out of the way to see it.)

1. You will see a map of the San Francisco Bay Area, with a large number of green markers crowding the city of San Francisco. Use the map controls or mouse wheel to zoom in and pan (hold down the left mouse button to drag and center the map), so you can see the individual vehicles. They jump around as their locations are updated: the map is live!

  The map refreshes every second, but remember that NextBus data is only updated every 30 seconds. If you zoom in far enough (click the   zoom tool five times from the starting level), you can see the simulated cars from the file move continually around downtown San Francisco. (They jump periodically, as the locations start over at the top of the file.)

  Hover over or click any one of the markers to get the full list of attributes for that vehicle.

 {% include nextPageFinder.html context=page.url %}
 