import justpy as jp 
import pandas
import matplotlib.pyplot as plt 
from datetime import datetime

data = pandas.read_csv('/Users/ruslansamatov/Projects/PythonBegining-/Python_data_analytics/movies.csv')


 #Filtering based on a specific condition

comedy_movies = data[data.loc[:,'Genre'] == "Comedy"]

print("Movies Comedy:\n", comedy_movies)

 

average_rating_For_Comedy_Movie = comedy_movies['Rotten Tomatoes %'].mean()

print(average_rating_For_Comedy_Movie)

 

Action_movies = data[data.loc[:,'Genre'] == "Action"]

print("Movies Action:\n", Action_movies)

 

average_rating_For_Action_Movie = Action_movies['Rotten Tomatoes %'].mean()

print(average_rating_For_Action_Movie)

 

Romance_movies = data[data.loc[:,'Genre'] == "Romance"]

print("Movies Romance:\n", Romance_movies)

 

average_rating_For_Romance_Movie = Romance_movies['Rotten Tomatoes %'].mean()

print(average_rating_For_Romance_Movie)

 

Romance_movies = data[data.loc[:,'Genre'] == "Romance"]

print("Movies Romance:\n", Romance_movies)

 

average_rating_For_Romance_Movie = Romance_movies['Rotten Tomatoes %'].mean()

print(average_rating_For_Romance_Movie)

 

Animation_movies = data[data.loc[:,'Genre'] == "Animation"]

print("Movies Animation:\n", Animation_movies)

 

average_rating_For_Animation_Movie = Animation_movies['Rotten Tomatoes %'].mean()

print(average_rating_For_Animation_Movie)

 

Drama_movies = data[data.loc[:,'Genre'] == "Drama"]

print("Movies Drama:\n", Drama_movies)

 

average_rating_For_Drama_Movie = Drama_movies['Rotten Tomatoes %'].mean()

print(average_rating_For_Drama_Movie)



chart_js= """ {
 chart: {
        type: 'pie'
    },
    title: {
        text: 'Start based on rotten tomatoes rating'
    },
    tooltip: {
        valueSuffix: '%'
    },
    subtitle: {
        text:
        'Source:<a href="https://www.mdpi.com/2072-6643/11/3/684/htm" target="_default">MDPI</a>'
    },
    plotOptions: {
        series: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}%',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'percentage',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Percentage',
            colorByPoint: true,
            data: [
                {
                    name: 'Comedy',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Most Popular genre from 2008-2024",classes="text-h2 text-center")
    hc_pie = jp.HighCharts(a=wp,options= chart_js)
    hc_pie.options.series[0].data[0].y = round(average_rating_For_Comedy_Movie,2)
    hc_pie.options.series[0].data[1].name = 'Action'
    hc_pie.options.series[0].data[1].y=round(average_rating_For_Action_Movie,2)
    hc_pie.options.series[0].data[0].name = "Comedy"

    hc_pie.options.series[0].data[0].y= average_rating_For_Comedy_Movie

    hc_pie.options.series[0].data[1].y= average_rating_For_Action_Movie

    hc_pie.options.series[0].data[2].y= average_rating_For_Drama_Movie

    hc_pie.options.series[0].data[3].y= average_rating_For_Animation_Movie
    return wp

jp.justpy(app)