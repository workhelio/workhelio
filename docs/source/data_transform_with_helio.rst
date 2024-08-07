How to Transform Data Using Helio Extension
===========================================

Another form of transforming data in Workhelio is with the use of helio extension. This extension is available in Chrome. You can download it here `here <https://chromewebstore.google.com/detail/helio-sql-query-assistant/mkiekcaeimlglkkenkfomllindljjihe>`_.   

.. figure:: /_static/images/helio_transform/img_01.png
   :width: 80%
   :align: center
   :alt: Extension Image

.. _steps_to_use_helio_extension_to_transform_data:

Steps to Use Helio Extension to Transform Data
----------------------------------------------

The following steps will help you use the helio extension to transform your data:
  
1. Open the Extension

Once you are done downloading the helio extension, open it to start using it. You can pin it at the top of your browser. When you open it, it looks like this:

.. figure:: /_static/images/helio_transform/img_02.png
   :width: 80%
   :align: center
   :alt: Example Image

  
2. Create a Dashboard

Click on the plus (+) button on the top right of the screen to create a dashboard. 

.. figure:: /_static/images/helio_transform/img_03.png
   :width: 80%
   :align: center
   :alt: Example Image


Select the “Dashboard” option inside the modal that appears after clicking the plus button.

.. figure:: /_static/images/img_002.png
   :width: 80%
   :align: center
   :alt: Example2 Image


.. figure:: /_static/images/img_003.png   
   :width: 80%
   :align: center
   :alt: Example3 Image


3. Name Your Dashboard
    
After selecting the dashboard, you will be taken to the dashboard page. On the top-left of the screen, edit the title of your dashboard to the title of your choice. 

.. figure:: /_static/images/img_004.png
   :width: 80%
   :align: center
   :alt: Example4 Image


Let's name our dashboard “Transform Data”. Click the save button on the top-right of the screen to save the title.

.. figure:: /_static/images/helio_transform/img_04.png
   :width: 80%
   :align: center
   :alt: Example5 Image   


4. Edit the Dashboard to Create a New Chart

After saving the dashboard name, click the edit dashboard button to create a new chart. 

.. figure:: /_static/images/img_006.png
   :width: 80%
   :align: center
   :alt: Example6 Image


The page will change and you will see a new button - “CREATE A NEW CHART”, click on it. 

.. figure:: /_static/images/img_007.png
   :width: 80%
   :align: center
   :alt: Example7 Image


This will take you to a new page where you will select the chart type you want and build your preferred dashboard chart. 

5. Choose Your Dataset and Chart Type

Choose a dataset to work with among the list of datasets in the select input options. We are going to select mock_employee_data as our option in this example. 

.. figure:: /_static/images/img_008.png
   :width: 80%
   :align: center
   :alt: Example8 Image    


Select the chart type. In this example, we are going to select the bar chart under the list of popular charts.

.. figure:: /_static/images/img_009.png
   :width: 80%
   :align: center
   :alt: Example9 Image


When you are done, click on the “CREATE NEW CHART” button at the bottom of the page. 

.. figure:: /_static/images/img_010.png
   :width: 80%
   :align: center
   :alt: Example10 Image

6. Select Your Data Source And Transformation Type, And Input Column Name in the Extension

In the extension, click on "Transform Data" at the top of the screen. You can then select your choice from the list of data sources. In this example, we will select Google BigQuery.  

.. figure:: /_static/images/helio_transform/img_05.png
   :width: 80%
   :align: center
   :alt: Example10 Image

Next is to select the transformation type. We are going to choose "Format date to MM/DD/YYYY" in this example.

.. figure:: /_static/images/helio_transform/img_06.png
   :width: 80%
   :align: center
   :alt: Example10 Image

You will then input the name of the column whose data you want to transform. Let's transform the data in "Order Date". Click on the "Run" button below the input once you are done to run it. 

.. figure:: /_static/images/helio_transform/img_07.png
   :width: 80%
   :align: center
   :alt: Example10 Image

7. Copy The Result And Paste It Into Your Chart 

Now, you copy the result from from the helio extension and paste it into the chart. 

.. figure:: /_static/images/helio_transform/img_08.png
   :width: 80%
   :align: center
   :alt: Example10 Image

Select and configure data for the x-axis and metrics, ensuring your visualizations accurately represent your data. Choose the CUSTOM SQL option under the X-AXIS modal and customize your data. 
    
.. code-block:: SQL

   FORMAT_DATETIME("%x", DATE(`Order Date`))

In the command above, the code will transform the date. After converting our age column to a string, we can equally concatenate another string to it. 

.. code-block:: SQL

   CONCAT(CAST(age AS STRING), " years old")

The command above will concatenate “ years old” to the age column string. Write the command inside the CUSTOM-SQL and save it as shown below:

.. figure:: /_static/images/img_011.png
   :width: 80%
   :align: center
   :alt: Example11 Image


Choose your metrics and save. 

.. figure:: /_static/images/img_012.png
   :width: 80%
   :align: center
   :alt: Example12 Image

6. Visualize and Complete the Chart Creation

Click the “CREATE CHART” button at the bottom of the page to visualize your new chart. 
    
.. figure:: /_static/images/img_013.png
   :width: 80%
   :align: center
   :alt: Example13 Image


.. figure:: /_static/images/img_014.png
   :width: 80%
   :align: center
   :alt: Example14 Image

On the top-left of the page, add the name of the chart and click on the “SAVE” button at the top-right of the screen.

.. figure:: /_static/images/img_015.png
   :width: 80%
   :align: center
   :alt: Example15 Image


The save button opens a save modal where you can complete your chart creation. 

.. figure:: /_static/images/img_016.png
   :width: 80%
   :align: center
   :alt: Example16 Image
    

.. _list_of_commands_to_transform_data:

List of Commands to Transform Data
----------------------------------

Similar to how we convert column data above from one data type to another, there are other data transformations that we can carry out on Workhelio. 

The following are commands to transform data in Workhelio:

1. Data Type Conversion 

.. code-block:: SQL

   CAST(age AS STRING)

Where ``age`` is the data column and ``STRING`` is the data type you are converting to.


2. String Concatenation

.. code-block:: SQL

   CONCAT(CAST(age AS STRING), " years old")


3. Format Date 

.. code-block:: SQL

   FORMAT_DATE('%x', `Order Date`)

Where ``Order Date`` is the data column for the date.


4. Format Time 

.. code-block:: SQL 

   FORMAT_TIME('%H:%M', PARSE_TIME('%I:%M %p', `ClockIn Time`))

Where ``ClockIn Time`` is the data column for the time.
    
  
