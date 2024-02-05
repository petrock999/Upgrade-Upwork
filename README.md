<div class="alert"  style="background-color:#1f2e6b; color:white; padding:0px 5px; border-radius:10px;"><h2 style='margin:10px'>Project Overview</h2></div>

# Goal of My Project

The primary goal of this project is to `extract and identify the underlying themes or topics that frequently occur in job descriptions across different categories`
# Utility of the Project
1. **Identifying Market Trends:** This analysis allows freelancers to understand current market trends, enabling them to adapt their skills and services to meet market demands.
2. **Skill Development:** By revealing in-demand skills and areas of expertise within various job categories, freelancers can prioritize their learning and development efforts towards acquiring high-demand skills.
3. **Personal Branding and Marketing:** Understanding prevalent topics enables freelancers to tailor their personal branding and marketing efforts, aligning their profiles, pitches, and portfolios with in-demand topics and skills to attract potential clients more effectively.
4. **Niche Specialization:** Analyzing topics within specific job categories helps freelancers identify niche areas that may be underserved, setting them apart from the competition.
In summary, insights from my model will enable freelancers to strategically position themselves in the market, making informed decisions about which projects to pursue or which clients to target.

# Methodology
The project employs `Natural Language Processing (NLP)` and machine learning models to cluster job descriptions.

Specifically, my model will focus on `topic modeling` techniques.

This will involve trying out TF-IDF, LDA, and finally, BERTopic to see what method is the most efficient, interpretable, and easier to deploy.


# Topic Modeling Overview
Topic modeling is a type of model used to `discover abstract topics within a collection of documents`, where a *topic* is a `collection of dominant, representative keywords`. 

This approach aims to uncover abstract topics, allowing for analysis of how these topics interact and intersect. 

For this project to be successful, the uncovered topics should be `clear, segregated, and meaningful.`

# Potential Issues
Topic modeling is a challenging task. It is difficult to evaluate the performance of the model, as the model operates under the `unsupervised learning` paradigm, lacking a ground truth to compare the performance of my model with. 

Thus, the model's success is largely dependent on the interpretability of its results.

However, that's not to say that there are no metrics to evaluate the performance of the different models employed. 

For instance, we will use the `Coherence Score` to evaluate the performance of the LDA model. The coherence score measures the degree of semantic similarity between high-scoring words in the topic. Higher coherence scores indicate better topics.

The `silhouette score` employed in the K-means model measures how similar an object is to its own cluster compared to other clusters. 
# Metrics
- K-means Silhouette Score - to evaluate the performance of the K-means clustering algorithm in the TF-IDF model
- Coherence Score - to evaluate the performance of the LDA model
- Interpretability - to evaluate the performance of the BERTopic model
<div class="alert"  style="background-color:#1f2e6b; color:white; padding:0px 5px; border-radius:10px;"><h2 style='margin:10px'>The Dataset</h2></div>

# Introduction to the dataset
Finally, we get to the data itself. 

The ideal version of my project would involve real time scraping of job descriptions from various platforms.

This first edition of this project will have a more limited scope. It will deal with job descriptions from a single platform, Upwork. More specifically, it will deal with job descriptions from Kaggle's dataset `Upwork freelance jobs (+60k)`, by user `Ahmed Myalo`. The dataset can be found [here](https://www.kaggle.com/ahmedmyalo/upwork-freelance-jobs-60k).

The dataset comprises 60,000 job descriptions from Upwork, spanning various categories. It contains 82 columns, for which I will only be using the Job Title, Job Description, and Category_1 (main category) columns. Out of these columns, any missing values will be dropped, since no meaningful imputation can be made for these columns.

# Quick EDA and Feature Reduction
The EDA focuses on maintaining only job titles, descriptions, the main job category, and dropping any NaN values.

You can find the EDA notebook [in the following link](./Sprint_3/EDA_NOTEBOOK.ipynb).

<div class="alert"  style="background-color:#1f2e6b; color:white; padding:0px 5px; border-radius:10px;"><h2 style='margin:10px'>Model Overview</h2></div>

# The models

Each link below will take you to the respective notebook for the model. Each notebook goes into more detail about how the model works, how it was implemented for my dataset, what results it produced, and how those results were evaluated.

1. [TF-IDF + KMeans](./TF_IDF.ipynb): This is a simple model which uses Term Frequency-Inverse Document Frequency (TF-IDF) to vectorize the job descriptions and KMeans to cluster them.
   
2. [LDA (Latent Dirichlet Allocation)](./LDA.ipynb): A more sophisticated approach that identifies topics based on word distributions within documents.

3. [BERTopic](./Sprint_3/BERT.ipynb): Utilizes BERT embeddings and does not require traditional preprocessing, leveraging the context of words to identify topics.

# Model Comparisons
<table>
    <tr>
        <th>Model Name</th>
        <th>TF-IDF</th>
        <th>LDA</th>
        <th>BERTopic</th>
    </tr>
    <tr>
        <td><strong>Approach</strong></td>
        <td>Calculates a term's importance in a document relative to its count across a collection of documents. These scores are then clustered via K-Means</td>
        <td>Assumes documents are mixtures of topics, and assigns the words inside the documents to topics based on their distribution.</td>
        <td>Utilizes a pipeline to reach state of the art results in topic modeling. This consists of preprocessing the text, generating embeddings, reducing dimensions, clustering, and visualization</td>
    </tr>
    <tr>
        <td><strong>Pros</strong></td>
        <td>Simpler model, less computationally demanding of all models</td>
        <td>Able to discover hidden topics, less computationally demanding than BERTopic</td>
        <td>Leads to most comprehensive results without manual text preprocessing</td>
    </tr>
    <tr>
        <td><strong>Cons</strong></td>
        <td>Ignores semantics and context</td>
        <td>Requires predefined number of topics, requires more parameter setting changes</td>
        <td>Computationally intensive, requires Google Colab on current setup. Could be unsistainable with larger datasets</td>
    </tr>
    <tr>
        <td><strong>Metrics</strong></td>
        <td>Often uses measures like Silhouette score for KMeans cluster</td>
        <td>Employs coherence scores to evaluate the quality of the topics produced, indicating how meaningful the topics are.</td>
        <td>Measure based on topic interpretability</td>
    </tr>
</table>

# Model of Choice and Rationale
Since the project aims to provide insights that are not only accurate but also interpretable so they can be easily understood and acted upon by freelancers, I believe BERTopic is the most suitable model.
<div class="alert"  style="background-color:#1f2e6b; color:white; padding:0px 5px; border-radius:10px;"><h2 style='margin:10px'>Next Steps</h2></div>

- Analyze how clusters evolve over time.
- Examine clusters by geography.
- Expand the analysis to other job platforms.
- Develop a GUI with Streamlit for interactive analysis.

<div class="alert"  style="background-color:#1f2e6b; color:white; padding:0px 5px; border-radius:10px;"><h2 style='margin:10px'>Closing thoughts</h2></div>
Overall, this project has been a great learning experience. While I can't claim to have a full understanding on the intricacies of NLP and topic modeling - Microsoft won't come knocking anytime soon - I have learned a lot, and I genuinely believe this project has the potential to be a valuable tool for freelancers, which makes it a worthwhile endeavor to continue working on.
