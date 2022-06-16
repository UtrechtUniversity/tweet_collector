# Setup Environment

You can run 'tweet_collector' on **ResearchCloud** or on **your local computer**.

## ResearchCloud

In this approach you do not need to install any application. The Research Engineering team in collaboration with the Research IT, provide a ready-to-run environment for tweet_collector. It is a workspace with pre-installed python and other required software applications running on Surfsara ResearchCloud.

### Step 1: Apply for an account on ResearchCloud
Send an email to Ton Smeele (A.P.M.Smeele@uu.nl) to request for an account.


### Step 2: Create a new Workspace
1. Go to [surfresearchcloud.nl](https://portal.live.surfresearchcloud.nl/)
2. Select Identity Provider (e.g., Utrecht University)
3. Sign in to your Identity Provider to validate your identity 
4. Go to `create new workspace` and click on `create new`
5. Select `Tweets Collector` and click `continue`
6. Select collaborative organisation (i.e., a group of connected researchers who can also enter the VRE)
7. Click `continue without selection`
8. Select a wallet & choose cloud provider, click `continue`
9. Click on `continue without selection`
10. Choose the expiration date of the machine, Give the VRE a name and description (optional).
11. Click on the checkbox of agreement on the Terms and Conditions .
12. Click on submit button .


### Step 3. Login to a Research Cloud workspace

1. Go to [surfresearchcloud.nl](https://portal.live.surfresearchcloud.nl/)
2. Select Identity Provider (e.g., Utrecht University)
3. Sign in to your Identity Provider to validate your identity 
4. In your `dashboard`, under `Your Workspaces` you see current 'workbenches'. To run this VRE, click on the yellow 'access' button. This will open the VRE.

**Note** In order to copy and paste text between your local computer and your workspace on cloud, you can save it in a .txt file and transfer it via SCP command.

1. Open a terminal on your local computer and type the following command. 

```sh
    scp [txt_to_copy.txt] [Usernames@ip-address]:/txt_to_copy.txt
 ```
2. Please change the parts in the square brackets:
    - [txt_to_copy.txt]: name of the file you want to transfer
    - [Usernames@ip-address]: username and ip-address can be found in the description page of your workspace.
  
## Local 

### Step 1: Install Requirements

Here is the list of requirements

- Python 3.8
- [Docker compose](https://docs.docker.com/compose/install/)

### Step 2: Install tweet-collector

To get a local copy up and running follow these simple steps.

2.1. Open a **Terminal** 

2.2. Clone the repo
```sh
    git clone https://github.com/UtrechtUniversity/tweet_collector.git 
```    
2.3. Navigate to 'tweet_collector' directory   
```sh
    cd tweet_collector 
```
2.4. (Optional but recommended) Create and activate a virtual environment
   ```sh
    python -m venv [myenvname]
    source [myenvname]/bin/activate
```
2.5. Create package file
```
poetry build
```
2.6. Install package through pip
```
pip install ./dist/tweet_collector_version.whl
```

In this step, the environment is ready to use. In order to start with searching tweets, go to '3_Search_Tweets.md'.