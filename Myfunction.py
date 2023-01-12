import requests


class Api:

    #API_URL = 'http://127.0.0.1:8000/'
    API_URL = 'https://0a1d-2a01-cb19-6ec-1800-7d22-7438-f54e-64a4.eu.ngrok.io'

    def get_query():
        query = '?job_title=Data%20Scientist&company_size=Large&company_country_location=Germany&experience_level=Intermediate&employee_country_residence=Germany&remote_ratio=0'
        return query

    @classmethod
    def get_data(self):
        my_query = self.get_query()
        print(self.API_URL)
        print(my_query)
        res = requests.get(f"{self.API_URL}{my_query}").json()
        return res#['prediction du salaire en $']


    @classmethod
    def get_data2(self, job_title, company_size, company_country_location, experience_level, employee_country_residence, remote_ratio):
        query = f'?job_title={job_title}&company_size={company_size}&company_country_location={company_country_location}&experience_level={experience_level}&employee_country_residence={employee_country_residence}&remote_ratio={remote_ratio}'
        print(query)
        print(f"{self.API_URL}{query}")
        res = requests.get(f"{self.API_URL}{query}").json()
        return res['prediction du salaire en $']
