# import pandas as pd
# import requests

# # Twój klucz API
# api_key = 'AIzaSyAT6xnSxPZplkntp4mJ6J85Ght2dNL7Cfc'

# # Parametry zapytania (lokalizacja, typ miejsca, promień itp.)
# locations_coords = {
#     'Warszawa_1': '52.23826076856302, 21.0143568111989',
#     'Wrocław_1': '51.11382193775396, 17.0504448170807',
#     'Kraków_1': '50.052966874438944, 19.930917730622067',
#     'Poznań_1': '52.4180113885816, 16.930477109251644',
#     'Gdańsk_1': '54.35819539008235, 18.6387006461402',
#     'Łódź_1': '51.75447593812657, 19.452593618100373',
#     'Katowice_1': '50.24951373713728, 19.016395412089288',
#     'Lublin_1': '51.25270823532197, 22.57774918110887',
#     'Bydgoszcz_1': '53.12806279543401, 18.01066256884164',
#     'Szczecin_1': '53.42451829070773, 14.53954083535824',
#     'Białystok_1': '53.1325, 23.1688',
#     'Rzeszów_1': '50.0413, 21.999',
#     'Torun': '53.0138, 18.5984',
#     'Częstochowa': '50.8113, 19.1203',
#     'Zamość': '50.7214, 23.2515',
#     'Gdynia': '54.5189, 18.5305',
#     'Zielona Góra': '51.9356, 15.5062',
#     'Gorzów Wielkopolski': '52.7325, 15.2384',
#     'Olsztyn': '53.7784, 20.4801',
#     'Zakopane': '49.2992, 19.9496',
#     'Płock': '52.5463, 19.7065',
#     'Opole': '50.6751, 17.9213',
#     'Radom': '51.4024, 21.1471',
#     'Kielce': '50.8661, 20.6286',
#     'Inowrocław': '52.7983, 18.2635',
#     'Elbląg': '54.1522, 19.4088',
#     'Grudziądz': '53.485, 18.7534',
#     'Piła': '53.1504, 16.7384',
#     'Gniezno': '52.5347, 17.5823',
#     'Sandomierz': '50.6826, 21.7491',
#     'Kazimierz Dolny': '51.3246, 21.9515',
#     'Tarnów': '50.0124, 20.9889'
# }


# radius = 10000
# place_type = 'restaurant'

# unique_places_headers = [
#     'place_id',
#     'name',
#     'opening_hours.weekday_text',
#     'permanently_closed',
#     'adr_address',
#     'url',
#     'geometry.location.lng',
#     'geometry.location.lat',
#     'plus_code.global_code',
#     'formatted_address',
#     'rating',
#     'wheelchair_accessible',
#     'user_ratings_total',
#     'price_level',
#     'address_components',
#     'vicinity',
#     'plus_code.compound_code',
#     'scope',
#     'website',
#     'business_status',
#     'types']

# review_headers = [
#     'place_id',
#     'author_name',
#     'language',
#     'original_language',
#     'rating',
#     'relative_time_description',
#     'text',
#     'time',
#     'translated'
# ]

# places_csv_file_path = 'raw_data/places.csv'

# try:
#     places_df = pd.read_csv(places_csv_file_path)
# except:
#     places_df = pd.DataFrame(columns=unique_places_headers)

# review_csv_file_path = 'raw_data/reviews_1.csv'
# try:
#     review_df = pd.read_csv(review_csv_file_path)
# except:
#     review_df = pd.DataFrame(columns=review_headers)

# for city in locations_coords:
#     url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={locations_coords[city]}&radius={radius}&type=restaurant&keyword=cuisine&key={api_key}"
#     response = requests.get(url)
#     places = response.json()
#     # # Wyświetlenie wyników
#     if 'results' in places:
#         for place in places['results']:
#             place_id = place.get('place_id', 'Brak id')
#             details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
#             details_response = requests.get(details_url)
#             place_details = details_response.json()
#             if 'result' in place_details and 'reviews' in place_details['result']:
#                 for review in place_details['result']['reviews']:
#                     unique_places_record = [place.get(header, None) for header in unique_places_headers]
#                     places_df.loc[len(places_df)] = unique_places_record
#                     places_df.to_csv(places_csv_file_path, index=False)
#                     review_record = [place.get('place_id', None),
#                                      review.get('author_name', None),
#                                      review.get('language', None),
#                                      review.get('original_language', None),
#                                      review.get('rating', None),
#                                      review.get('relative_time_description', None),
#                                      review.get('text', None),
#                                      review.get('time', None),
#                                      review.get('translated', None)
#                                      ]
#                     review_df.loc[len(review_df)] = review_record
#                     review_df.to_csv(review_csv_file_path, index=False)
# print('done')

