#! /usr/bin/env python
import psycopg2

query1 = (
    "select articles.title, count(log.path) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%')"
    "where status = '200 OK' group by "
    "articles.title, log.path order by views desc limit 3"
    )


query2 = (
    "select authors.name, articleViews.views from authors "
    "join articleViews on authors.id = articleViews.author "
    "order by views desc;"
    )


query3 = (
    "select dailyErrors.date, "
    "round(100.0*dailyErrors.errors/dailyRequests.requests,2) "
    "as percentErrors from dailyErrors, dailyRequests where "
    "dailyErrors.date=dailyRequests.date order by percentErrors "
    "desc limit 1;"
    )


def connect(database_name="news"):
    """connect to database"""
    try:   
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Database does not exist")

def getQueryResults(query):
    """Return query results for given query"""
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def printQueryResults(query_results):
    """prints results for first two queries"""
    for results in query_results:
        print(results[0], " - ", results[1], "views")


def printErrorResults(query_results):
    """prints results for error query"""
    for results in query_results:
        print(results[0], results[1], "% errors")

"""run queries and save reults"""
popularArticlesResults = getQueryResults(query1)
popularAuthorsResults = getQueryResults(query2)
loadErrorDays = getQueryResults(query3)


"""print query results"""
print("Top three articles by view count")
printQueryResults(popularArticlesResults)
print("Most popular Authors by view count")
printQueryResults(popularAuthorsResults)
print("Days with more than 1% errors")
printErrorResults(loadErrorDays)
