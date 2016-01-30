# django-haystack-note
Using Elasticsearch for implement search functionality in Django Website

### Requirements
- Python==2.7
- Django==1.8
- Elasticsearch==2.1.0 (this is different than the elasticsearch package in _requirements.txt_)

*debug_toolbar* was optionally added in this example; but it is not mandatory.

### Points to note
- Signal processing is used in this example; after every change in the model, the elasticsearch index is automatically updated. 
- **python manage.py update_index** to manually update the index

### Open Issues

- The **Previous** and **Next** links to retrieve prior/latter search results is not working because *has_previous* is always returning FALSE. (see _templates/search/search.html_)
- **_http://127.0.0.1:8000/search_** works as expected; while *http://127.0.0.1:8000* doesnt work - this is based on the *django-haystack-example* (see Reference).


### Reference
- [Haystack Tutorial] (http://django-haystack.readthedocs.org/en/v2.4.1/tutorial.html#installation) 
- [django-haystack-example](http://nanvel.name/2013/07/django-haystack-example) (after working through this realized that it is outdated and shouldnt have referred it :( )
