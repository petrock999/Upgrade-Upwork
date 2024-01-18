# Updating Upwork

# Sprint 2 Updates:
The project is moving along! 

By analyzing the 3D Modeling Category using N-Grams, we could gather some insights. For instance, Upwork recruiters are keen on Unreal Engine. 

The Baseline Model will consist of a RNN model, which still needs to be heavily tuned to get acceptable results. Right now it appears to be overfitting.

I'm also interested in trying Pretrained models, which produce better results. A lightweight version of Falcon by vilsonrodrigues is of particular interest:

https://huggingface.co/vilsonrodrigues/falcon-7b-instruct-sharded

# TODO
* Implement GUI

* Imputing missing categories from job titles
* Creating a better RNN model with regularization, more training data or dropout

* Finetuning pretrained model
* Trying Falcoln with more parameters
* Changing Falcoln configuration, e.g. Top P, Temperature
* Finetuning other pretrained models, e.g. Llama, Mistral


# Broad Overview

My capstone project will revolve around the Upwork Dataset, created by Kaggle user Ahmed Myalo.

https://www.kaggle.com/datasets/ahmedmyalo/upwork-freelance-jobs-60k?select=Final_Upwork_Dataset.csv

The features I'm particularly interested on are (as written by Ahmed on the Kaggle post):

    - Job Title: Specifies the nature of the job. It aids potential applicants in quickly understanding the role that client needs.
    - EX_level_demand: Describes the skill tier desired. Helps candidates evaluate if they are a fit for the job. (there's 3 tiers on the site: "Entry level & Intermediate & Expert")
    - Description: the full description of the job which client wrote.
    - Category_1 to Category_9: These columns specify categories of skills that the client wrote as relevant to the job. Each category column is paired with a corresponding URL ("CategoryX_URL_search") which leads to a search page for requiring the specified skill.
    - Search_Keyword: the keyword I've used in the search bar to get that row result. I've used (3D & Data science & Developer & Marketing) but I didn't scrap these fields with the same quantity.
    - Applicants_Num: number of the freelancers who have applied for that job yet. A high number might deter someone from applying.
    - Highlight: it's an indicator about this job.
    - Job_Cost: it's for "Fixed-price" projects; The projected budget can help freelancers gauge the project's scale and value.
    - Connects_Num: connects are the currency of the site; the freelancers buy every 10 connects for 1.5$ . so the more job costs the less freelancers applying for it.
	
However, further exploration of the dataset and expansion of the scope of the project could warrant more features being taken into consideration.

The current scope of the project aims to extract key skills and requirements from the job descriptions in order to better understand the most in-demand skills in different sectors, allowing freelancers to focus on the development of those skills.

Since the dataset also contains the how much each applicant offers for the employer to push their offer up the ranks of visibility - Upwork names this currency "connects" - I would be able to examine job popularity and competition, to see what jobs are chased and what niches are oversaturated or otherwise.

In the end, the project aims to provide various insights, being able to guide the freelancer into what sort of job is typical, what title and description it tends to have, what skills are typically required, and the competition to be expected. It would also produce examples of atypical jobs and jobs other members of Upwork aren't applying for, to allow the freelancer to seek out potential niches.

I aim to later expand this model to include more categories of Upwork, particularly video production and writing, with an expanded database that contains those categories in the future.
