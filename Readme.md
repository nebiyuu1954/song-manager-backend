# Song Manager Backend

A Django REST Framework API for managing songs, supporting CRUD operations, pagination, search, and sort, integrated with the Song Manager frontend.

## Prerequisites

Python (3.8+)

pip

Virtual environment (recommended)

## Installation


```bash

git clone git@github.com:nebiyuu1954/song-manager-backend.git
cd song-manager-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate

```



## Adding Data

Using Python Shell


```bash
python manage.py shell
```

In the shell:


```bash
exec(open('songBackend/seed.py').read())
```

- all the sample songs inside the seed.py will be added to the database


## Running Locally

```bash
python manage.py runserver
```

- Access API at http://localhost:8000/api/songs/.



## Features

- CRUD: Create, read, update, delete songs.
- Pagination: 7 songs per page (?page=, ?perpage=).
- Search: Filter by title, artist, album (?search=query).
- Sort: Title ascending (?ordering=title) or descending (?ordering=-title).
- Model: Song (id, title, artist, album, year, stream).



## API Endpoints

#### Get all items

```http
GET /api/songs/: List songs (?search=, ?ordering=, ?page=, ?perpage=).
```

#### Post an item

``` http
POST /api/songs/: Create song (e.g., { "title": "Song", "artist": "Artist", "album": "Album", "year": 2020, "stream": 1000000 }).
```


#### Get an item

``` http
GET /api/songs/:id/: Retrieve song.
```


#### Update an item

``` http
PUT /PATCH /api/songs/:id/: Update song.
```

#### Delete an item

``` http
DELETE /api/songs/:id/: Delete song.

```


## AI Usage

Used AI (Grok) to:

- Debug CORS



## Dependencies

- django, djangorestframework, django-cors-headers