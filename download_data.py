import pandas as pd
import requests

# Twój klucz API
api_key = ''

# Parametry zapytania (lokalizacja, typ miejsca, promień itp.)
locations_coords = {'Warszawa_1': '52.23826076856302, 21.0143568111989',
                    'Warszawa_2': '52.21734461858539, 21.013517276066736',
                    'Warszawa_3': '52.23596290735246, 21.024858738112805',
                    'Warszawa_4': '52.21719732052002, 21.01937501442012',
                    'Warszawa_5': '52.238435912885, 21.001034851289983',
                    'Warszawa_6': '52.22246037721922, 21.011685738326733',
                    'Warszawa_7': '52.22233682564661, 20.99897719370571',
                    'Warszawa_8': '52.21981725219317, 20.99947853403626',
                    'Warszawa_9': '52.22035436159655, 21.021098480767638',
                    'Warszawa_10': '52.24066463598689, 21.012877915343747',
                    'Wrocław_1': '51.11382193775396, 17.0504448170807',
                    'Wrocław_2': '51.096475891662415, 17.045078709695936',
                    'Wrocław_3': '51.09890809477713, 17.03169394628345',
                    'Wrocław_4': '51.106335786097496, 17.0406583892598',
                    'Wrocław_5': '51.10161358620371, 17.042996094444025',
                    'Kraków_1': '50.052966874438944, 19.930917730622067',
                    'Kraków_2': '50.06956384852997, 19.944632544225527',
                    'Kraków_3': '50.052607883866294, 19.947184511356923',
                    'Kraków_4': '50.05877469380732, 19.93751687740881',
                    'Kraków_5': '50.07039598634938, 19.94821314517603',
                    'Poznań_1': '52.4180113885816, 16.930477109251644',
                    'Poznań_2': '52.41281255307241, 16.922174544941686',
                    'Poznań_3': '52.407679380866426, 16.91680917672723',
                    'Poznań_4': '52.39758482997274, 16.922172472509907',
                    'Poznań_5': '52.39730926307092, 16.91983774735165',
                    'Gdańsk_1': '54.35819539008235, 18.6387006461402',
                    'Gdańsk_2': '54.358746643515914, 18.645336540935496',
                    'Gdańsk_3': '54.359763850036074, 18.653133457002067',
                    'Gdańsk_4': '54.349254236002345, 18.63720497548465',
                    'Gdańsk_5': '54.34298622025309, 18.651744330903878',
                    'Łódź_1': '51.75447593812657, 19.452593618100373',
                    'Łódź_2': '51.76096992626223, 19.447499081580812',
                    'Łódź_3': '51.761278398592296, 19.462365479366657',
                    'Łódź_4': '51.7607198927213, 19.46613599105772',
                    'Łódź_5': '51.7669986349209, 19.45802051015485',
                    'Katowice_1': '50.24951373713728, 19.016395412089288',
                    'Katowice_2': '50.25178711554309, 19.031702836072817',
                    'Katowice_3': '50.26901247291018, 19.008497633225947',
                    'Katowice_4': '50.252986449330166, 19.034716690387118',
                    'Katowice_5': '50.25475619505899, 19.015582069781473',
                    'Katowice_6': '50.26355075993786, 19.026860475860214',
                    'Katowice_7': '50.27229489557349, 19.02486686690035',
                    'Katowice_8': '50.25269386662713, 19.02538990147203',
                    'Katowice_9': '50.26208349131675, 19.018737676891114',
                    'Katowice_10': '50.25236567174837, 19.025994420128544',
                    'Lublin_1': '51.25270823532197, 22.57774918110887',
                    'Lublin_2': '51.25271702324647, 22.562292570130527',
                    'Bydgoszcz_1': '53.12806279543401, 18.01066256884164',
                    'Bydgoszcz_2': '53.11456929779187, 18.019608410411333',
                    'Szczecin_1': '53.42451829070773, 14.53954083535824',
                    'Szczecin_2': '53.42953210442023, 14.553362939100966',
                    'Białystok_1': '53.135802446960305, 23.171314319188074',
                    'Białystok_2': '53.12815081119562, 23.163699924153416',
                    'Rzeszów_1': '50.048395184185644, 21.993894517172883',
                    'Rzeszów_2': '50.03098099174974, 22.002100071537015'}

radius = 2000
place_type = 'restaurant'

unique_places_headers = [
    'place_id',
    'name',
    'opening_hours.weekday_text',
    'permanently_closed',
    'adr_address',
    'url',
    'geometry.location.lng',
    'geometry.location.lat',
    'plus_code.global_code',
    'formatted_address',
    'rating',
    'wheelchair_accessible',
    'user_ratings_total',
    'price_level',
    'address_components',
    'vicinity',
    'plus_code.compound_code',
    'scope',
    'website',
    'business_status',
    'types']

review_headers = [
    'place_id',
    'author_name',
    'language',
    'original_language',
    'rating',
    'relative_time_description',
    'text',
    'time',
    'translated'
]

places_csv_file_path = 'raw_data/places.csv'

try:
    places_df = pd.read_csv(places_csv_file_path)
except:
    places_df = pd.DataFrame(columns=unique_places_headers)

print(places_df)
review_csv_file_path = 'raw_data/reviews.csv'
try:
    review_df = pd.read_csv(review_csv_file_path)
except:
    review_df = pd.DataFrame(columns=review_headers)

for city in locations_coords:
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={locations_coords[city]}&radius={radius}&type={place_type}&key={api_key}"
    response = requests.get(url)
    places = response.json()
    # # Wyświetlenie wyników
    if 'results' in places:
        for place in places['results']:
            place_id = place.get('place_id', 'Brak id')
            details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
            details_response = requests.get(details_url)
            place_details = details_response.json()
            if 'result' in place_details and 'reviews' in place_details['result']:
                for review in place_details['result']['reviews']:
                    unique_places_record = [place.get(header, None) for header in unique_places_headers]
                    places_df.loc[len(places_df)] = unique_places_record
                    places_df.to_csv(places_csv_file_path, index=False)
                    review_record = [place.get('place_id', None),
                                     review.get('author_name', None),
                                     review.get('language', None),
                                     review.get('original_language', None),
                                     review.get('rating', None),
                                     review.get('relative_time_description', None),
                                     review.get('text', None),
                                     review.get('time', None),
                                     review.get('translated', None)
                                     ]
                    review_df.loc[len(review_df)] = review_record
                    review_df.to_csv(review_csv_file_path, index=False)