import pandas as pd
import requests
import time

# API Key
api_key = 'AIzaSyAT6xnSxPZplkntp4mJ6J85Ght2dNL7Cfc'

locations_coords = {
    'Warszawa_1': '52.23826076856302, 21.0143568111989',
    'Wrocław_1': '51.11382193775396, 17.0504448170807',
    'Kraków_1': '50.052966874438944, 19.930917730622067',
    'Poznań_1': '52.4180113885816, 16.930477109251644',
    'Gdańsk_1': '54.35819539008235, 18.6387006461402',
    'Łódź_1': '51.75447593812657, 19.452593618100373',
    'Katowice_1': '50.24951373713728, 19.016395412089288',
    'Lublin_1': '51.25270823532197, 22.57774918110887',
    'Bydgoszcz_1': '53.12806279543401, 18.01066256884164',
    'Szczecin_1': '53.42451829070773, 14.53954083535824',
    'Białystok_1': '53.1325, 23.1688',
    'Rzeszów_1': '50.0413, 21.999',
    'Torun': '53.0138, 18.5984',
    'Częstochowa': '50.8113, 19.1203',
    'Zamość': '50.7214, 23.2515',
    'Gdynia': '54.5189, 18.5305',
    'Zielona Góra': '51.9356, 15.5062',
    'Gorzów Wielkopolski': '52.7325, 15.2384',
    'Olsztyn': '53.7784, 20.4801',
    'Zakopane': '49.2992, 19.9496',
    'Płock': '52.5463, 19.7065',
    'Opole': '50.6751, 17.9213',
    'Radom': '51.4024, 21.1471',
    'Kielce': '50.8661, 20.6286',
    'Inowrocław': '52.7983, 18.2635',
    'Elbląg': '54.1522, 19.4088',
    'Grudziądz': '53.485, 18.7534',
    'Piła': '53.1504, 16.7384',
    'Gniezno': '52.5347, 17.5823',
    'Sandomierz': '50.6826, 21.7491',
    'Kazimierz Dolny': '51.3246, 21.9515',
    'Tarnów': '50.0124, 20.9889'
}

radius = 10000
place_type = 'restaurant'

# Column headers
unique_places_headers = [
    'place_id', 'name', 'opening_hours.weekday_text', 'permanently_closed',
    'adr_address', 'url', 'geometry.location.lng', 'geometry.location.lat',
    'plus_code.global_code', 'formatted_address', 'rating', 'wheelchair_accessible',
    'user_ratings_total', 'price_level', 'address_components', 'vicinity',
    'plus_code.compound_code', 'scope', 'website', 'business_status', 'types'
]

review_headers = [
    'place_id', 'author_name', 'language', 'original_language', 'rating',
    'relative_time_description', 'text', 'time', 'translated'
]

# CSV file paths
places_csv_file_path = 'raw_data/places.csv'
review_csv_file_path = 'raw_data/reviews_1.csv'

# Load or create DataFrames
places_df = pd.read_csv(places_csv_file_path) if pd.io.common.file_exists(places_csv_file_path) else pd.DataFrame(columns=unique_places_headers)
review_df = pd.read_csv(review_csv_file_path) if pd.io.common.file_exists(review_csv_file_path) else pd.DataFrame(columns=review_headers)

for city in locations_coords:
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={locations_coords[city]}&radius={radius}&type=restaurant&keyword=cuisine&key={api_key}"
    response = requests.get(url)
    places = response.json()

    # Process each place
    if 'results' in places:
        for place in places['results']:
            place_id = place.get('place_id')
            if place_id and place_id not in places_df['place_id'].values:
                # Place Details
                details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
                details_response = requests.get(details_url)
                place_details = details_response.json()

                if 'result' in place_details:
                    unique_places_record = [place_details['result'].get(header, None) for header in unique_places_headers]
                    places_df.loc[len(places_df)] = unique_places_record

                    # Process reviews if they exist
                    if 'reviews' in place_details['result']:
                        for review in place_details['result']['reviews']:
                            review_record = [
                                place_id,
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

    # Optional delay to prevent hitting rate limits
    time.sleep(1)

# Save DataFrames to CSVs
places_df.to_csv(places_csv_file_path, index=False)
review_df.to_csv(review_csv_file_path, index=False)

print('Done')
