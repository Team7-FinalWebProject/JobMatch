# Job Utopia

Work in progress

## Run Locally

Currently the recommended way to setup locally is via Docker

Install and run Docker

Clone the project

```bash
git clone https://github.com/Team7-FinalWebProject/JobMatch
```
Go to the project directory
```bash
cd JobMatch
```

Register and setup accounts at OpenAPI and Mailjet.
Save the API keys and prepare other details to fill in

 - Mailjet sender e-mail, API_secret
 - user password for the jobmatch admin and initial users
 - db password (same password in several files)
 - JWT_Secret for login security

Fill the details in the template configuration files identified with ".sample" extension and rename the files.
```bash
Windows: rename file.extension.sample file.extension
Linux: mv file.extension.sample file.extension
```
Start the containers (with Docker compose)
```bash
docker-compose up -d --build
```

## Hosting:

Project is currently hosted here:
[Fronted -> Vercel](https://jobutopia.vercel.app/)
[Backend -> Heroku (Swagger API docs)](https://jobutopia-82f9ec412313.herokuapp.com/docs)
[DB -> Supabase (private)](https://supabase.com/)


## Database:
PostgreSQL

```mermaid
erDiagram

WEB_FILTERS }o--||  USERS  : user_id
PROFESSIONAL_OFFERS }o--|| PROFESSIONALS  : id
REQUESTS }o--|| PROFESSIONAL_OFFERS : id
USERS ||--|| PROFESSIONALS : user_id
USERS ||--|| COMPANIES : user_id
COMPANY_OFFERS }o--|| COMPANIES  : id
REQUESTS }o--||  COMPANY_OFFERS : id
MESSAGES  }o--||  USERS  : sender
MESSAGES  }o--||  USERS  : receiver
CONFIG {
bool static_skills
int min_level
int max_level
jsonb baseline_skills
jsonb pending_approval_skills
jsonb approved_skills
}
COMPANIES{
varchar address
bool approved
text description
int id
varchar name
int user_id
}
COMPANY_OFFERS{
int  chosen_professional_offer_id
int company_id
int id
int max_salary
int min_salary
jsonb  requirements
varchar status
}
MESSAGES{
text content
int id
varchar receiver_username
varchar sender_username
 }
 PROFESSIONAL_OFFERS{
int chosen_company_offer_id
text description
int id
int max_salary
int min_salary
int professional_id
 jsonb skills
varchar status
}
PROFESSIONALS{
varchar address
bool approved
int default_offer_id
varchar first_name
int id
varchar last_name
varchar status
 text summary
 int user_id
}
REQUESTS{
int company_offer_id
int id
int professional_offer_id
varchar request_from
 }
 USERS{
bool admin
int id
bytea password
varchar username
 }
 
WEB_FILTERS{
jsonb filter
int id
int user_id
}
```


> Written with [StackEdit](https://stackedit.io/).