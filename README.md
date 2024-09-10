# Django training project
Fitness project based on Django

## Table of Contents

## Features

- Create new student / trainer
- Create exercises, training plan
- Create prope nutrition, supplements
- Storage data in a PostgreSQL database

## Installation

1. Clone the repository:

    ```sh
    git clone 
    cd DjangoProject
    ```

2. Create virtual environment
    ```sh
    python -m venv venv
    ```

3. Activate virtual environment
    
    On MacOS or Linux:
    ```sh
    source venv/bin/activate
    ```
   
    On Windows:
    
    ```sh
    venv\Scripts\activate
    ```
    
4. Install dependencies from requirements.txt:

    ```sh
    pip install -r requirements.txt
    ```
   
## Configuration

1. Copy the `.env.example` file to `.env`:

    ```sh
    cp .env.example .env
    ```