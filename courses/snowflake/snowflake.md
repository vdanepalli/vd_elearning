# [Snowflake](../../courses.md)

- [Snowflake](#snowflake)
  - [LinkedIn: End to End Real-World Data Engineering Project with Snowflake](#linkedin-end-to-end-real-world-data-engineering-project-with-snowflake)


## LinkedIn: End to End Real-World Data Engineering Project with Snowflake

- Data silos 
- 24 hour processing delays 
- Scalability issues
- Data quality inconsistencies
- Limited analytical capabilities


<br/><br/>

- Centralize Data
- Enable real-time analytics
- Improve scalability
- Enhance data quality
- Support advance analytics


<br/><br/>

- Customer Data: daily CSV 100,000 records/day
- Product Catalog: hourly JSON 10,000 changes/day
- Transaction logs: real-time Parquet files 500,000 transactions/day


<br/><br/>

- Reduce processing time - 24 hours to 1 hour
- 99.9% accuracy in cross-channel reporting
- Handle five times current data volume
- Enable self-service analytics


<br/><br/>

- Multilayer Snowflake Architecture
  - Bronze Layer: Raw data ingestion
  - Silver Layer: Cleaned and Conformed data
  - Gold layer: Business-level aggregates

<br/><br/>

- Overall Architecture
- Data Sources
  - Customer Relationship Management (CRM)
  - Inventory management system
  - Ecommerce platform
- Azure Data Lake Storage (ADLS)
  - Centralized data lake
  - Scalable and cost effective
  - Support various data formats
  - Staging area for Snowflake
- Snowflake Data Warehouse
  - Core of the Solution
  - Connects to ADLS via external stages
  - Ingest data using COPY Commands
  - Process and Transform data
  - Multilayer data storage
  - Computation resources for analytics  
- Data Processing Layers
  - Bronze: Raw data
  - Silver: Cleaned and Conformed data -- Incremental merge logic
  - Gold: Business-level aggregates
- Reporting and Analytical Tools


<br/><br/>

- Data Flow
- Source Systems -> ADLS -> Bronze Layer (COPY Commands in Snowflake Tasks)
- Bronze -> Silver (another task - transformations and quality rules)
- Silver -> Gold 
- Gold -> BI Tools (reporting and analytics)

- One database (three different schemas, one for each Bronze, Silver, Gold)

<br/><br/>

- Key Snowflake Features
  - External Stages - (connect ADLS to Snowflake)
  - COPY Command (Snowflake feature)
  - Tasks (automate data loading and processing workflows)
  - Streams (capture and process incremental changes)
  - Time travel (data recovery and historical analysis)
  - Zero-copy cloning (environment provisioning for dev, test, prod)
- Benefits
  - Scalability
  - Flexibility - diff sources
  - Performances - separation of storage and computer, improve query efficiency 
  - Cost Efficiency
  - Data Governance


<br/><br/>

- Key Components
  - Snowflake DB
  - External Stage
  - Multiple Schema
  - Tables
  - Task
  - Streams (incremental data from bronze to silver)
  - Views
