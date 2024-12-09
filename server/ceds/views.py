from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ServicesMockListView(APIView):
    def mock_data(self):
        data = {
            "success": True,
            "code": 200,
            "message": "Service list retrieved successfully.",
            "data": [
                {
                    "id": 1,
                    "title": "Respond",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 2,
                    "title": "Notice",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 3,
                    "title": "Problems",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 4,
                    "title": "Tax",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 5,
                    "title": "Birth Certificate Registration",
                    "link": "https://bdris.gov.bd/br/application"
                },
                {
                    "id": 6,
                    "title": "Birth Certificate Correction",
                    "link": "https://bdris.gov.bd/br/application"
                },
                {
                    "id": 7,
                    "title": "Death Certificate Registration",
                    "link": "https://bdris.gov.bd/br/application"
                },
                {
                    "id": 8,
                    "title": "Married Certificate Correction",
                    "link": "https://bdris.gov.bd/br/application"
                },
                {
                    "id": 9,
                    "title": "Respond",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 10,
                    "title": "Notice",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 11,
                    "title": "Problems",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 12,
                    "title": "Tax",
                    "link": "https://cdn-icons-png.flaticon.com/128/4707/4707622.png"
                },
                {
                    "id": 13,
                    "title": "Birth Certificate Registration",
                    "link": "https://bdris.gov.bd/br/application"
                },
                {
                    "id": 14,
                    "title": "Birth Certificate Correction",
                    "link": "https://bdris.gov.bd/br/application"
                },
                {
                    "id": 15,
                    "title": "Death Certificate Registration",
                    "link": "https://bdris.gov.bd/br/application"
                },
                {
                    "id": 16,
                    "title": "Married Certificate Correction",
                    "link": "https://bdris.gov.bd/br/application"
                }
            ]
        }

        return data
    
    def get(self, request):
        return Response(self.mock_data(), HTTP_200_OK)