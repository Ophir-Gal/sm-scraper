# _sm-scraper_
Social Media Scraper (CMSC828D Final Project)

## Description

This final project idea is a collaboration with the Full Disclosure Project,
through the National Association of Criminal Defense Lawyers. The goal was to
develop a background process for continually scraping the web for relevant
posts to social media sites, such as Twitter, Facebook, Instagram, Reddit,
etc.. The targets of the scraping process are social media posts that mention
potential misconduct by police officers in specific Jurisdictions. The
deliverables for the project are: a) a public GitHub repository with clear and
detailed instructions on how to setup and execute the scraper; b) a starting
collection of social media posts produced by the scraper as an example dataset,
with an explicit schema describing the structure of the scraped data; c) a
separate script to extract relevant information uncovered by the scraper within
each social media post; and d) ideally a prototype interface to visualize the
extracted results.

## How to Use `sm-scraper`

We designed `sm-scraper` in a modular fashion, so that the user could decide
how to extend each module and keep things self-contained. There are
four different modules: `db` (stands for database), `scraper`, `dashboard`, and
`nlp` (stands for natural language processing).
Each module has its own dependencies which are listed in a separate
Dockerfile associated with that module. The `scraper` relies on the `nlp` and
`db` modules, and so does the `dashboard` (relies on `nlp` and `db`). The
dashboard module is an optional module which serves a website on
http://localhost:5000/ for exploring statistics, visualizations, and content of
the scraped posts.

The recommended order for running the modules is as follows:
1. `db`
2. `nlp` 
3. `scraper` (continuous scraping module)
4. `dashboard` (optional, for browsing and visualizing posts)

We recommend that you run the modules inside Docker containers, since that's
what we designed them for, but you can also run things locally if you have the
right dependencies.

### How to run modules with Docker and `make`

- Available modules: `db`, `scraper`, `dashboard`, and `nlp`.
- Supported Operation Systems: `windows`, `mac`, and `linux`.
- Change `env/machine_config.bashrc` w/ PROJECT_DN; absolute path to `sm-scraper`.
- To run the project, if you're using a non-linux machine, you need to first
  run `make add_smscraper_net_<your host OS>`, e.g. for mac run `make add_smscraper_net_mac`.
- Then, to run individual containers run `make <desired module>_<your host OS>`; 
  this automatically builds and runs the container, e.g. to run the `db`
  container on a mac run `make db_mac`.

### How to run modules locally (without Docker)

-- Yiheng needs to fill this out.

