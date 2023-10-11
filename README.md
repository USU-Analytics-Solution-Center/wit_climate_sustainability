![Logo](ASC.png)



# Women in Data DATATHON 2023

- **Theme:** Climate sustainability
- **Prompt:** Investments in climate services and early warning systems (USU-DAIS-WIT)

## Task

Assess the climate finance flows dedicated to climate services and early warning projects. There's a need to analyze adaptation-related projects financed by various major climate change funding sources.

This competition in 2023 saw participation from our students in Women in Tech from the Department of Data Analytics and Information Systems (DAIS) at Utah State University, Huntsman School of Business. This project is mentored by the Analytics Solution Center (ASC).

## Team Members (Alphabetical Order)

- [Adelaide Berry](https://www.linkedin.com/in/adelaideberry/)
- [Chloe Clemens](https://www.linkedin.com/in/chloe-clemens/)
- [Brooke Monson](https://www.linkedin.com/in/brooke-monson-484527122/)
- [Hannah Whiting](https://www.linkedin.com/in/hannah-whiting-/)
- [Morgan Phillips](https://www.linkedin.com/in/morganphillips-/)

## Project Journey

Our quest began with an extensive review of 16 provided websites to identify relevant climate services and early warning systems projects. Initially, a manual analysis was performed on selected projects from each site, which laid a solid foundation for the subsequent automation phase. We chose a complex, dynamic website and employed Selenium for web scraping, which proved to be a robust proof of concept.

With the acquired data, a detailed database was constructed, encapsulating vital project information and descriptions. In parallel, a list of project components was furnished, outlining the core elements of climate service and early warning systems projects.

The challenge then was to map these components with the projects in our database. While exact keyword matching was the initial directive, the subjective nature of components nudged us towards a more advanced text-matching technique. Utilizing transformer models like BERT, we encoded the text to compare context-aware representations of components and project information. This approach yielded 12 distinct component scores per project.

These scores were normalized and employed as weights to discern the financial flow associated with each component and project. The finale of our journey was encapsulated in a comprehensive Tableau dashboard, offering a user-friendly interface to interact with and analyze our findings. This journey not only enhanced our technical skills but also fostered a collaborative spirit amongst team members, illuminating the path of climate sustainability through data-driven insights.


## Visualization Dashboard 
All the code is available in this repository. Check out our [Visualization Dashboard](https://public.tableau.com/shared/YNFS44TNG?:display_count=n&:origin=viz_share_link) for a user-friendly interface showcasing our findings! 

## License

This project is licensed under the BSD 3-Clause License.

