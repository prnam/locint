# Solution using Azure and its marketplace 

1. Develop locally timer funtions using Python & Azure Funtions Core Tools.
2. Push the code to GitHub and merge to main to trigger CI/CD pipeline.
3. CI/CD pipeline will fetch secrets using Azure Service Prinicpal and deploy Azure Funtions on Azure.
4. Once deployed the Azure funtion will run on scheduled timer and fetch data based on the code.
    - Code takes ApiId of OpenWeather API from Funtions app keys
    - Uses Open Weather API endpoint and business logic in the funtion to GET data, if pressure is predicted to fall below 995 Millibar during 6am to 6pm or not.
    - Inputs are on functions.json file.
5. Once API fetching is done it outputs the response through SendGrid bindings as email to recipients.
    - selected reponse and async/ await is part of code
    - email recipient can be on json file or as secrets based on security needs
---
### Extra Note: 
a] Timer based approach does not attempt retry (most often in N/W blips) so best we can do is monitor, hence we have Azure Monitor to log everything we need and improve further during any kind of failure.

b] Azure Policy used to make sure solution adheres policy of well-architecture proposed by Azure and Solution architect of the company, if not raise concerns for necessary stakeholders.

### What if customer is not on Cloud or do not want to use marketplace?

We can create same using .NET worker serivce (.NET 5 or .NET6) and use existing SMTP setup on prem ( may need network team to unblock port based VM security). This to has issue with retry. This can also done in Python but I recommend .NET 5 or 6.

### I am okay with timer retry issue, but how to overcome failure if VM goes down on prem setup?
We can convert worker serivce to container based solution easily and orachestrate using k8s(if there is approval to setup one)