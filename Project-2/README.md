# Project 2. HeadHunter Job Analysis Goals

The goal of the project is to create a tool that helps users and analysts study the labor market based on parameters such as in-demand skills, work experience, salary expectations, and the geography of job openings.

### Tasks

- Analyze the structure of the labor market
  - Assess the ratio of job vacancies to employers (identify if there is a concentration of vacancies with certain employers)
  - Explore regional coverage and industries served by employers

- Analyze the geography of job openings
  - Identify major megacities and economically developed cities by the number of vacancies
  - Evaluate how geography affects the distribution of jobs

- Analyze salary expectations
  - Study how transparent the labor market is, based on salary data
  - Compare average salaries with data from the largest cities in Russia

- Analyze work conditions
  - Investigate preferences for working hours (full-time, part-time)
  - Analyze vacancy profiles based on the experience level of professionals

- Study employer activity
  - Find leading companies by the number of vacancies (for example, Yandex, Gazprom Neft)
  - Analyze the scale of activity of employers across regions

- Data quality and completeness
  - Evaluate how fully employers fill out their industry categories
  - Identify multinational companies with a wide range of vacancies

- Analyze the IT and Data Science markets
  - Assess demand for IT specialists and Data Science professionals
  - Analyze skill requirements (Python, SQL, etc.)
  - Understand entry levels for positions (beginners vs experienced specialists)
  - Compare average salaries in IT/Data Science with overall market salaries

### Summary of work stages

1. Data collection
   - Downloading job vacancies and employer data from platforms like HeadHunter
   - Gathering information on regions, industries, salaries, and requirements

2. Data preprocessing
   - Cleaning data from missing values and errors
   - Standardizing salary ranges and skill descriptions
   - Creating useful aggregated tables and dashboards

3. Data analysis
   - Generating statistical summaries of vacancies, employers, regions, and experience levels
   - Analyzing salary distributions and work conditions
   - Finding patterns and identifying leading companies and regions

4. Visualization and reporting
   - Building charts and dashboards for key metrics
   - Presenting information in a user-friendly format for users and managers

### Tools used

- Python with libraries:
  - pandas for data processing and analysis
  - matplotlib for visualization

- SQL:
  - PostgreSQL for storing, managing, and analyzing large and complex datasets in various sectors

- Jupyter Notebook:
  - An environment for developing and documenting code, running code blocks, and conducting interactive data analysis

### Conclusions

After completing all stages and building the model, we can expect:

- High concentration of vacancies among certain employers. The number of vacancies is more than twice the number of employers, indicating many companies post several vacancies simultaneously.
- Presence of large, multinational companies across multiple industries. Some employers operate in many regions and sectors—up to 181 regions for one employer.
- The geography of the labor market is concentrated in megacities and developed regional centers, reflecting high economic activity in these areas.
- The transparency of the labor market is increasing, as many vacancies include salary expectations, helping job seekers navigate the market better.
- The average salaries range from 70,000 to 100,000 rubles or more, aligning with market expectations in major Russian cities.
- The IT and Data Science sectors remain highly demanded, with high competition and salaries, though entry to these fields can be challenging for beginners.
- The job market is filled with vacancies for professionals with 1–6 years of experience, while opportunities for beginners and very experienced specialists are less developed.
