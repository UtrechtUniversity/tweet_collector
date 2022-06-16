# Visualizing Twitter Data
After collecting tweets, the next step is to visualize this data for further analysis. In this guideline we explain how to visualize tweets using Elasticsearch/Kibana. Here are the steps:

1. Running Elasticsearch and Kibana using Docker
2. Loading the extracted tweets into Elasticsearch
3. Visualizing the data in Kibana

## 1. Run Elasticsearch/Kibana

To run Elasticsearch/Kibana, you can use a docker image called `docker-compose.yaml`, available via the 'tweet_collector' repo. Type the following code in Terminal:

```
cd tweet_collector
docker-compose up -d
```
If the process is done completely, you should find home page of elasitc in http://localhost:5601 

## 2. Load data
To upload your data into Elastic, you need to run the following code in your terminal:

```
cd tweet_collector
sh load_elastic.sh
```

**Note:** This script uploads all the json files starting with `filename_prefix`  mentioned in `config/api_config.config`.


For example, considering `guidelines/example/api_config.config`, all files in 'output/happiness[x].json will be uploaded to elasticsearch.

## 3. Kibana
### Adding data in Kibana
Now, when you click on `Kibana visualize & analyze` you can add the imported data. To do this, perform the following steps:

1. Click on `Add your data`
2. Click on `Create index pattern`
3. Provide an index pattern name, in this case *twitter*, and click `Next step`
4. Select time field,'created_at'.
5. Click `Create index pattern`
6. The final step is an overview of the imported data and it's mapping/type structure.\* You don't need to change anything.


### Creating a dashboard
To create a visualization of the twitter data:
1. Select `Dashboard` from the main menu in the upper left corner, in `Analytics` section.
2. Click on `Create new dashboard`
3. Click on `Create panel`. It shows multiple visualization options.
4. You can choose `Lens` which is recomended for many users.

**Notes**
- By dragging fields to the center of the screen, you can create graphs. You can personalize the graphs by means of form (e.g., stacked bar, area, bar, etc.) and by defining `Break down by`, splitting up your graph even further. 

- Make sure to select the right timeframe (see calender icon on the right of the screen) matching your Twitter filter. The default value of this 'time filter' is '15 minutes ago - now'. So, for example, if you've filtered tweets untill a certain end date (that is before 15 minutes ago), this will leave you with an empty list of `Available fields`.

- For more information about what you can do with Kibana, have a look at [this web page](https://www.elastic.co/guide/en/kibana/current/discover.html).

## 4. Saving data
As you are working on a virtual research environment, it is essential to save all your data on another location before closing off the environment.

### Saving twitter data
To ensure you've saved all the extracted tweets, make sure to save the output .json file.

### Saving visuals
The visuals you've created can either be saved as:
* a csv (see button `Download as CSV`, which translates your graph/visualization into a table in csv format).
* an image (by right clicking on the created visual, you can save the visual as image).